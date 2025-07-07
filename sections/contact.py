### pages/3_Contact.py
import streamlit as st
from utils.email_handler import send_email

def render():
    st.title("📲 Contact Me")
    st.write("You can reach out to me via the following:")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.link_button('🐙Github', url='https://github.com/VictorZhayon', type= "tertiary")
    with col2:
        st.link_button('🌐Twitter (X)', url='https://x.com/VictorZhayon', type= "tertiary")
    with col3:
        st.link_button('👨🏿‍💼LinkedIn', url='https://linkedin.com/in/victor-zion', type= "tertiary")
    with col4:
        st.link_button('📞WhatsApp', url='https://wa.com/+2348105123142', type= "tertiary")

    with st.form("contact_form", border= False):
        name = st.text_input("Your Name", placeholder= "John Doe")
        email = st.text_input("Your Email", placeholder= "example@email.com")
        message = st.text_area("Your Message", placeholder= "Say, 'Hi!😁'")
        submitted = st.form_submit_button("Send", type= "primary")

        if submitted:
            success = send_email(name, email, message)
            if success:
                st.success("Message sent successfully!", icon="🎉")
            else:
                st.error("Failed to send message. Please try again.", icon="☹")
