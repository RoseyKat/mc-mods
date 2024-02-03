import shutil
import os

input_valid = False

while input_valid == False:
    user_input = input("Install mod installer? (y/n)>")

    if user_input.lower() == "y":
        start_menu = os.path.expanduser("~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs")
        os.mkdir(f"{start_menu}/Mod Installer")

        mod_folder = f"{start_menu}/Mod Installer"

        shutil.unpack_archive("mod_installer.zip", mod_folder)

        input("Done! Press enter to exit....")
        exit()

    elif user_input.lower() == "n":
        exit()

    else:
        os.system("cls")
        print(f"{user_input} is not a valid input!")