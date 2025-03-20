with open(f"{''.join(x+'/' for x in __file__.split('/')[:-1])}fox.txt") as file:
    text = []
    fplace = []
    for x in file.readlines():
        x = x.strip().split(",")
        for a in range(len(x)):
            if x[a] == "F":
                fplace.append((len(text),a))
        text.append(x)

foxcount = 0

def checkline(r,c,rs,cs,wlen):
    word = ""
    for x in range(wlen):
        rp = r+(rs*x)
        cp = c+(cs*x)
        if rp > -1 and rp < len(text) and cp > -1 and cp < len(text[0]):
            word += text[rp][cp]
        else:
            return "Failed"
    
    return word

for sr,sc in fplace:
    for w in [checkline(sr,sc,0,1,3),checkline(sr,sc,1,0,3),checkline(sr,sc,0,-1,3),checkline(sr,sc,-1,0,3)]:
        if w == "FOX":
            foxcount += 1

print(foxcount)