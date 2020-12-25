import time
import requests
import schedule


def alphabet():
    alphabet_URL = 'https://cloud.iexapis.com/stable/stock/goog/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=alphabet_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(alphabet)
    while True:
        schedule.run_pending()
        time.sleep(1)


def apple():
    apple_URL = 'https://cloud.iexapis.com/stable/stock/aapl/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=apple_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(apple)

    while True:
        schedule.run_pending()
        time.sleep(1)


def amazon():
    amazon_URL = 'https://cloud.iexapis.com/stable/stock/amzn/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=amazon_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(amazon)

    while True:
        schedule.run_pending()
        time.sleep(1)


def J_and_J():
    bitcoin_URL = 'https://cloud.iexapis.com/stable/stock/JNJ/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=bitcoin_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(J_and_J)

    while True:
        schedule.run_pending()
        time.sleep(1)


def bp():
    bp_URL = 'https://cloud.iexapis.com/stable/stock/BP/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=bp_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(bp)

    while True:
        schedule.run_pending()
        time.sleep(1)


def Visa_Inc():
    Visa_URL = 'https://cloud.iexapis.com/stable/stock/V/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=Visa_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(Visa_Inc)

    while True:
        schedule.run_pending()
        time.sleep(1)


def fb():
    fb_URL = 'https://cloud.iexapis.com/stable/stock/FB/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=fb_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(fb)

    while True:
        schedule.run_pending()
        time.sleep(1)


def JPMorgan():
    gbpusd_URL = 'https://cloud.iexapis.com/stable/stock/JPM/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=gbpusd_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(JPMorgan)

    while True:
        schedule.run_pending()
        time.sleep(1)


def P_and_G():
    gold_URL = 'https://cloud.iexapis.com/stable/stock/PG/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=gold_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(P_and_G)

    while True:
        schedule.run_pending()
        time.sleep(1)


def NVIDIA():
    oil_URL = 'https://cloud.iexapis.com/stable/stock/NVDA/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=oil_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(NVIDIA)

    while True:
        schedule.run_pending()
        time.sleep(1)


def ms():
    ms_URL = 'https://cloud.iexapis.com/stable/stock/MSFT/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=ms_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(ms)

    while True:
        schedule.run_pending()
        time.sleep(1)


def tesla():
    tesla_URL = 'https://cloud.iexapis.com/stable/stock/TSLA/quote?token=sk_62c7728036de4d86b842b28f617246b6'
    r = requests.get(url=tesla_URL)
    data = r.json()
    return data['latestPrice']

    schedule.every(10).seconds.do(tesla)

    while True:
        schedule.run_pending()
        time.sleep(1)
