import requests

request_url="https://swapi.dev/api/planets/1/"

r = requests.get(request_url)

status_code = r.status_code

if status_code == 200:
    print("Exito en la conexion")
else:
    print("NOK conexion")

response_data = r.json()
print(response_data)