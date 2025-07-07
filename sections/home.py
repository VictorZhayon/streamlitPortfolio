### main.py
import streamlit as st
from pathlib import Path
from PIL import Image

# Load assets
def render():
    profile_pic = Image.open("assets/profile_pic.jpg")
    resume_file = "assets/resume.pdf"

    # Custom CSS
    with open("assets/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    # Header
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(profile_pic, width=200, caption="<img> Victor Zion </img>")
    with col2:
        st.title("👋🏽Hi! I'm Victor Zion")
        st.subheader("AI Engineer || Python Engineer || Technical Researcher")
        st.write("""
            - 🔬 Building RAG systems, AI assistants, and backend infrastructures.
            - 🧠 Passionate about teaching technical writing and prompt engineering.
            - 📚 Writing API/SDK docs, research reports, and technical documentations.
        """)
        st.download_button("📄 Download Resume", resume_file, file_name="Victor_Zion_Resume.pdf")

    st.divider()
    st.markdown("## 🛠️ Tech Stack")

    cols = st.columns(3)
    with cols[0]:
        st.markdown("#### 🎨Frontend")
        st.markdown("**Streamlit, HTML5, CSS3, Flutter/Dart, JavaScript**")
        
        st.markdown("#### ⚙Tools ")
        st.markdown("**Git/Github, Docker, Postman**")
        
    with cols[1]:
        st.markdown("#### 👨🏿‍💻Backend")
        st.markdown("**Python, FastAPI, Flask**")

        st.markdown("#### 🤖Artifical Intelligence/Machine Learning") 
        st.markdown("**LangChain, Transformers, RAG, HuggingFace, NLP**")
        
    with cols[2]:
        st.markdown("#### ⛓Blockchain/Web3")
        st.markdown("**Solana, solana-py, Bitcoin**")
        
        st.markdown("#### 📚Database")
        st.markdown("**MongoDB, Pinecone, FAISS, Chroma**")

    st.divider()
    st.markdown("## 🤹🏽‍♂️ Hobbies")
    st.write("- 🎵 Listening to music and podcasts, playing the Piano, studying Music Theory")
    st.write("- 📖 Reading books relating to space science, self-development, fiction... reading in general😁")
    st.write("- 🌐 Surfing the net.")
    st.write("- 🧘🏽‍♂️ Spending time alone.")
    st.divider()
    st.markdown("👉 Use the sidebar to explore my projects, blog posts, and contact info.")