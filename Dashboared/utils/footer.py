# utils/footer.py
import streamlit as st

def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style="background:#0B1F4D;padding:30px;border-radius:15px;text-align:center;color:white;">
    <h2>🌧️ TRUERIZE Dashboard</h2>
    <p>© 2026 <b>TRUERIZE Strategic Solutions Pvt. Ltd.</b></p>
    <p>All Rights Reserved.</p>
    </div>
    """, unsafe_allow_html=True)