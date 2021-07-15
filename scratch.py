import os
import tkinter as tk
from tkinter import font
from tkinter import *
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import pandas as pd
from datetime import date
import time
import ScrolledText
import numpy as np
from selenium import webdriver
import selenium as se
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import glob
import os

identifiers = ["eps", '"pe"', "tendayavgvol", "mktcap", '"name"', 'yrloprice', 'yragopricechange', 'revenuettm',
                   'NETPROFTTM', 'todays_closing', 'prev_prev_closing', 'yrhiprice', 'yrhidate']

test_set = []

with open("NASDAQ_dict.csv", "r") as r:
    for line in csv.reader(r):
        test_set.append(line)

with open("NASDAQ_dict.csv", 'r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}

for Ticker in mydict:
    link = ("https://www.cnbc.com/quotes/?symbol=" + Ticker + "&qsearchterm=" + Ticker)
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    e = str(soup)
    ## f = e.index(identifier) ##
    f = e.index("eps")
    x = e[f:].index('":"') + f + 3
    z = e[x:].index('","') + x
    ## identifier = e[x:z] ##
    eps = e[x:z]
    print(Ticker, eps)