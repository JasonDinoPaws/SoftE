import socket, pickle
from sys import exit

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("10.0.12.2", 8888))
        pass

    def SendMessage(self,Messsage:str):
        self.socket.send(Messsage)

    def SendArray(self,arrayType:str, array:list):
        self.socket.send(arrayType.encode())
        self.socket.sendall(pickle.dumps(array))

    def GetArray(self):
        data = self.socket.recv(4096)

        if not data:
            self.socket.close()
            exit("Server Died")
            return "Dead"
        
        return repr(pickle.loads(data))
