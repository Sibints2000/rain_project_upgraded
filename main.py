import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9fcfa411c1742820ff1de86d72434f2c"
account_sid = "AC88a8c9dc2194c9afa111d4f97f50afae"
auth_token = "be7bdde9a96548aaea6d39643176a1e3"

weather_params = {
    "lat": 12.871930,
    "lon":  74.832540,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.Remember to bring an umbrella.",
        from_="+16318306012",
        to="+91 77602 79160",
    )
    print(message.status)


