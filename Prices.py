import requests
from bs4 import BeautifulSoup


class Prices:

    @staticmethod
    def alphabet_price():
        response = requests.get('https://finance.yahoo.com/quote/GOOG/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text

        return price

    @staticmethod
    def apple_price():
        response = requests.get('https://finance.yahoo.com/quote/AAPL/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text

        return price

    @staticmethod
    def amazon_price():
        response = requests.get('https://finance.yahoo.com/quote/AMZN/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def bitcoin_price():
        response = requests.get('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def bp_price():
        response = requests.get('https://finance.yahoo.com/quote/BP/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def eurusd_price():
        response = requests.get('https://finance.yahoo.com/quote/EURUSD=X?p=EURUSD=X')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def fb_price():
        response = requests.get('https://finance.yahoo.com/quote/FB/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def gbpusd_price():
        response = requests.get('https://finance.yahoo.com/quote/GBPUSD=X?p=GBPUSD=X')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def gold_price():
        response = requests.get('https://finance.yahoo.com/quote/GC=F?p=GC=F')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def oil_price():
        response = requests.get('https://finance.yahoo.com/quote/CL=F?p=CL=F')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def ms_price():
        response = requests.get('https://finance.yahoo.com/quote/MSFT/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price

    @staticmethod
    def tesla_price():
        response = requests.get('https://finance.yahoo.com/quote/TSLA/')
        soup = BeautifulSoup(response.text, 'lxml')

        price = soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
        return price
