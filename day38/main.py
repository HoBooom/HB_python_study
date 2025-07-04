import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM = "189"
AGE = "23"
USER_NAME=os.environ.get("USER_NAME")
USER_PASSWORD=os.environ.get("USER_PASS")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("APP_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

#exercise_text = input("Tell me which exercises you did: ")
exercise_text = "30 minutes yoga"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            USER_NAME,
            USER_PASSWORD
        )
    )

    print(sheet_response.text)