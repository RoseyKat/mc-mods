import os
import json

with open("data/mods.json", "w") as f:
    data = {"mods": []}
    f.write("")

mods = os.listdir("mods")

for i in mods:
    data["mods"].insert(-1, i)

with open("data/mods.json", "w") as f:
    f.write(json.dumps(data))