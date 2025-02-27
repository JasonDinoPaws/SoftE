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

# Connects to the Server(attacker)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((save["Add"],int(save["FP"])))

# makes it so that the client can send a message at any time
def Server():
    global active,server
    while active:
        text = input("")

        SendMessage(text,server,save["e"],save["n"])

Thread(target=Server).start()

try:
    while True:
        # checks if the server sent a message
        data = server.recv(save["data"]).decode()
        if not data:
            break

         # if the first message starts with a m gooes threw until it sees e tell the server the message has ended
        if data == "m":
            mes = []
            while True:
                let = server.recv(save["data"]).decode()
                if let == "e":
                    break
                else:
                    mes.append(let)
            # decrupts the message and checks it it says exit
            data = combine(decrypt(mes,save["d"],save["n"]))
            print(f"[Server]: {data}")
            if data == "exit":
                break

        else:
            # if the attacker sends a message
            print("There is a attack listenning, Stopping all operations")
            SendMessage("There is a attack listenning, Stopping all operations",server,save["e"],save["n"])
            SendMessage("exit",server,save["e"],save["n"])
            break
except:
    pass

# Closing
print("Closed")
server.close()
active = False
exit()