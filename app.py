import requests
from PIL import Image
print("Pokemon Character Generator\n")

user_input = input("Enter character Name: \n")
user_input = user_input.lower()

if user_input:
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input}")
    if req.status_code == 200:
        data = req.json()
        type_one = data["types"]
        for dtype in type_one:
            print(f"Results for {user_input}")
            print("Slot :",dtype["slot"])            
            print("Type :",dtype["type"]["name"])
            print("URL :",dtype['type']['url'])
    else:
        print("Invalid Character Choice\n")
    
else:
    print("No Character name was Provided\n")
