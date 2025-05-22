"""
This module provides a function to perform sentiment analysis using
the Watson NLP BERT Sentiment Analysis model via an HTTP POST request.

Dependencies:
    - requests: Required to send HTTP requests to the Watson NLP API.
"""

import json

import requests


def sentiment_analyzer(text_to_analyse: str) -> str:
    """
    Analyze the sentiment of a given text using
    the Watson NLP BERT Sentiment Analysis model.

    Args:
        text_to_analyse (str): The input text to be analyzed.

    Returns:
        str: A string describing the sentiment label and score,
        or an error message if the analysis fails.
    """
    try:
        url = (
            "https://sn-watson-sentiment-bert.labs.skills.network/v1/"
            "watson.runtime.nlp.v1/NlpService/SentimentPredict"
        )
        myobj = {"raw_document": {"text": text_to_analyse}}
        header = {
            "grpc-metadata-mm-model-id": (
                "sentiment_aggregated-bert-workflow_lang_multi_stock"
            )
        }

        response = requests.post(url, json=myobj, headers=header, timeout=10)
        response.raise_for_status()

        result = json.loads(response.text)

        label = None
        score = None

        if response.status_code == 200:
            label = result["documentSentiment"]["label"]
            score = result["documentSentiment"]["score"]

        return {"label": label, "score": score}

    except requests.exceptions.RequestException as e:
        return f"Network error during sentiment analysis: {e}"
    except ValueError as e:
        return f"Error parsing response: {e}"
