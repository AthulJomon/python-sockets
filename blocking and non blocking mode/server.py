import socket
from datetime import datetime

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),4571))
    s.listen(5)

    print('Server is up. Listening for connections..')

    client,address=s.accept()
    
    start_time=datetime.now()
    
    data=client.recv(1024)
    total_recv_size=len(data)
    i=1
    
    while data:
        print(data.decode('utf-8'))
        data=client.recv(1024)
        total_recv_size+=len(data)
        i+=1
    
    print('All data received in %i batches' %i)
    client.close()

end_time=datetime.now()
print('Duration:',end_time - start_time)
print('Total size of received files: %i' %total_recv_size)
