import requests
import json
import urllib
from bs4 import BeautifulSoup
from Discord import sendToDiscord

def NeweggStock(item_id, mode):
    if mode == "pid":
        url = "https://www.newegg.com/LandingPage/ItemInfo4ProductDetail2016.aspx"
        querystring = {"Item":item_id}
        response = requests.request("GET", url, params=querystring)

        # Splits text to grab the json for the item.
        text = response.text
        text = text.split("rawItemInfo=")
        text = text[1]
        text = text.split(';')
        text = text[0]

        j = json.loads(text) # gets json for info.

        if j['mainItem']['instock'] == True: # if item in stock.
            product_url = 'https://newegg.com/p/' + j['mainItem']['neweggItemNumber']
            sendToDiscord(item_id, product_url)
            return True
        else:
            return False
    elif mode == "keywords":
        url = "https://www.newegg.com/p/pl"
        querystring = {"d":item_id}
        response = requests.get(url, params=querystring)
        soup = BeautifulSoup(response.text, 'html.parser')

        # looks for product does not exist error class.
        span = soup.find('span', {'class' : 'result-message-error'})

        if span == None: # If there is no product does not exist error
            url = soup.find('a', {'title' : 'View Details'})
            sendToDiscord(item_id, url['href'])
            return True
        else:
            return False

        
    