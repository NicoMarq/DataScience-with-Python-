import requests
import pandas as pd



request_url="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=120&interval=daily"
r = requests.get(request_url)
status_code=r.status_code

#si el status code es 200 salio todo bien
#puedo recibir 200 y que no haya ningun dato,eso es normal, 200 indica exito en la conexion
if (status_code==200):
    print("Request exitoso")
    response_data=r.json()
    
    
    #Uso esta funcion de Pandas para convertir del formato JSON 
  
    response_df = pd.json_normalize(
        data=response_data,
        record_path='prices'
        )
  

    response_df[0]=pd.to_datetime(
        response_df[0],
        unit="ms",
        origin="unix"
        )
    
  
    response_df.rename(
        columns={
            0:'date',
            1:'close'
            }, 
        inplace=True)
    

    response_df=response_df.set_index(
        response_df['date']
        )
    

    response_df=response_df.drop(
        ['date'],
        axis=1
        )
    
    #con un dataframe ya limpio,graficar es simplemente una linea 
    response_df.plot(title="BTC - Daily Close")
    

else:
    
    print("Error!")
