import streamlit as st
from sqlalchemy import text

def render_sidebar_info():
    """Render sidebar information and database status"""
    st.sidebar.title("🎬 Sakila DVD Rental")
    
    # Add database connection status only when Refresh Data is clicked
    db_status = st.sidebar.empty()
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
        try:
            from Backend import create_db_engine
            engine = create_db_engine()
            if engine:
                with engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                db_status.success("✅ Database Connected")
            else:
                db_status.error("❌ Database Offline")
        except Exception as e:
            db_status.error(f"❌ Database Offline: {str(e)}")
        st.rerun()