import requests 
from bs4 import BeautifulSoup
import pandas as pd

def yearTargetEst(ticker):
    # url = 'https://finance.yahoo.com/quote/CHEK?p=CHEK'
    url = "https://finance.yahoo.com/quote/{}?p={}".format(ticker, ticker) 

    r = requests.get(url)
    stock_content = BeautifulSoup(r.text, 'lxml')

    varYearTargetEst = stock_content.find_all('td', {'data-test':'ONE_YEAR_TARGET_PRICE-value'})[0].find('span').text
    return varYearTargetEst

def currentValue(ticker):
    try:
        #url = 'https://finance.yahoo.com/quote/SY?p=SY'
        url = "https://finance.yahoo.com/quote/{}?p={}".format(ticker, ticker)

        response = requests.get(url)
        stock_content = BeautifulSoup(response.text, 'lxml')
        stock_content = stock_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
        stock_content = stock_content.find('span').text

    except AttributeError as error:
        print("N/A 1", str(error).rstrip("\n"))
    except Exception as exception:
        print("N/A 2", str(exception).rstrip("\n"))
    finally:
        return stock_content


df = pd.read_excel('./health-bio-vol-over-1.2m-over-0.5d.xlsx')
# print(df['ticker'][0])
for x in range(100):
    # print(df['ticker'][x], currentValue(df['ticker'][x]))
    print(currentValue(df['ticker'][x]))
#  print(yearTargetEst(df['ticker'][x]))

