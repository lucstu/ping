import requests
import json
import urllib
import time
from bs4 import BeautifulSoup
from Discord import sendToDiscord

def MicroCenterStock(item_id, mode):
    if mode == "upc":
        url = 'https://www.microcenter.com/search/search_results.aspx?Ntt=' + item_id + '&searchButton=search&storeid=151'

        head = {
            'user-agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
        }

        response = requests.get(url, headers=head)

        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find('a', {'id' : 'hypProductH2_0'})

        if link is not None:
            sendToDiscord(link.text, 'https://microcenter.com' + link['href'])

    elif mode == "keywords":
        url = 'https://www.microcenter.com/search/search_results.aspx?Ntt=' + item_id + '&searchButton=search&storeid=151'

        head = {
            'user-agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
        }

        response = requests.get(url, headers=head)

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', id=lambda x: x and x.startswith('hypProductH2'))

        for link in links:
            keywords = item_id.split('+') # splits keywords into array
            if all(kw in link.text.casefold() for kw in keywords):
                sendToDiscord(link.text, 'https://microcenter.com' + link['href'])