import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:

    s.bind((socket.gethostname(),4571))
    s.settimeout(10)
    try:
        s.listen(5)
        print("Server Running. Listening for connections..")

        client, address=s.accept()
        print("Connected to ",address,"\n")
        print("Client object ",client,"\n")
        client.send(bytes('Hello World','utf-8'))
    
    except socket.timeout:
        print('The timeout has been exceeded.Closing the connection..')
