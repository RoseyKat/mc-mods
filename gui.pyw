import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilenames
import os
import shutil
import installer
import json
import sys

os.makedirs("cache", exist_ok=True)

root = tk.Tk()

def get_mods():
    files = askopenfilenames(filetypes=[('Mods', '*.jar'), ('Mods', '*.zip')])

    if files != '':
        with open("cache/mods.json", "w") as f:
            f.write(json.dumps(files))

def install():
    with open("config.json", "r") as f:
        config = json.loads(f.read())

    print(gui.essential_selector.state())

    if "selected" in gui.essential_selector.state():
        essential = True
    else:
        essential = False

    config["loader"] = gui.loader_selector.get()
    config["version"] = gui.version_selector.get()
    config["essential"] = essential
    config["install_location"] = installer.find_best_loc(gui.version_selector.get(), essential, gui.loader_selector.get())

    with open("config.json", "w") as f:
        f.write(json.dumps(config, indent=4))

    install = installer.install_mods()
    if install == 1:
        gui.final_frame.place(relx=0, rely=0, relheight=1, relwidth=1, anchor="nw")
        gui.frame.place_forget()

class gui:
    frame = tk.Frame(root, relief="ridge", bd=5)

    header = tk.Label(frame, text="Mod Installer", font="Arial 24")

    version_selector_label = tk.Label(frame, text="Version")
    version_selector = ttk.Combobox(frame, values=installer.get_current_versions())

    loader_selector_label = tk.Label(frame, text="Loader")
    loader_selector = ttk.Combobox(frame, values=["Fabric", "Forge"])

    essential_selector = ttk.Checkbutton(frame, text="Using essential mod?")

    mods_selector = tk.Button(frame, text="Select Mods", command=get_mods)

    install_button = tk.Button(frame, text="Install!", command=install)


    frame.place(relx=0, rely=0, relheight=1, relwidth=1, anchor="nw")

    header.place(relx=0.5, rely=0.15, anchor="center")

    version_selector_label.place(relx=0.35, rely=0.45, anchor="center")
    version_selector.place(relx=0.35, rely=0.5, relheight=0.05, relwidth=0.2, anchor="center")

    loader_selector_label.place(relx=0.65, rely=0.45, anchor="center")
    loader_selector.place(relx=0.65, rely=0.5, relheight=0.05, relwidth=0.2, anchor="center")

    essential_selector.place(relx=0.5, rely=0.6, anchor="center")

    mods_selector.place(relx=0.5, rely=0.7, relheight=0.1, relwidth=0.2, anchor="center")

    install_button.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.2, anchor="center")



    final_frame = tk.Frame(root)

    complete_label = tk.Label(final_frame, text="All mods installed!", font="Arial 24")

    exit_btn = tk.Button(final_frame, text="Exit", command=sys.exit)

    complete_label.place(relx=0.5, rely=0.25, anchor="center")

    exit_btn.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.2, anchor="center")

root.title("Mod Installer")
root.geometry("512x512")
root.mainloop()