import requests
import json

def sendToDiscord(item, url):
    data = {
        "embeds": [
            {
                "color": 53380,
                "fields": [
                    {
                    "name": "Restock",
                    "value": item,
                    },
                    {
                    "name": "Product Link",
                    "value": url,
                    }
                ]
            }
        ]
    }
    

    webhook = 'INSERT WEBHOOK HERE'

    result = requests.post(webhook, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Discord webhook successfully sent for product id: {}.".format(item))
