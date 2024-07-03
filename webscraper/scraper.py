import requests
from bs4 import BeautifulSoup

def exchange():
    r = requests.get('https://www.x-rates.com/table/?from=USD&amount=1#google_vignette')
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', id='content')
    lines = s.find_all('tr')
    temp = []
    for line in lines:
        temp.append(line.text)

    newArr = temp[12:]

    char = "\n"
    
    for i, j in enumerate(newArr):
        newArr[i] = j.replace(char, " ")
    return newArr