import network
from wlan import do_connect
import socket
from machine import Pin

led=Pin(0,Pin.OUT) #define GPIO 0 as OUTPUT

def webpage(message):
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
                    <p>Response from Server is "Hello" and receive from client is {message }</p>
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
        html=webpage(message)
        client.send(html)
        client.close()
try:
    ip=do_connect()
    print('Ip address is:',ip)
    connection=open_socket(ip)
    serve(connection)
    
except KeyboardInterrupt:
    pass
