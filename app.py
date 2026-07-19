import streamlit as st
import pandas as pd
from google import genai

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Payment Failure Analyzer",
    page_icon="💳",
    layout="wide"
)

# -----------------------------
# GEMINI
# -----------------------------

API_KEY = "your api key"

client = genai.Client(
    api_key=API_KEY
)

MODEL_NAME = "gemini-flash-latest"

# -----------------------------
# TITLE
# -----------------------------

st.title("💳 AI Payment Failure Analyzer")

st.write(
    "Upload a payment transaction CSV and let Gemini AI analyze failed payments."
)

uploaded_file = st.file_uploader(

    "Upload CSV",

    type=["csv"]

)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Transactions")

    st.dataframe(df)

    failed = df[df["Status"] == "Failed"]

    st.divider()

    c1, c2 = st.columns(2)

    c1.metric(
        "Total Transactions",
        len(df)
    )

    c2.metric(
        "Failed Payments",
        len(failed)
    )

    analyses = []
    with st.spinner("Analyzing failed payments..."):

        for _, row in failed.iterrows():

            prompt = f"""
You are a Senior FinTech Risk Analyst.

Analyze the following failed payment transaction.

Transaction ID : {row['Transaction_ID']}
Customer : {row['Customer_Name']}
Amount : {row['Amount']}
Payment Method : {row['Payment_Method']}
Bank : {row['Bank']}
Failure Reason : {row['Failure_Reason']}

Return ONLY in this format.

Root Cause:
Risk Level:
Explanation:
Suggested Fixes:
1.
2.
3.
"""

            try:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                analyses.append(response.text)

            except Exception as e:

                analyses.append(f"Gemini Error: {e}")

    st.divider()

    st.subheader("🤖 AI Payment Analysis")

    for i, analysis in enumerate(analyses):

        with st.expander(
            f"Transaction {failed.iloc[i]['Transaction_ID']}",
            expanded=True
        ):

            st.markdown(analysis)

    summary = []

    for _, row in failed.iterrows():

        summary.append({

            "Transaction ID": row["Transaction_ID"],

            "Customer": row["Customer_Name"],

            "Amount": row["Amount"],

            "Failure Reason": row["Failure_Reason"]

        })

    summary_df = pd.DataFrame(summary)

    st.divider()

    st.subheader("📋 Failed Payment Summary")

    st.dataframe(
        summary_df,
        use_container_width=True
    )

    csv = summary_df.to_csv(index=False).encode("utf-8")

    st.download_button(

        "⬇ Download Report",

        data=csv,

        file_name="payment_failure_report.csv",

        mime="text/csv"

    )

    st.success("Analysis Completed Successfully.")