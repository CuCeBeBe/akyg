import requests
url="https://makeup-api.herokuapp.com/api/v1/products.json"
response=requests.get(url)
data=response.json()
print(data)
