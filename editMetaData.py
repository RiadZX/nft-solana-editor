import os
import json
from natsort import natsorted

path = natsorted(os.listdir("./metadata"))
imagePath = natsorted(os.listdir("./images"))
startFrom = int(input("What should the starting number be?\n"))
i = startFrom
def updateJsonFile(filename):
    global i
    jsonFile = open(filename, "r+") # Open the JSON file for reading
    
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file
    os.rename(filename, r"./metadata/{}.json".format(i))
    
    #name of a single nft with the number added
    data["name"] = "Name #{}".format(i)
    #ignore this
    data["image"] = "{}.png".format(i)
    #description
    data["description"] = "Description."
    #ignore this
    data["properties"]["files"] = [{'uri': '{}.png'.format(i),"type" : "image/png"}]
    #symbol
    data["symbol"] = "Symbol"
    #6%
    data["seller_fee_basis_points"] = 600
    #change the wallets here
    data["properties"]["creators"] = [
      {
        "address": "51fGJfr3zjhMiGOPILN1jG2kJXpsdDqdvxP4YHRpEh7",
        "share": 80
      },
      {
        "address": "51fGJfr3zjhMiGkZLbqN1jG2kJXpsdDqdvxP4YHRpEh7",
        "share": 20
      }
    ]
    #external website
    data["external_url"] = "https://www.riaddev.tech/"

    #collection name and family
    data["collection"] = { "name": "RiadDev'", "family": "RiadDev Family" }

    
    #this deletes the rarity rank
    attributes = data["attributes"];
    if(attributes[-1]["trait_type"] == "Rarity Rank"):
        del attributes[-1]

    
    # Save our changes to JSON file
    jsonFile = open(r"./metadata/{}.json".format(i), "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
    i+=1

def updateImageFile(filename):
    global i
    
    os.rename(filename,r"./images/{}.png".format(i))
    
    i+=1

for file in path:
    updateJsonFile(r"./metadata/{}".format(file))
    #print(r"./metadata/{}".format(file))

i = startFrom

for file in imagePath:
    updateImageFile(r"./images/{}".format(file))
    #print(file)


    
