from rannumgen import GetRanNum
from millerrabin import is_prime
from extendedeuclidean import mod_inverse,extended_gcd


while True:
    # Getting P and Q primte numbers and make sureing that they do not equal each other
    p = 1
    q = 1
    while not is_prime(p): p = GetRanNum()
    while q != p and not is_prime(q): q = GetRanNum()

    # multiplying p and q to make n and on
    n = p*q
    on = (p-1)*(q-1)

    # asking the user for E and then finding which exponet mod n is 1
    e = int(input("Choose a number for E: "))

    r = 0
    while True:
        r += 1
        if (e**r) % n == 1:
            break
        
    # getting the mod inverse of e and on and setting it as d
    try:
        d = mod_inverse(e,on)
        break
    except:
        pass


# asking the user for the message
m = input("Message: ")

print("\n"*5)
# encryping each character of the message
c = []
for x in range(len(m)):
    c.append(ord(m[x])**e % n)

# decryping each character of the new encrypted message
m = []
for x in c:
    m.append(x**d % n)

# prints all of the variables that got saved
print(f"p value: {p}")
print(f"q value: {q}")
print(f"n value: {n}")
print(f"on value: {on}")
print(f"r value: {r}")
print(f"Public (e,n) = ({e},{n})")
print(f"Privte (d,n) = ({d},{n})")

print(f"Encrypted messge: {''.join(chr(x) for x in c)}\n{c}")
print(f"Decrypted messge: {''.join(chr(x) for x in m)}\n{m}")