#  OnboardAI — AI-Powered Employee Onboarding Platform

A smart employee onboarding platform powered by Google Gemini AI. Automates task generation, tracks progress across departments, and provides an AI assistant to guide employees through every onboarding step.

 **Live Demo:** https://scintillating-enchantment-production-16f9.up.railway.app

---

##  Features

- **AI Task Assistant** — Employees can chat with Gemini AI for instant help on any onboarding task
- **Auto Task Generation** — Automatically generates role-specific onboarding tasks for Developers, Designers, and HR
- **4 Agent Modules** — HR, IT, Manager, and Monitor agents each handle their own domain
- **Real-time Progress Tracking** — Visual progress bars and task status updates
- **Alerts & Activity Log** — Monitor agent detects delays and fires escalation alerts
- **Secure Backend** — API key is hidden on the server, never exposed to users

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| AI | Google Gemini 2.5 Flash API |
| Hosting | Railway |

---

##  Project Structure

```
onboardai/
├── app.py            ← Flask backend server
├── requirements.txt  ← Python dependencies
├── .env              ← API key (never commit this!)
└── static/
    └── index.html    ← Frontend UI
```

---

##  Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/onboardai.git
cd onboardai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Gemini API key**

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
Get a free key at: https://aistudio.google.com

**4. Run the app**
```bash
python app.py
```

**5. Open in browser**
```
http://localhost:5000
```

---

##  Environment Variables

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Your Google Gemini API key |
| `PORT` | Port to run the server on (default: 5000) |

---

##  Notes

- Free tier allows **5 requests per minute** on Gemini 2.5 Flash
- Never commit your `.env` file — add it to `.gitignore`
- The API key is stored securely on the backend — users never see it

---

##  Built for Hackathon

This project was built as a prototype for a student hackathon, demonstrating how AI agents can streamline the employee onboarding process in modern organizations.






