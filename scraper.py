import requests

response = requests.get("https://www.ceneo.pl/712992#tab=reviews")

print(response.status_code)