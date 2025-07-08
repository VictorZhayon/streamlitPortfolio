### pages/1_Projects.py
import streamlit as st
from utils.load_projects import load_projects

def render():
    st.title("👨🏽‍🍳Projects")

    projects = load_projects()

    # Display categories as tabs
    if projects:
        tab_labels = list(projects.keys())
        tabs = st.tabs(tab_labels)
        for tab, category in zip(tabs, tab_labels):
            with tab:
                items = projects[category]
                for project in items:
                    st.markdown(f"### {project['title']}")
                    st.markdown(f"- {project['description']}")
                    if project.get("link"):
                        st.link_button('🔗 View Project', url=project['link'])
                    if project.get("github"):
                        st.link_button('📚 View on GitHub', url=project['github'])
                    st.markdown("---")
    else:
        st.info("No projects found.")
