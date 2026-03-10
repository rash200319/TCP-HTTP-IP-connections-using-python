import requests

base_url ="https://vehicleapi.com"

response = requests.get(f"{base_url}/vehicles")

print(response.status_code)
print(response.json())