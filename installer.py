import os
import json
import requests
import shutil

shutil.rmtree("cache")

mc_folder = os.path.expanduser("~\\AppData\\Roaming\\.minecraft")
mod_file = "https://raw.githubusercontent.com/RoseyKat/mc-mods/main/mods/mods.zip"

with open("data/config.json", "r") as f:
    data = json.loads(f.read())

    essentials = data["essential"]
    mod_type = data["mod_type"]
    version = data["version"]
    rm_old = data["rm_old"]

if essentials:
    path = f"{mc_folder}\\essential_mod\\fabric\\{version}\\{version} Fabric Essential\\mods"
else:
    path = f"{mc_folder}\\mods"

if rm_old:
    shutil.rmtree(path)
    os.makedirs(path)

downloaded_file = requests.get(mod_file)
os.makedirs("cache", exist_ok=True)
with open("cache/mods.zip", "wb") as f:
    f.write(downloaded_file.content)

shutil.unpack_archive("cache/mods.zip", path)

input(f"Downloaded mods to: '{path}'\npress enter to exit.....")
shutil.rmtree("cache")
exit()