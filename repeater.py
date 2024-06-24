import requests
import time

url = 'https://ticket-review-system-flask.onrender.com/'

while True:
    try:
        response = requests.get(url)
        print(f"Status code : {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(870)