import smtplib
from datetime import datetime
import requests
import time

MY_LAT = 51.507351
MY_LONG = -0.127758
my_pos = (MY_LAT,MY_LONG)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0
}

def check_iss_is_my(my_pos):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    iss_position = (longitude, latitude)

    return abs(iss_position[0] - my_pos[0]) <= 5 and abs(iss_position[1] - my_pos[1]) <= 5

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = datetime.now()
    cnt_hour = time_now.hour
    if sunset < cnt_hour or cnt_hour < sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_night() and check_iss_is_my(my_pos):
        temp_email = "<EMAIL>"
        temp_password = "<PASSWORD>"
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=temp_email, password=temp_password)
        connection.sendmail(
            from_addr=temp_email,
            to_addrs=temp_email,
            msg=f"Subject: Look UP🤙!\n\nThe ISS is above U in the sky"
        )
