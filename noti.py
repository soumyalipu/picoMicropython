import network
import time
import json
import urequests
from wlan import do_connect

do_connect()
apiKey = 'API' #reemplazar por la propia API KEY

url = "https://api.pushbullet.com/v2/pushes"
headers = {'Access-Token': apiKey, 'Content-Type': 'application/json'}

data = {'type':'note','body':'message','title':'state'}
dataJSON = json.dumps(data)

r = urequests.post(url, headers=headers,data=dataJSON)
print(r.json()['receiver_email'])