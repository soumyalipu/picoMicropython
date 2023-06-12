import network
from wlan import do_connect
import socket
from machine import Pin
import utime


from dht import DHT11, InvalidChecksum


led=Pin(1,Pin.OUT) #define GPIO 0 as OUTPUT
utime.sleep(1)

pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
def webpage(data):
    html=f"""
            <!DOCTYPE html>
            <html>
                <body>
                    <form action="./ledon">
                        <input type="submit" value="ledon" style="height:120px; width:120px" />
                    </form>
                    <form action="./ledoff">
                        <input type="submit" value="ledoff" style="height:120px; width:120px" />
                    </form>
                    <p>Response from Server is "Hello" and receive from client is {data}</p>
                </body>
            </html>
            """
    return html

def open_socket(ip):
    address=(ip,80)
    connection=socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    while True:
        client=connection.accept()[0]
        request=client.recv(1024)
        request=str(request)
        
        try:
            request=request.split()[1]
            print("request",request)
        except KeyboardInterrupt:
            pass
        message=request
        if message=='/ledon?':
            led.value(1)
        if message=='/ledoff?':
            led.value(0)
        dhtdata='T'+str(sensor.temperature)+' H'+str(sensor.humidity)
        print(dhtdata)
        utime.sleep(7)
        html=webpage(dhtdata)
        client.send(html)
        client.close()
try:
    ip=do_connect()
    print('Ip address is:',ip)
    connection=open_socket(ip)
    serve(connection)
    
except KeyboardInterrupt:
    pass

