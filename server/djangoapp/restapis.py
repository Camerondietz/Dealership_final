import requests
import os
from dotenv import load_dotenv
from django.http import JsonResponse

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    
    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None

def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    
    try:
        response = requests.get(request_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error occurred: {e}")
        return None

def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    print(f"Complete URL: {request_url}")
    print(f"Type of data being passed to post_review: {type(data_dict)}")

    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None