import requests

res=requests.get(url="http://api.open-notify.org/iss-now.json")
data=res.json()

longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]


location=(longitude,latitude)
print(location)