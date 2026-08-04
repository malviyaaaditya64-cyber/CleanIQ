import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# ===============================
# Load .env
# ===============================

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("ANTHROPIC_API_KEY")

API_URL = "https://api.anthropic.com/v1/messages"


def build_dataset_context(df):

    memory = round(df.memory_usage(deep=True).sum() / 1024 / 1024, 2)

    context = f"""
Dataset Summary

Rows: {df.shape[0]}
Columns: {df.shape[1]}
Memory: {memory} MB

Column Names:
{", ".join(df.columns)}

Data Types:
{df.dtypes.to_string()}

Missing Values:
{df.isna().sum().to_string()}

Duplicate Rows:
{df.duplicated().sum()}

First Five Rows:

{df.head().to_string()}
"""

    return context


def ask_claude(df, question):
    print("✅ USING REQUESTS VERSION")

    if not API_KEY:
        raise Exception(
            "ANTHROPIC_API_KEY not found inside .env file."
        )

    dataset_context = build_dataset_context(df)

    prompt = f"""
You are CleanIQ AI.

You are an expert Data Scientist.

Your job is to answer questions about the uploaded dataset.

Dataset Information:

{dataset_context}

User Question:
{question}

Instructions:

- Answer naturally like ChatGPT.
- Explain in simple English.
- If the user asks about rows, columns, missing values,
  duplicates or datatypes, calculate from the dataset.
- If the user asks what the dataset is about,
  infer it from column names and sample rows.
- Suggest preprocessing whenever useful.
- Never say "I don't know" unless information truly
  doesn't exist.
"""

    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "claude-sonnet-5",
        "max_tokens": 700,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    if response.status_code != 200:
        raise Exception(response.text)

    data = response.json()

    return data["content"][0]["text"]


if __name__ == "__main__":

    print("✅ FILE IS RUNNING")

    print("API KEY FOUND:", API_KEY is not None)

    print("API KEY:", API_KEY[:20] + "..." if API_KEY else None)

    try:

        response = requests.post(
            API_URL,
            headers={
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-sonnet-5",
                "max_tokens": 20,
                "messages": [
                    {
                        "role": "user",
                        "content": "Say hello"
                    }
                ]
            }
        )

        print("STATUS:", response.status_code)
        print(response.text)

    except Exception as e:
        print(e)

