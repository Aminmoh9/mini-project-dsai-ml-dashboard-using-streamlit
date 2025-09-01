import streamlit as st
from sqlalchemy import text

def render_sidebar_info():
    """Render sidebar information and database status"""
    st.sidebar.title("🎬 Sakila DVD Rental")
    
    # Add database connection status
    try:
        from Backend import create_db_engine
        engine = create_db_engine()
        if engine:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            st.sidebar.success("✅ Database Connected")
        else:
            st.sidebar.error("❌ Database Offline")
    except Exception as e:
        st.sidebar.error(f"❌ Database Offline: {str(e)}")
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Sakila DVD Rental Analysis**  
    Built with Streamlit  
    Data from Supabase PostgreSQL Cloud Database
    
    **Navigation:**
    Use the page selector above to navigate between:
    - 🏠 Home
    - 📊 EDA Analysis  
    - 📈 Predictions
    """)
    
    # Add quick actions
    st.sidebar.markdown("### Quick Actions")
    if st.sidebar.button("🔄 Refresh Data", help="Reload all data from database"):
        st.rerun()