import streamlit as st
from UI_components import render_sidebar_info
from Backend import create_db_engine, get_movie_database
from sqlalchemy import text

# Page config
st.set_page_config(
    page_title="Sakila DVD Rental Analysis",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapsed for faster main page rendering
)

# Navigation
render_sidebar_info()

# Main content
st.title("🎬 Sakila DVD Rental Store Analysis")

# Single connection check, result reused
try:
    engine = create_db_engine()
    db_connected = False
    if engine:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_connected = True
        st.success("✅ Successfully connected to Sakila database")
    else:
        st.error("❌ Database connection failed.")
        st.info("Please check your database configuration in the .env file")
except Exception as e:
    st.error(f"❌ Database connection failed: {e}")
    st.info("Please check your database configuration in the .env file")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Welcome to Sakila DVD Rental Analysis")
    st.write("""
    This application provides comprehensive analysis of the Sakila DVD rental store operations.
    
    **Features include:**
    - 📊 **EDA Analysis**: Explore rental patterns and store performance
    - 📈 **Visualizations**: Daily rentals, store benefits, and top movies
    - 🔮 **Movie Recommendations**: Find similar movies based on description using AI
    - ☁️ **Cloud Database**: Powered by Supabase PostgreSQL for reliable performance
    
    Use the page navigation above to explore different sections of the analysis.
    """)
    
    st.subheader("About Our Setup")
    st.write("""
    This application uses the Sakila sample database hosted on **Supabase** (PostgreSQL):
    - **🗄️ Database**: Sakila sample data hosted on Supabase cloud
    - **🎬 1,000 Films** with descriptions, ratings, and categories
    - **🏪 2 Stores** with complete rental history and analytics
    - **📅 Historical Data** from 2005-2006 period
    - **🤖 AI-Powered**: Movie recommendations using Sentence Transformers
    """)
    
    # Show some quick stats (cached)
    @st.cache_data
    def cached_movie_db():
        return get_movie_database()
    try:
        movie_db = cached_movie_db()
        if not movie_db.empty:
            st.metric("Movies in Database", len(movie_db))
    except:
        pass

with col2:
    # ADDED IMAGE HERE - DVD rental store image
    st.image("images/dvd_store.jpg", 
             caption="DVD Rental Store", 
             width='stretch')
    
    st.info("""
    **Getting Started:**
    1. 📊 Check EDA for comprehensive data insights
    2. 📈 Use Predictions for AI-powered movie recommendations
    3. ☁️ All data served from Supabase cloud database
    """)

# Add another image below the main content for better visual appeal
st.markdown("---")
st.subheader("📀 Our Movie Collection")

# Add multiple images in a grid (consider compressing images for faster load)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/action_movies.jpg",
             caption="Action Movies Collection",
             width='stretch')

with col2:
    st.image("images/classic_films.jpg",
             caption="Classic Films",
             width='stretch')
         
with col3:
    st.image("images/drama_romance.jpg",
             caption="Drama & Romance",
             width='stretch')

# Add system requirements
with st.expander("⚙️ Tech Stack & Requirements"):
    st.write("""
    **Technology Stack:**
    - 🐍 **Python 3.8+** - Core application language
    - 🌐 **Streamlit** - Web application framework
    - ☁️ **Supabase** - PostgreSQL cloud database hosting
    - 🤖 **Sentence Transformers** - AI model for movie recommendations
    - 📊 **Plotly** - Interactive data visualizations
    - 🔗 **SQLAlchemy** - Database connection and queries
    
    **Setup Requirements:**
    - Streamlit secrets configuration for Supabase connection
    - Python packages listed in requirements.txt
    - Internet connection for cloud database access
    """)
    # Add a technical image
    st.image("images/cloud_tech.jpg",
             caption="Cloud Database Technology",
             width='stretch')