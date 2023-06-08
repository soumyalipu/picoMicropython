import network
from wlan import do_connect
import socket

def webpage(message):
    html=f"""
            <!DOCTYPE html>
            <html>
                <body>
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