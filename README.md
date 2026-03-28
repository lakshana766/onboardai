# OnboardAI — Setup Instructions

## Your project structure
```
onboardai/
├── app.py            ← Flask backend (runs the server)
├── .env              ← Your secret API key lives here
├── requirements.txt  ← Python packages needed
└── static/
    └── index.html    ← Frontend (the app users see)
```

## Step 1 — Add your Gemini API key
Open the `.env` file and replace `paste_your_key_here` with your actual key:
```
GEMINI_API_KEY=AIzaSy...your key here...
```
Get a free key at: https://aistudio.google.com

## Step 2 — Install dependencies
Open your terminal in the `onboardai` folder and run:
```
pip install -r requirements.txt
```

## Step 3 — Run the app
```
python app.py
```

## Step 4 — Open in browser
Go to: http://localhost:5000

That's it! Users just chat normally — they never see or need the API key.
