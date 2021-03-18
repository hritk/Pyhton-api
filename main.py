import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL="your email"
MY_PASSWORD="your pass"




MY_LAT=51.507351
MY_LNG=-0.127758

def is_iss_here():
    res=requests.get(url="http://api.open-notify.org/iss-now.json")
    data=res.json()

    longitude=(float(data["iss_position"]["longitude"]))
    latitude=(float(data["iss_position"]["latitude"]))

    if MY_LAT-5 <= latitude<=MY_LAT+5 and MY_LNG-5<=longitude<=longitude:
        return True


def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    res=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    res.raise_for_status()
    data=res.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now=datetime.now().hour
    if time_now>=sunrise or time_now<=sunset:
         return True
while True:
    time.sleep(60)
    if is_iss_here() and is_night():
        connection =smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= "Subject: look the ISS is here "
        )

