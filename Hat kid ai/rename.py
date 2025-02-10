from os import listdir,rename

path = "Sounds"

try:
    listdir(path)
except:
    path = "Hat kid ai/"+path

for x in listdir(path):
    rename(f"{path}/{x}",f"{path}/{x.replace('VA_Hatkid_','')}")