csvpath = "".join(x+"/" for x in __file__.split("/")[:-1])+"Menu.csv"

items = []
itempos = ["price","name","type","description"]


def SaveMenu():
    with open(csvpath,"w") as csv:
        for p,i,t,d in items:
            line = f"{p},{i},{t},\"{d}\"\n"
            csv.write(line)

def GetItemPos(name:str):
    for x in range(len(items)):
        if items[x][1] == name:
            return x
    return -1

def AddItem(price:float,name:str,type:str,description:str):
    if GetItemPos(name) == -1:
        items.append([int(price),name,type,description])
        print(f"added {name}")
    else:
        print(f"Can't add {name}, already in system")

def RemoveItem(name:str):
    pos = GetItemPos(name)
    if pos != -1:
        items.pop(pos)
        print(f"removed {name}")
    else:
        print(f"{name} not in menu")
    
def EditItem(name:str,props:dict):
    pos = GetItemPos(name)
    if pos != -1:
        for p in props.keys():
            if p in itempos:
                items[pos][itempos.index(p)] = props[p]
                print(f"Edited {name}")
    else:
        print(f"{name} not in menu")
    
def GetMenu():
    return items

def GetMenuSections():
    Menu = {}
    for p,i,t,d in items:
        if t in Menu:
            Menu[t] = []

        Menu[t].append((p,i,d))
    return Menu

with open(csvpath,"r") as csv:
    for x in csv.readlines()[1:]:
        s = x.strip().split(",")
        AddItem(float(s[0]),s[1],s[2],s[3])