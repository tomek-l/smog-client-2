import requests
import json
import time
import logging

#from requests import ConnectionError
from pms7003.pms7003 import Pms7003Sensor, PmsSensorExcpetion

def mainloop():
    try:
        j['values'] = sensor.read()
    except PmsSensorExcpetion as e:
        logging.exception('{} {}'.format(int(1000*time.time()), e))

    j['timestamp'] = time.time()

    try:
        r=requests.post('https://smog-monitor.herokuapp.com/api/get-one', json=json.dumps(j), timeout=4)
        logging.info('{} {}'.format(int(1000*time.time()), r.status_code))
        if r.status_code != 200:
            time.sleep(1)
        del r

    except ConnectionError as e:
        logging.exception('{} {}'.format(int(1000*time.time()), e))

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')
    j = {}
    logging.basicConfig(filename='/home/pi/smog-client-2/smog.log', level='INFO')

    while True:
        mainloop()





        