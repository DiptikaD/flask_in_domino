import os
import requests
from dotenv import load_dotenv

def getProjects():
    load_dotenv()

    api_key = os.getenv("DOMINO_KEY")

    if api_key is None:
        print("API key not found in environment variables!!")
        exit(1)

    headers = {
        "x-domino-api-key": api_key,
        "Cookie": "dominoSession=639ddf91-358b-4fb9-985b-4181724cd525"
    }

    response = requests.get("https://domino.ksmpartners.com/v4/projects", headers=headers)

    try:
        # attempt to parse json
        response_data = response.json()
        return response_data
    except ValueError as e:
        # if response is not valid json
        print(f"Error decoding JSON: {e}")
        return {"error": "Failed to decode JSON from response"}
    except requests.exceptions.RequestException as e:
        # handle general errors
        print(f"Request failed: {e}")
        return {"error": "Request failed, please check the API URL or network connection"}

if __name__ == '__main__':
    print(getProjects())