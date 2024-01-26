import os
import json
import requests
import shutil
from time import sleep

shutil.rmtree("cache")

mc_folder = os.path.expanduser("~\\AppData\\Roaming\\.minecraft")

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

def download_mods():
    with open("data/mods.json", "r") as f:
        mods_list = json.loads(f.read())["mods"]

    for i in mods_list:
        sleep(0.2)
        file = requests.get(f"https://raw.githubusercontent.com/RoseyKat/mc-mods/main/mods/{i}")

        os.makedirs("cache", exist_ok=True)
        with open(f"cache/{i}", "wb") as f:
            f.write(file.content)

        print(f"Downloaded: '{i}'")

download_mods()

shutil.make_archive("mods", "zip", "cache")

shutil.unpack_archive("cache/mods.zip", path)

input(f"Downloaded mods to: '{path}'\npress enter to exit.....")
shutil.rmtree("cache")
exit()