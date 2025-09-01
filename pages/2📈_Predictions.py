import streamlit as st
from Backend import get_movie_database, find_similar_movies
from UI_components import render_sidebar_info

# Side_bar
render_sidebar_info()

st.title("🔮 Movie Recommendation System")

st.write("""
Enter a movie description below and get the top 3 most similar movies from our database.
The system uses advanced natural language processing to find matches based on content.
""")

# Check if movie database is available
with st.spinner("Loading movie database..."):
    movie_db = get_movie_database()

if movie_db.empty:
    st.error("❌ Could not load movie database. Please check your database connection.")
    st.info("Make sure the Sakila database is installed and contains the 'film' table.")
    st.stop()

# Show some stats
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Movies", len(movie_db))
with col2:
    st.metric("Unique Ratings", movie_db['rating'].nunique())

# Text area for movie description input
movie_description = st.text_area(
    "Enter a movie description:",
    height=150,
    placeholder="Describe a movie you're interested in...\nExample: 'A space adventure with aliens and spaceships'",
    help="Be as descriptive as possible for better results"
)

if st.button("🎯 Get Your Prediction", type="primary"):
    if movie_description.strip():
        with st.spinner("Finding similar movies..."):
            # Get similar movies
            similar_movies = find_similar_movies(movie_description)
            
            if similar_movies:
                # Display results
                st.subheader("🎬 Top 3 Similar Movies:")
                
                for i, (title, rating, similarity) in enumerate(similar_movies, 1):
                    # Create columns for better layout
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.markdown(f"**{i}. {title}**")
                        # Get the full description from database
                        movie_desc = movie_db[movie_db['title'] == title]['description'].iloc[0]
                        st.caption(f"*{movie_desc}*")
                    
                    with col2:
                        # Color code ratings
                        rating_color = {
                            'G': 'green',
                            'PG': 'blue',
                            'PG-13': 'orange',
                            'R': 'red',
                            'NC-17': 'darkred'
                        }.get(rating, 'gray')
                        st.markdown(f"<span style='color: {rating_color}; font-weight: bold;'>Rating: {rating}</span>", 
                                  unsafe_allow_html=True)
                    
                    with col3:
                        # Color code similarity score
                        similarity_color = "green" if similarity > 0.7 else "orange" if similarity > 0.5 else "red"
                        st.markdown(f"<span style='color: {similarity_color}; font-weight: bold;'>Similarity: {similarity:.3f}</span>", 
                                  unsafe_allow_html=True)
                    
                    st.divider()
            else:
                st.warning("No similar movies found. Try a different description.")
    else:
        st.warning("Please enter a movie description to get recommendations.")

# Show sample of available movies with pagination
with st.expander("📋 Browse Available Movies"):
    movies_per_page = 10
    total_movies = len(movie_db)
    total_pages = (total_movies + movies_per_page - 1) // movies_per_page  # Ceiling division
    
    # Initialize page number in session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1
    
    # Page navigation controls
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("◀ Previous", disabled=(st.session_state.current_page <= 1)):
            st.session_state.current_page -= 1
            st.rerun()
    
    with col2:
        st.markdown(f"<div style='text-align: center; font-weight: bold;'>Page {st.session_state.current_page} of {total_pages}</div>", 
                   unsafe_allow_html=True)
    
    with col3:
        if st.button("Next ▶", disabled=(st.session_state.current_page >= total_pages)):
            st.session_state.current_page += 1
            st.rerun()
    
    # Calculate start and end indices for current page
    start_idx = (st.session_state.current_page - 1) * movies_per_page
    end_idx = start_idx + movies_per_page
    
    # Show movies for current page
    current_page_movies = movie_db[['title', 'rating', 'description']].iloc[start_idx:end_idx]
    
    st.dataframe(
        current_page_movies,
        width="stretch",
        hide_index=True
    )
    
    st.caption(f"Showing movies {start_idx + 1}-{min(end_idx, total_movies)} of {total_movies} available movies")
