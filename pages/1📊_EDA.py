import streamlit as st
from Backend import get_daily_rentals, get_store_benefit, get_top_movies, get_unique_movies_rented
from UI_components import render_sidebar_info
import plotly.express as px
import plotly.graph_objects as go

# Navigation
render_sidebar_info()

st.title("📊 Exploratory Data Analysis")

# Load data with loading states
with st.spinner("Loading rental data..."):
    daily_rentals = get_daily_rentals()
with st.spinner("Loading store benefits..."):
    store_benefit = get_store_benefit()
with st.spinner("Loading top movies..."):
    top_movies = get_top_movies()

# Check if data was loaded successfully
if daily_rentals.empty or store_benefit.empty or top_movies.empty:
    st.error("❌ Failed to load data from database. Please check your database connection.")
    st.stop()

# Add some summary statistics
st.subheader("📈 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    if not daily_rentals.empty:
        total_rentals = daily_rentals['rental_count'].sum()
        st.metric("Total Rentals (2005)", f"{total_rentals:,}")

with col2:
    if not store_benefit.empty:
        total_benefit = store_benefit['benefit'].sum()
        st.metric("Total Benefit", f"${total_benefit:,.2f}", 
                 help="Total revenue from all rental payments (before expenses)")

with col3:
    if not top_movies.empty:
        unique_movies_count = get_unique_movies_rented()
        st.metric("Unique Movies Rented (2005)", unique_movies_count)

st.markdown("#####")
col_filter1, col_filter2 = st.columns([1, 3])
with col_filter1:
    store_filter = st.selectbox(
        "Select Store(s):",
        options=["All Stores", "Store 1 Only", "Store 2 Only"],
        index=0,  # Default to "All Stores"
        help="Choose which store(s) to display in the line plot"
    )
with col_filter2:
    st.write("")  # Empty space for alignment

# Line plot of daily rentals

daily_pivot = daily_rentals.pivot_table(
    values='rental_count', 
    index='rental_date', 
    columns='store_id', 
    fill_value=0
).reset_index()

daily_pivot.columns = [str(int(col)) if isinstance(col, float) or isinstance(col, int) else col for col in daily_pivot.columns]

# Filter data based on selection
if store_filter == "Store 1 Only":
    # Keep only Store 1 data
    if '1' in daily_pivot.columns:
        daily_pivot_filtered = daily_pivot[['rental_date', '1']].copy()
    else:
        daily_pivot_filtered = daily_pivot.copy()
elif store_filter == "Store 2 Only":
    # Keep only Store 2 data
    if '2' in daily_pivot.columns:
        daily_pivot_filtered = daily_pivot[['rental_date', '2']].copy()
    else:
        daily_pivot_filtered = daily_pivot.copy()
else:
    # Both stores (default)
    daily_pivot_filtered = daily_pivot.copy()

daily_pivot_melted = daily_pivot_filtered.melt(id_vars='rental_date', var_name='Store', value_name='Rentals')

# Update title based on filter
if store_filter == "Store 1 Only":
    plot_title = '📅 Daily Rentals - Store 1 Only (2005)'
elif store_filter == "Store 2 Only":
    plot_title = '📅 Daily Rentals - Store 2 Only (2005)'
else:
    plot_title = '📅 Daily Rentals by Store in 2005'

fig = px.line(
    daily_pivot_melted, 
    x='rental_date', y='Rentals', color='Store',
    title=plot_title,
    labels={'rental_date': 'Date', 'Rentals': 'Number of Rentals'},
    template='plotly_white',
    color_discrete_map={
        '1': "#1faab4",  
        '2': "#f67fa3"   
    }
)
fig.update_traces(line=dict(width=2))
fig.update_layout(
    title_font_size=28,
    xaxis=dict(tickfont=dict(size=14)),
    yaxis=dict(tickfont=dict(size=14)),
    xaxis_title_font=dict(size=16),
    yaxis_title_font=dict(size=16),
    legend_title_font=dict(size=14),
    legend_font=dict(size=14),
    font=dict(size=14),  # General font size
    margin=dict(t=40, b=20)
)
st.plotly_chart(fig, width="stretch")
st.markdown("######")



#Bar plot of total benefit

st.caption("*Benefit calculated as total revenue from rental payments (before operational costs)")

fig = go.Figure()

colors = ["#1faab4", "#f67fa3"]  # Blue and orange—clean and professional

for i, row in store_benefit.iterrows():
    store_label = f"Store {int(row['store_id'])}"  
    fig.add_trace(go.Bar(
        x=[store_label],
        y=[row['benefit']],
        marker_color=colors[i],
        text=f"${row['benefit']:,.0f}",
        textposition='outside',
        name=store_label
    ))

fig.update_layout(
    title='💰 Total Benefit by Store',
    xaxis_title='Store',
    yaxis_title='Total Benefit ($)',
    xaxis=dict(tickfont=dict(size=14)),
    yaxis=dict(tickfont=dict(size=14)),
    template='plotly_white',
    showlegend=False,
    margin=dict(t=40, b=20),
    title_font_size=28,
    xaxis_title_font=dict(size=16),
    yaxis_title_font=dict(size=16),
    font=dict(size=14)
)

st.plotly_chart(fig, width="stretch")

# Add clarification about benefit calculation
with st.expander("ℹ️ About Benefit Calculation"):
    st.write("""
    **Benefit Definition**: In this analysis, "benefit" refers to **total revenue** generated by each store.
    
    **Calculation**: Sum of all rental payment amounts per store
    - ✅ **Includes**: All customer payments for movie rentals
    - ❌ **Excludes**: Operational costs, staff salaries, movie acquisition costs, overhead
    
    **Business Context**: This represents gross revenue before any business expenses are deducted.
    For true profit analysis, operational costs would need to be subtracted from these figures.
    """)


# Top 5 most rented movies by store
st.subheader("Top 5 Most Rented Movies by Store in 2005")

if not top_movies.empty:
    for store_id in top_movies['store_id'].unique():
        st.write(f"**Store {store_id}**")
        store_data = top_movies[top_movies['store_id'] == store_id].head(5)
        
        # Display as a nice table
        display_df = store_data[['title', 'rental_count']].copy()
        display_df['rental_count'] = display_df['rental_count'].astype(int)
        display_df = display_df.rename(columns={
            'title': 'Movie Title',
            'rental_count': 'Rental Count'
        })
        
        st.dataframe(display_df.reset_index(drop=True), width="stretch")
        st.write("")  # Add some space
else:
    st.warning("No top movies data available")

