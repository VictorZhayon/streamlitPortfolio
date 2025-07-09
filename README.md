# Victor Zion Portfolio

A modern, interactive portfolio web app built with [Streamlit](https://streamlit.io/). This project showcases Victor Zion's skills, projects, and contact information, and is designed for developers, recruiters, and collaborators.

---

## 🚀 Features

- **Home Page:**
  - Professional profile with photo, resume download, and a summary of skills and interests.
  - Custom CSS for a unique, branded look.
  - Tech stack overview (Frontend, Backend, AI/ML, Blockchain, Databases, Tools).
  - Hobbies and personal interests.

- **Projects Page:**
  - Categorized project showcase (AI/ML, Blockchain, Technical Writing, Frontend, Mobile).
  - Each project includes a title, description, and link (if available).

- **Contact Page:**
  - Social links (GitHub, Twitter/X, LinkedIn, WhatsApp).
  - Contact form to send messages directly (via email handler).

---

## 🏗️ Project Structure

```
StreamlitPortfolio/
│   main.py                # App entry point
│   nav.py                 # Sidebar navigation
│
├── assets/                # Static assets (CSS, images, resume)
│     custom.css
│     profile_img.jpg
│     resume.pdf
│
├── sections/              # App sections/pages
│     home.py
│     projects.py
│     contact.py
│
├── utils/                 # Utility modules
│     load_projects.py     # Loads project data
│     email_handler.py     # Handles contact form email
│
└── README.md              # README.md file
```

---

## 🛠️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/VictorZhayon/StreamlitPortfolio.git
cd StreamlitPortfolio
```

### 2. Install Dependencies
Create a `requirements.txt` file with the following (or use your preferred method):

```
streamlit
Pillow
```

If you use the contact form (email), also add:
```
smtplib
```

Then install:
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

---

## ⚙️ Configuration
- **Custom CSS:** Modify `assets/custom.css` for theming.
- **Profile Image & Resume:** Replace `assets/profile_img.jpg` and `assets/resume.pdf` with your own.
- **Email Handler:** Update credentials in `utils/email_handler.py` for contact form functionality.

---

## 📂 Project Data
- Project data is managed in `utils/load_projects.py` as a Python dictionary. Add or edit your projects there.

---

## 📧 Contact
- Social links and contact form are in `sections/contact.py`.
- To enable email, configure your email and password in `utils/email_handler.py` (use environment variables for security in production).

---

## 📜 License
This project is for personal portfolio use. Feel free to fork and adapt for your own portfolio!

---

## 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Pillow](https://python-pillow.org/)
- [Python](https://python.org/)

---

**Made with ❤️ by Victor Zion**
