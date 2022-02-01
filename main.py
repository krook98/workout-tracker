import os
import requests


API_ID = os.environ.get('API_ID')
API_KEY = os.environ.get('API_KEY')
EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = 'male'
WEIGHT_KG = 80
HEIGHT_CM = 172
AGE = 23

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

exercise_params = {
    'query': input('Tell me which exercise you did'),
    'gender': 'male',
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
exercise_response.raise_for_status()
result = exercise_response.json()
