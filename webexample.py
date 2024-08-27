import requests

response=requests.get(url="https://www.facebook.com")
print(response.text)