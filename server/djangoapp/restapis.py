import requests
import os
from dotenv import load_dotenv
from django.http import JsonResponse

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    print("complete URL:", request_url)
    #print("data: ", data_dict.json())
    print("Type of data being passed to post_review:", type(data_dict))
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # Log connection error
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # Log timeout error
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")  # Log any other request error
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")  # Log JSON decoding issues
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Log any unexpected errors
    return None