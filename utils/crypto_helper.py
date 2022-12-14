from dotenv import load_dotenv
import pandas as pd
import numpy as np

from pycoingecko import CoinGeckoAPI
crypto = CoinGeckoAPI()

# load global variables
load_dotenv(dotenv_path='credentials.env')  

def infoCoinMarkets():
    coinList = []
    data = crypto.get_coins_markets('usd')
    # print(data) 

    for el in data :
        crypto_info = {
            'Crypto_ID': el['market_cap_rank'],
            'Crypto_Name': el['name'],
            'Crypto_Price': el['current_price'],
            'Market_Cap': el["market_cap"],
            'Total_Supply': el["total_supply"],
            'Circulating_Supply': el["circulating_supply"],
            'Price_High_24h': el["high_24h"],
            'Price_Low_24h': el["low_24h"],
            'Price_Change_Perchentage_24h': el["price_change_percentage_24h"],
        }
        coinList.append(crypto_info)
        items = pd.DataFrame(coinList)
        # print(items)
        
    return items
        
infoCoinMarkets()


