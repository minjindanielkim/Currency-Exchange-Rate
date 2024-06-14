import requests
from bs4 import BeautifulSoup

def exchange():
    r = requests.get('https://www.x-rates.com/table/?from=USD&amount=1#google_vignette')
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', id='content')
    lines = s.find_all('tr')
    count = 1
    arr = []
    for line in lines:
        if count == 12:
            break
        count += 1
        arr.append(line.text)

    arr.pop(0)

    char = "\n"
    
    for i, j in enumerate(arr):
        arr[i] = j.replace(char, " ")
    
    return arr