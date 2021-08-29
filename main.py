import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "9fcfa411c1742820ff1de86d72434f2c"
account_sid = "AC88a8c9dc2194c9afa111d4f97f50afae"
auth_token = "be7bdde9a96548aaea6d39643176a1e3"

weather_params = {
    "lat":  51.759050,
    "lon":  19.458600,
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
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from="",
        to=""
    )
