import streamlit as st
from nav import navigation

from sections import home, projects, contact

st.set_page_config(page_title="Victor Zion Portfolio", layout="wide", page_icon="👩🏿‍💻")

page = navigation()

if page == "Home":
    home.render()
elif page == "Projects":
    projects.render()
elif page == "Contact":
    contact.render()