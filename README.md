🤖 Mon AI Assistant - AI-Powered PDF Questioning Tool

🏆 Hackathon de rentrée 2024 • 🎓 AI-driven learning assistant

📌 Overview

During our back-to-school hackathon, we built a Flask-based AI assistant that allows users to upload PDFs and generate AI-powered questions to test their understanding of the content.

📚 Problem: Students often struggle to retain key concepts from lecture notes and PDFs.
💡 Solution: An AI assistant that generates contextual questions based on course materials and provides feedback on user responses.

⚙️ Tech Stack

🔹 Backend: Flask, Python
🔹 Database: SQLite (via Flask-SQLAlchemy)
🔹 PDF Processing: PyMuPDF (fitz)
🔹 Frontend: HTML, Jinja2
🔹 LLM Integration: OpenAI API

🎯 Features

✅ PDF Upload & Parsing – Users can upload course materials in PDF format
✅ AI-Powered Question Generation – Generates questions based on uploaded content
✅ Response Evaluation – Assesses user answers and provides feedback
✅ Dark Mode Preference – User settings stored in a local database
✅ Web Interface – Simple and intuitive UI using Flask & Jinja

📖 How to Run Locally

1️⃣ Clone the Repository

git clone https://github.com/yourusername/mon-ai-assistant.git
cd mon-ai-assistant

2️⃣ Set Up the Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt

3️⃣ Run the Flask Application

python main.py

Once running, click on the link displayed in the terminal (http://127.0.0.1:5000/) to access the web app.

🔍 Preview:
<img width="1461" alt="Capture d’écran 2025-02-20 à 18 02 46" src="https://github.com/user-attachments/assets/e207b40b-602b-459c-8cdb-0a69c80089ac" />
<img width="1461" alt="Capture d’écran 2025-02-20 à 18 11 55" src="https://github.com/user-attachments/assets/8e07c8a6-acb1-466d-935f-0744eafbc8ea" />

📈 Results & Achievements

🏆 Successfully built an AI-driven educational assistant in 48 hours.
⚡ Integrated PDF parsing and question generation using OpenAI’s LLMs.
🚀 Designed a clean and functional Flask web app with a user-friendly interface.

(https://m33.notion.site/Projet-Web-Python-ENPC-2024-ded99a2530e041cf921321cb696db202)

