from bs4 import BeautifulSoup
import requests
import time

def getCurrentAssetPrice(ticker):

	#     """The function returns the current price of selected security from finance.yahoo.com.....

#     Parameters
#     ----------
#     ticker : string
#         The symbol of the selected security

#     Returns
#     -------
#     price : float
#         The current, reali-time price of the selected security (ticker)

    source = requests.get(f'https://finance.yahoo.com/quote/{ticker}') 
    soup = BeautifulSoup(source.content, 'lxml')
    price = float(soup.select_one('.Trsdu\(0\.3s\)').text)
    time.sleep(1)
    return(price)


