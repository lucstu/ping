import requests
import json
import urllib
import time
from bs4 import BeautifulSoup
from Discord import sendToDiscord

def BestBuyStock(item_id, mode):
    if mode == "upc":
        url = 'https://www.bestbuy.com/site/searchpage.jsp?st=' + item_id +'&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'

        head = {
            'user-agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
        }

        response = requests.get(url, headers=head)

        soup = BeautifulSoup(response.text, 'html.parser')
        item_exists = soup.find('button', {'class' : 'btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button'})

        if item_exists != None:
            item_link = soup.find('h4', {'class' : 'sku-header'})
            item_link = item_link.findChild("a", recursive=False)
            item_link = 'https://bestbuy.com' + item_link['href']
            sendToDiscord(item_id, item_link)

    elif mode == "keywords":
        url = 'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&sp=-displaydate%20skuidsaas&st=' + item_id + '&type=page&usc=All%20Categories'

        head = {
            'user-agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'
        }

        response = requests.get(url, headers=head)

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('h4', {'class' : 'sku-header'})

        for link in links:
            child = link.findChild("a", recursive=False)
            keywords = item_id.split('+') # splits keywords into array

            # checks to see if all keywords are in product name (casefold gets rid of case)
            if all(kw in child.contents[0].casefold() for kw in keywords):
                sendToDiscord(child.contents[0], 'https://bestbuy.com' + child['href'])

        return False # This part of the script should constantly be running as it needs to search for new results consistently.