from Socket import Server
from Menu import *

Ser = Server()
cmds = {
    "/Additem": "Adds a item to the menu",
    "/Removeitem": "Removes a item to the menu",
    "/Edititem": "Edits a item to the menu",
    "/Menu": "Prints the menu",

    "/List": "Lists the clients that are connected",
    "/Kill": "Removes a client that is connected",
}


while True:
    print("Command - Description")
    for x in cmds.keys():
        print(f"{x} - {cmds[x]}")
    print()
    command = input("Command: ").lower()

    if command[0] == "/":
        if command[1:] == "menu":
            print()
            for p,i,t,d in GetMenuSections():
                print(x)