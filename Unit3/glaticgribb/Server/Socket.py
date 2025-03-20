import socket, pickle
from Menu import GetMenu
from threading import Thread

class Server:
    def __init__(self):
        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Sock.bind(("localhost",8888))
        self.Sock.listen(1)

        self.receipts = []
        self.Clients = []
        Thread(target=self.Listen).start()
        pass

    def Listen(self):
        while True:
            cli, addr = self.Sock.accept()
            self.Clients.append((cli,addr))
            Thread(target=self.Client,args=(cli,addr,)).start()

    def Connected(self,cli,add):
        print(f"Client connected from {add}")
        while True:
            data = cli.recv(4096)
            if not data:
                break
            decode = data.decode()

            if decode == "m":
                cli.sendall(pickle.dumps(GetMenu()))
            elif decode == "t":
                redata = cli.recv(4096)
                receipt = repr(pickle.load(redata))
                self.receipts.append(receipt)

