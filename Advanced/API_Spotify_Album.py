#Spotify API
#Buscar toda la discografia de Camilo
#Metodos de autorizacion y autenticacion de APIs: Ejemplo de OAuth


#necesitamos codificar el envio de datos, esta libreria nos ayuda con eso
import base64

import requests
import pandas as pd


#credenciales, modificar de acuerdo a su usuario y lo que les dé la API de Spotify
#la documentacion de la API de Spotify esta aqui:
#https://developer.spotify.com/documentation/web-api/reference/

username = 'nico.marquez@hotmail.com'
password= 'Spotymarquez22'
consumer_key = 'a26daeed7c2947e18c4c2ea0aef07e64'
consumer_secret = '6202c2f7fd3b4142a1ad7343cfce1d09'

#codificamos las credenciales
consumer_key_secret = consumer_key+":"+consumer_secret
consumer_key_secret_enc = base64.b64encode(consumer_key_secret.encode()).decode()


#Las comunicaciones mas complejas llevan un Header o encabezado antes del mensaje en si 
#en este caso vamos a usar este formato de encabezado para indicar que queremos autorizarnos
#ante la API como un "logueo"
headersAuth = {
    'Authorization': 'Basic '+ str(consumer_key_secret_enc),
}

#y como datos vamos a enviar nuestro user y password
data = {
  'grant_type': 'client_credentials',
  'username': username,
  'password': password
}

## Post Request a Spotify para pedir token de autorizacion
## Hasta ahora pediamos datos,ahora estamos enviando ya no es GET, es POST
## Siempre lo hacemos hacia un Endpoint o direccion Web que informa la API
## En este caso ,por como funciona el proceso de autorizacion de Oauth
## Primero necesitamos un token antes de poder usar la API

response_auth = requests.post('https://accounts.spotify.com/api/token', data=data,headers=headersAuth, verify=True)
json_data = response_auth.json()
access_token=json_data['access_token']


#Una vez tenemos el token, podemos hacer Get Request normalmente
# La diferencia es que tenemos que incluir el token en cada request con Oauth
# Lo ponemos en el encabezado,usando este tipo de formato

headers = {
     'accept': 'application/json',
     'Authorization': 'Bearer '+access_token,
 }


# Parametros que pide la llamada a la  API
#estamos usando la API de busqueda de Spotify,la documentacion esta aqui
#https://developer.spotify.com/documentation/web-api/reference/#category-search
#Primero leer bien la documentacion y probar desde el sitio de Spotify las consultas
#antes de escribir codigo en Python
#Buscamos albumes de Camilo
params = {
     'q': 'camilo',
     'type': 'album'
 }


#Hacemos un Get Request con el Encabezado, que contiene el token de acceso
#y los parametros de busqueda
response = requests.get('https://api.spotify.com/v1/search?',                                                
                        headers=headers,
                        params=params, 
                        verify=True)

#pedimos los datos en formato JSON
api_response = response.json()


#Basicamente el JSON esta anidado,tiene multiples niveles
#y usamos el Variable Explorer para ver donde estan los datos exactamente
#y luego indicarle a Pandas de donde sacarlos
df_response=pd.json_normalize(
    data=api_response['albums'],
    record_path=(['items'])
    )

#Modificamos el Dataframe con las columnas que necesitamos
dualipa_releases=df_response[['name','release_date','total_tracks','album_type']]


print(dualipa_releases)