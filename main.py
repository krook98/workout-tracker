import os
import requests
from datetime import datetime


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
print(result)

today = datetime.now()
hour = f"{today.hour}:{today.minute}:{today.second}"

for exercise in result['exercises']:
    bearer_token = {
        'Authorization': os.environ.get('TOKEN')
    }

    sheety_params = {
        'workout': {
            'date': today.strftime('%x'),
            'time': hour,
            'exercise': result['exercises'][0]['name'].title(),
            'duration': result['exercises'][0]['duration_min'],
            'calories': result['exercises'][0]['nf_calories']
        }
    }

    sheety_response = requests.post(
        url=os.environ.get('SHEETY_ENDPOINT'),
        json=sheety_params,
        headers=bearer_token
    )