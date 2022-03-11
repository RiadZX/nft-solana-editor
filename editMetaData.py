import os
import json
from natsort import natsorted

path = natsorted(os.listdir("./metadata"))
imagePath = natsorted(os.listdir("./images"))
startFrom = int(input("What should the starting number be?)\n"))
print(startFrom)
i = startFrom

def updateJsonFile(filename):
    global i
    jsonFile = open(filename, "r+") # Open the JSON file for reading
    
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file
    os.rename(filename, r"./metadata/{}.json".format(i))
    
    #edit the info here
    name = "Name #{}".format(i)
    image = "{}.png".format(i)
    description = "peepeepoopoo"
    properties = [{'uri': '{}.png'.format(i),"type" : "image/png"}]
    symbol = "$chungus"
    seller_fee_basis_points = 600
    external_url = "https://www.riaddev.tech/"
    collection = { "name": "chungus", "family": "rabbit" }
    creators = [
      {
        "address": "A5sPLXifFmjKAdoC7rLbhUD6vNgAUfuiDKebgecm1WX2",
        "share": 100
      }
    ]

    data["name"] = name
    data["image"] = image
    data["description"] = description
    data["properties"]["files"] = properties
    data["symbol"] = symbol
    data["seller_fee_basis_points"] = seller_fee_basis_points
    data["properties"]["creators"] = creators
    data["external_url"] = external_url
    data["collection"] = collection

    
    #this deletes the rarity rank, delete it if you want to keep the rarity rank from launchmynft 
    attributes = data["attributes"];
    if(attributes[-1]["trait_type"] == "Rarity Rank"):
        del attributes[-1]
    ##delete till here if you dont need it
    
    # Save our changes to JSON file
    jsonFile = open(r"./metadata/{}.json".format(i), "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
    i+=1
    print(f"SUCCESS | {name}  |{image} |\n")

def updateImageFile(filename):
    global i
    os.rename(filename,r"./images/{}.png".format(i))
    i+=1

for file in path:
    updateJsonFile(r"./metadata/{}".format(file))

i = startFrom

for file in imagePath:
    updateImageFile(r"./images/{}".format(file))



    
