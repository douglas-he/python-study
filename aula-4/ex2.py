import requests

response = requests.get("https://api.github.com/users")

for user in response.json():
    print(user["login"], user["url"])
