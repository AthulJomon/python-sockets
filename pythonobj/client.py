import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(),4582))
    while True:
        msg=s.recv(1024)

        if not msg:
            print('No messages from server. Closing connection..')
            break

        Product_obj=pickle.loads(msg)

        print('Product ID:',Product_obj.pid)
        print('Product name:',Product_obj.pname)
        print('Product price:',Product_obj.pprice)