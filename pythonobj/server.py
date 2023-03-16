import socket
from product import Product
import pickle
import time

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),4582))

    custom_objects=[Product('p024','Torch',8),
                    Product('p110','Scissors',5),
                    Product('p014','Cigarettes',10),
                    Product('p077','WaterBottle',10)]

    s.listen(5)
    print("Server is up. Listening for connections..")
    client, address=s.accept()
    print('Connected to',address,'successfully \n')
    print('Client object:',client,'\n')
    for product in custom_objects:
        pickeled_product=pickle.dumps(product)
        client.send(pickeled_product)

        print("Sent Product: ",product.pid)
        time.sleep(1)