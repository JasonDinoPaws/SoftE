from time import sleep

# Encrypts the data in rsa
def encrypt(m,e,n):
    c = []
    for x in range(len(m)):
        c.append(str(ord(m[x])**e % n))
    return c

# Decrypts the data in rsa
def decrypt(c,d,n):
    m = []
    for x in c:
        m.append(int(x)**d % n)
    return m

# combines everything in the list to a string
def combine(a):
    return "".join(str(chr(x)) for x in a)

# Sends a message to a recever while it is encrypted 
def SendMessage(message,recever,e,n):
    recever.send("m".encode())
    for x in encrypt(message,e,n):
        recever.send(x.encode())
        sleep(.1)
    recever.send("e".encode())