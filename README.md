# 🫀 BRO Health AI – Heart Attack & SHD Diagnosis App
This is a GUI-based clinical AI application for early diagnosis of Structural Heart Disease (SHD) and heart-related symptoms. Designed to assist patients, doctors, and rural health workers, the app analyzes patient vitals, lifestyle, and symptoms using Google Gemini 2.5 Pro and provides a complete diagnostic summary + hospital suggestions + doctor-ready PDF report — all offline with a simple .exe file.

💡 No prior medical knowledge required. Built for accessibility and awareness in low-resource or rural settings.
---
# 🚀 Features
✅ Core Functionality
💬 AI-powered health analysis (via Gemini 2.5 Pro)

🩺 Predicts Structural Heart Disease (SHD) risk score (0–10 scale)

⚠️ Flags urgent consult requirements

🧪 Suggests medical tests (ECG, ECHO, etc.)

📋 Lists possible SHD conditions (ASD, VSD, Valve disorders, etc.)

🧑‍⚕️ Provides a clinical summary to show your doctor

🏥 Recommends top 3 hospitals in your city for cardiology

📄 Exports PDF health report for clinical use

📶 Gives rural alternatives for low-tech screening

🔴 Highlights "Red Flags" and long-term care suggestions


---
# 🖥️ Tech Stack
Python 3.10+

Tkinter for GUI

Google Gemini 2.5 Pro API for diagnosis

fpdf for exporting structured .pdf reports

Converted to .exe for Windows users using pyinstaller

# 🧠 How it Works
User inputs personal, lifestyle, vitals, and symptoms info via GUI

AI builds a medical prompt and sends it to Gemini

Gemini analyzes and returns:

Risk score

Urgency level

Test suggestions

Disease possibilities

Care advice

Nearby hospitals

Output is shown in-app and downloadable as PDF

---
# 🖼️ Screenshots
![WhatsApp Image 2025-07-11 at 16 28 15_fd3e71b3](https://github.com/user-attachments/assets/2d139b66-d9c1-471b-b664-24a4b81ba735)

---
# 💻 Clean, scrollable UI with categorized fields

📈 One-click analysis & output summary

📄 Save as printable PDF

# 🔑 API Key Setup (Google Gemini)
You must have a Google AI Studio API Key

Go to Google AI Studio

Generate your Gemini API key

Replace this line in the code:

python
Copy
Edit
API_KEY = "YOUR-API-KEY-HERE"
# IF YOU DON'T HAVE API YOU CAN USE THE .EXE FILE SORRY BUT I CAN'T SHOW MY API KEY HERE
---


# 👨‍💻 Author
# Rohit Yadav
🎓 NIT Jalandhar | 💻 Systems Developer | 🧠 AI & Compiler Enthusiast
🌐 Portfolio | 💬 LinkedIn | 🛠️ GitHub

# 💡 Future Plans
🩺 Integrate real-time vitals via medical devices

🌍 Add support for multiple languages (Hindi, Bengali, etc.)

🤖 Use Llama3 / Mistral locally for offline diagnosis

📲 Android app version (coming soon)

# 🛡️ Disclaimer
This is NOT a replacement for clinical diagnosis. It is an awareness + triage tool intended for educational or supportive health assessment. Please consult a certified doctor for final medical decisions.
