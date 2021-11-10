import logging
import threading
import time
import sys
import signal
import http.client as hc
import random
import argparse

httpHost    = "localhost:8000";
httpMethod  = "GET";
url         = "/?clientId={}"

run = True

def signal_handler(signum, frame):
    global run
    run = False

def thread_function(client, w):
    while(run):
        hcon = hc.HTTPConnection(httpHost)
        hcon.request(httpMethod, url.format(client))
        response = hcon.getresponse()
        html = response.read()        
        status = response.getcode()
        logging.info(status)
        logging.info(html)
        rnd_sleep = random.normalvariate(2.0, 0.5)
        time.sleep(rnd_sleep)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description='Simulate DoS attack! Ctrl-C to quit.')
    parser.add_argument('clients', type=int,
                        help='Number of clients')
    parser.add_argument('workers', type=int, 
                        help='Number of workers per client')

    args = parser.parse_args()
    num_clients = int(args.clients)
    num_workers = int(args.workers)
    threads = []

    for client in range(num_clients):
        for worker in range(num_workers):
            threads.append({"thread" : threading.Thread(target=thread_function, args=(client, worker)),
                            "client" : client, 
                            "worker" : worker })
    
    for t in threads:
        t["thread"].start()
    
    while run:
        signal.pause()

    for t in threads:
        logging.info("Joining client {} worker {}".format(t["client"], t["worker"]))
        t["thread"].join()
	
    logging.info("All cleaned up")

