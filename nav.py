import streamlit as st

def navigation():
    # Sidebar
    with st.sidebar:
        st.markdown("# 📌 Navigation")
        page = st.radio("Routes", ["Home", "Projects", "Contact"])
        
    return page
        