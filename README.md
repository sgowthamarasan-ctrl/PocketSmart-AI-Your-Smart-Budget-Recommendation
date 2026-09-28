# PocketSmart AI: Your Smart Budget & Recommendation

PocketSmart AI is a simple personal-finance dashboard built with Streamlit. It analyzes monthly income and expenses and provides rule-based smart budgeting recommendations.

## Features

- Monthly income and savings-goal input
- Expense tracking by category
- Total expense and remaining-balance calculation
- Savings-rate calculation
- Expense breakdown chart
- Personalized budgeting recommendations
- Responsive Streamlit dashboard
- Ready for GitHub and cloud deployment

## Project Structure

```text
PocketSmart_AI/
├── app.py
├── requirements.txt
├── Procfile
├── Dockerfile
├── .gitignore
├── README.md
└── utils/
    ├── __init__.py
    └── budget_engine.py
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Deploy

You can deploy the project using Streamlit Community Cloud or another service that supports Streamlit.

For Streamlit Community Cloud:
1. Upload this project to GitHub.
2. Open Streamlit Community Cloud.
3. Select your GitHub repository.
4. Choose `app.py` as the main file.
5. Deploy.

## Note

The recommendation engine is rule-based and is intended for budgeting guidance, not professional financial advice.
