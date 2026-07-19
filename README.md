# 💳 AI Payment Failure Analyzer

An AI-powered payment transaction analysis system built using **Python, Streamlit, and Google Gemini AI**.

The application analyzes failed payment transactions, identifies the possible root cause, determines the risk level, and provides intelligent suggestions for resolving the issue.

## Features

- Upload payment transaction CSV files
- Detect failed payment transactions
- AI-powered root cause analysis using Gemini
- Risk level identification
- Suggested fixes for each failed transaction
- Dashboard with transaction statistics
- Downloadable CSV report

## Tech Stack

- Python
- Streamlit
- Pandas
- Google Gemini API

## Project Structure

```
AI_Payment_Failure_Analyzer/
│
├── app.py
├── requirements.txt
├── sample_transactions.csv
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Sample Dataset

The project includes a sample payment transaction CSV containing successful and failed payment records for demonstration.
