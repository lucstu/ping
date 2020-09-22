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
    

    webhook = 'https://discordapp.com/api/webhooks/720758771093340171/-bqA33nsV9FbpRMq5jVcLUP5TXQfxxHCojcjnvervDLMu2-tiHgCmeVxR0Z_dAYbW_qc'

    result = requests.post(webhook, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Discord webhook successfully sent for product id: {}.".format(item))