def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('Rout2g','Rout@4321')
        print('....')
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
    print('connected to network',wlan.ifconfig()[0])
