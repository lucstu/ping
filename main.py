from Newegg import NeweggStock
from Amazon import AmazonStock
from BestBuy import BestBuyStock
from BandH import BandHStock
from MicroCenter import MicroCenterStock
from logging.config import fileConfig
import time
import random
import threading
import csv
import logging

def monitor(site, product_id, mode):
    if site == "Newegg":
        while NeweggStock(product_id, mode) != True:
            log.info(product_id + " out of stock/not loaded.")
            time.sleep(generateTime())
        log.info("{} restocked. Removing item from monitored items.".format(product_id))

    elif site == "BestBuy":
        while BestBuyStock(product_id, mode) != True:
            log.info(product_id + " out of stock/not loaded.")
            time.sleep(generateTime())
        log.info("{} restocked. Removing item from monitored items.".format(product_id))

    elif site == "MicroCenter":
        while MicroCenterStock(product_id, mode) != True:
            log.info(product_id + " out of stock/not loaded.")
            time.sleep(generateTime())
        log.info("{} restocked. Removing item from monitored items.".format(product_id))

    return 0

def generateTime():
    return random.randint(5,10)

def loadTasks():
    with open('tasks.csv', newline='') as csvfile:
        tasks = list(csv.reader(csvfile))
    
    return tasks

if __name__ == "__main__":
    fileConfig('logconfig.ini')
    log = logging.getLogger()
    log.info("Starting program")

    tasks = loadTasks()

    threads = list()
    for task in tasks:
        t = threading.Thread(target=monitor, args=(task[0], task[1], task[2]))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

