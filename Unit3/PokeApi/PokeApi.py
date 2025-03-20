import requests
import cv2
import numpy as np

Stats = {}
imgpix = np.zeros((96,96,4))
img = []
Color = [0,1,2]
path = "".join(x+"/" for x in __file__.split("/")[:-1])

def GetPath(name):
    return path+"/"+name

# Creates the image from a array for each pixel mulitplyed by the size and given a color based off of the variables
def CreateImage():
    global imgpix,img
    if type(img) == type(None):
        return
    
    imgpixs = []
    for r in range(len(img)):
        row = []
        for c in range(len(img[r])):
            color = (img[r,c,Color[0]],img[r,c,Color[1]],img[r,c,Color[2]])
            row.append(color)
        imgpixs.append(row)

    imgpix = np.array(imgpixs)
    cv2.imwrite(GetPath("pokemon_image.png"),imgpix)
    

# checks if the link is valid for the iamge
def GetImage(link):
    if link:
        img = requests.get(link)
        if img.status_code == 200:
            img = np.asarray(bytearray(img.content), dtype="uint8")
            return cv2.imdecode(img, cv2.IMREAD_COLOR)
    return

# Calulates the height of the pokemon in feet
def CaltHeight(dm:int):
    cm = dm * 10
    inches = cm / 2.54
    feet = inches // 12
    inches = inches % 12
    return f"{int(feet)}' {round(inches)}\""

# Checks if the number given is valid and sets its image and stats
def GetPokemonInfo(number):
    global Stats,img
    page = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}",json=True)

    if page.status_code == 200:
        Stats = page.json()
        img = GetImage(Stats["sprites"]["front_default"])
        CreateImage()

        Stats["height"] = CaltHeight(Stats['height'])

        return True
    return False
# If a entry is unfocused a and trys to set it to a value
# def Out(en,x=""):
#     global images
#     if x == "":
#         data = en.widget.get()
#         for x,ent in Entrys:
#             if ent == en.widget:
#                 break
#         else:
#             return
#     else:
#         data = en.get()

#     if x in ["R","G","B"] and data.isdigit():
#         if int(data) >= 0 and int(data) < 3:
#             Left[x] = int(data)
#     elif x == "Size" and data.isdigit():
#         Left[x] = int(data)

#     elif x == "Name/Number":
#         page = requests.get(f"https://pokeapi.co/api/v2/pokemon/{data}",json=True)

#         if page.status_code == 200:
#             js = page.json()

#             images = [
#                 GetImage(js["sprites"]["front_default"]),
#                 GetImage(js["sprites"]["back_default"]),
#                 GetImage(js["sprites"]["front_female"]),
#                 GetImage(js["sprites"]["back_female"]),


#                 GetImage(js["sprites"]["front_shiny"]),
#                 GetImage(js["sprites"]["back_shiny"]),
#                 GetImage(js["sprites"]["front_shiny_female"]),
#                 GetImage(js["sprites"]["back_shiny_female"]),
#             ]

#             for x in range(len(Stats)):
#                 if Stats[x][0] in js:
#                     Stats[x][2] = js[Stats[x][0]]


#     CreateImage(images[0])
#     for n,l,i in Stats:
#         l.config(text=f"{i}: {n}")
#         l.place(x=root.winfo_width()-l.winfo_width()-5)


# root.bind_class("Entry", "<FocusOut>", Out)

# # Places and loads in all items like the canvas and the Entrys
# yp = 5
# for tab in Stats:
#     lab = Label(root,text=f"Waitting to load",bg="white",highlightthickness=0,font=("Arial",15,"bold"),anchor="e")
#     tab.append(lab)
#     tab.append("Waitting")
#     # lab.pack(side="top")
#     lab.place(x=root.winfo_width()-5,y=yp)
#     yp += 30

# yp = 5
# for N in Left.keys():
#     ent =  Entry(root)
#     Label(root,text=N).place(x=5,y=yp)
#     ent.insert(0,Left[N])
#     ent.place(x=5,y=yp+20)
#     Entrys.append([N,ent])
#     Out(ent,N)
#     yp += 50

# can.pack()

# # system("amixer -D pulse set Master 25%")
# # Playsound("Pokemon.ogg",loop=5)

# root.mainloop()