import urequests
import network
from wlan import do_connect

do_connect()

data=urequests.get('https://jsonplaceholder.typicode.com/todos/1')
print(data.json())