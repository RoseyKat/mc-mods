import os
import json
import shutil

def install_mods():
    with open("config.json", "r") as f:
        config = json.loads(f.read())

    if config["install_location"] == "Too many essential installations!":
        print("Too many essential installations!")
        exit()
    
    elif config["install_location"] == "No essential installations!":
        print("No essential installations!")
        exit()

    with open("cache/mods.json", "r") as f:
        mods = json.loads(f.read())

    for i in mods:
        if str(i).endswith(".zip"):
            shutil.unpack_archive(i, "cache")

            for j in os.listdir("cache"):
                if str(j).endswith(".jar"):
                    shutil.copy(f"cache/{j}", f"{config["install_location"]}/{os.path.split(j)[1]}")
                    os.remove(f"cache/{j}")

        elif str(i).endswith(".jar"):
            shutil.copy(i, f"{config["install_location"]}/{os.path.split(i)[1]}")
        
        print(f"Installed: {i}")

    print("Done")
    shutil.rmtree("cache")
    return 1

def find_best_loc(version:str, essential:bool, loader:str):
    if essential:
        ongoing_path = os.path.expanduser(f"~/AppData/Roaming/.minecraft/essential_mod/{loader}/{version}")

        essential_installations = os.listdir(ongoing_path)
        count = 0
        for i in essential_installations:
            count = count + 1
        
        if count == 1:
            return ongoing_path + f"/{essential_installations[0]}/mods"

        elif count >= 2:
            return "Too many essential installations!"
        
        else:
            return "No essential installations!"

    else:
        return os.path.expanduser(f"~/AppData/Roaming/.minecraft/mods")
    
def get_current_versions():
    version_manifest = os.path.expanduser("~/AppData/Roaming/.minecraft/versions/version_manifest_v2.json")

    with open(version_manifest, "r") as f:
        data = json.loads(f.read())["versions"]

    with open("config.json", "r") as f:
        config = json.loads(f.read())

    version_list = []
    for i in data:
        version_id = i["id"]
        version_type = i["type"]

        if version_type == "release":
            version_list.insert(-1, str(version_id))

    config["versions"] = version_list

    with open("config.json", "w") as f:
        f.write(json.dumps(config, indent=4))

    return version_list