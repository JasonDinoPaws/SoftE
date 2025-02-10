import google.generativeai as genai
from PlaySound import GetAvaliableSounds,Playsound
import string



genai.configure(api_key="AIzaSyAU021QhVx8dX5_qJ9cELnFp1uQ_fH1AZE")
model = genai.GenerativeModel('gemini-1.5-flash')

Allowed = ""

for x in GetAvaliableSounds():
    Allowed += x+","
Allowed = Allowed[:-1]

def GetGenResponce():
    return model.generate_content(f"Create a sentence only using [{Allowed}] without modifying the way the word is spelt.").text


responce =  GetGenResponce()

print("Generated responce, Removing Punctuation")
print(len(responce))
responce = ''.join([x for x in responce if x == "_" or x not in string.punctuation])
for w in responce.split(" "):
    Playsound(w.strip())

print("\n\n"+responce)