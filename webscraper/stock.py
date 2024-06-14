import requests
from bs4 import BeautifulSoup

def indicies():

    r = requests.get("https://finance.yahoo.com/world-indices/")
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', id="list-res-table")
    lines = s.find_all('tr')
    arr = []

    for i in lines:
        arr.append(i.text)
    return arr