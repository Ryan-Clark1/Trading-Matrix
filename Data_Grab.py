
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

Ticker = ''

link = ("https://www.cnbc.com/quotes/?symbol=" + Ticker + "&qsearchterm=" + Ticker)
html = requests.get(link).content
soup = BeautifulSoup(html, 'html.parser')
soup.prettify()
e = str(soup)


#  Banner tape snippet  #
f = e.index('"fullchange_pct"')
g = f+500
snap = e[f:g]

def makingsoup(Ticker):
    link = ("https://www.cnbc.com/quotes/?symbol=" + Ticker + "&qsearchterm=" + Ticker)
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    e = str(soup)
    return e


def burn_rate(Ticker):
    link = "https://finance.yahoo.com/quote/"+Ticker+"?p="+Ticker+"&.tsrc=fin-srch"
    driver = webdriver.Safari()
    driver.get(link)
    time.sleep(5)
    #cash = driver.find_elements("x")
    br = 1
    return br

def eps():
    f = e.index("eps")
    x = 20
    g = f + x
    snip = e[f:g]
    end = snip.index('",')
    start = snip.index(':"')
    start = start + 2
    eps = snip[start:end]
    return eps


def pe():
    f = e.index("eps")
    x = 500
    g = f + x
    snip = e[f:g]
    start = snip.index('"pe"')
    end = start + 14
    start = start + 6
    pe = snip[start:end]
    return pe

def volume():
    f = e.index("tendayavgvol")
    x = 40
    g = f + x
    snip = e[f:g]
    start = snip.index('":"') + 3
    end = snip.index('","')
    volume = snip[start:end]
    return volume

def market_cap():
    f = e.index("mktcap")
    x = 50
    g = f + x
    snip = e[f:g]
    start = snip.index('":"') + 3
    end = snip.index('","')
    market_cap = snip[start:end]
    return market_cap

def company_name():
    f = e.index('"name"')
    x = 50
    g = f + x
    snip = e[f:g]
    start = snip.index('">') + 2
    end = snip.index(' - Stock')
    companyname = snip[start:end]
    return companyname

def percent_daily():
    f = e.index('"name"')
    x = 1750
    g = f + x
    snip = e[f:g]
    snip = snip.split('"')
    indentifier = snip.index("change_pct")
    pct_change = snip[indentifier + 2]
    return pct_change

def recent_price():
    f = e.index('"name"')
    x = 1750
    g = f + x
    snip = e[f:g]
    snip = snip.split('"')
    indentifier = snip.index("last")
    banner_price = snip[indentifier + 2]
    return banner_price

def recent_price_time():
    f = e.index('"name"')
    x = 1750
    g = f + x
    snip = e[f:g]
    snip = snip.split('"')
    indentifier = snip.index("last_time")
    last_updated = snip[indentifier + 2]
    start = last_updated.index("T") + 1
    end = start + 8
    last_updated = last_updated[start:end]
    return last_updated

def daily_change():
    f = e.index('"name"')
    x = 1750
    g = f + x
    snip = e[f:g]
    snip = snip.split('"')
    indentifier = snip.index("change")
    day_change = snip[indentifier + 2]
    return day_change

def earnings_date():
    f = e.index('"name"')
    x = 1750
    g = f + x
    snip = e[f:g]
    snip = snip.split('"')
    indentifier = snip.index("next_earnings_date")
    day_change = snip[indentifier + 2]
    return day_change



f = e.index('is_halted')
x = 1750
g = f + x
snip = e[f:g]
f = e.index('high')
g = e.index("providerSymbol")
snap = e[f:g]
snap = snap.split('"')
#print(snap)

def year_low_price():
    f = e.index('yrloprice')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    yrloprice = e[x:z]
    return yrloprice
def year_price_change():
    f = e.index('yragopricechange')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    yragopricechange = e[x:z]
    return yragopricechange
def revenue_ttm():
    f = e.index('revenuettm')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    revenuettm = e[x:z]
    return revenuettm
def net_profit_ttm():
    f = e.index('NETPROFTTM')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    NETPROFTTM = e[x:z]
    return NETPROFTTM
def ten_day_avg_volume():
    f = e.index('tendayavgvol')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    tendayavgvol = e[x:z]
    return tendayavgvol
def price_today_close():
    f = e.index('todays_closing')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    todays_closing = e[x:z]
    return todays_closing
def price_prev_prev_close():
    f = e.index('prev_prev_closing')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    prev_prev_closing = e[x:z]
    return prev_prev_closing
def price_hoy():
    f = e.index('yrhiprice')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    yrhiprice = e[x:z]
    return yrhiprice
def hoy_date():
    f = e.index('yrhidate')
    x = e[f:].index('":"') + f + 3
    z = e[x+1:].index('","') + x
    yrhidate = e[x:z]
    return yrhidate


z = snap.count('","')
i = 0




