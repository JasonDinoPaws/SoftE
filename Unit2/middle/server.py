import socket
from datetime import datetime
from threading import Thread
from RSA import *
from sys import exit

# Loading setting data to make it easyer
save = {}
path = "".join(x+"/" for x in __file__.split("/")[:-1])
active = True
with open(f"{path}/data.txt") as file:
    for x in file.readlines():
        x = x.strip().split(":",1)
        save[x[0]] = x[1].isdigit() and int(x[1]) or x[1]


# Sets up the server on the ip and the real port and waits for a client to connect
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((save["Add"],int(save["RP"])))
sock.listen(1)

cli, addr = sock.accept()
print(f"Client connected at {addr[0]}")

# Makes it so that the server can send any input to the client at any time
def Server():
    global active,cli
    while active:
        text = input("")
        SendMessage(text,cli,save["e"],save["n"])

Thread(target=Server).start()

try:
    while True:
        #Waits for a the client input and decrupts it
        data = cli.recv(save["data"]).decode()

        # it no input exit
        if not data:
            SendMessage("exit",cli,save["e"],save["n"])
            break

        # if the first message starts with a m gooes threw until it sees e tell the server the message has ended
        if data == "m":
            mes = []
            while True:
                let = cli.recv(save["data"]).decode()
                if let == "e":
                    break
                else:
                    mes.append(let)
            
            # decrupts the message and checks it it says exit
            data = combine(decrypt(mes,save["d"],save["n"]))
            print(f"[{datetime.now()}]: {data}")
            if data == "exit":
                break

        else: 
            # if the attacker sends a message
            print("There is a attack listenning, Stopping all operations")
            SendMessage("There is a attack listenning, Stopping all operations",cli,save["e"],save["n"])
            break
except Exception as e:
    print(e)

# Closing
print("Closed")
cli.close()   
active = False
exit()