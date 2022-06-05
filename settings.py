from logging import exception
from tkinter import Tk, Button, Toplevel, filedialog
from PIL import ImageTk, Image
from dark_title_bar import *

settings_file = "settings/settings.txt"


def set_up_window(theme):
    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
    global settings

    root = Toplevel()
    root.title("Settings")
    root.geometry("250x250")

    if theme == "light":
        print("Theme set to \"light\"")
        bg_color = "#f0f0f0"
        button_bg_color = "#c3c3c3"
        fg_color = "#000000"
        button_active_bg_color = button_bg_color
        button_active_foreground_color = fg_color
        label_bg_color = "#e4e4e4"
        frame_bg_color = bg_color
        highlightbackground_color = "#afafaf"
        settings_cog = ImageTk.PhotoImage(Image.open("images/settings_cog_light.png"))
        #virtualPixel is used to make the buttons completely resizable
        virtualPixel = ImageTk.PhotoImage(Image.open("images/virtualPixel_light.png"))

    if theme == "discord dark":
        print("Theme set to \"discord dark\"")
        try:
            dark_title_bar(root)
        except: print("Dark title bar is not supported by this computer")

        bg_color = "#36393f"
        button_bg_color = bg_color
        fg_color = "#d2d3d5"
        button_active_bg_color = button_bg_color
        button_active_foreground_color = fg_color
        label_bg_color = "#40444b"
        frame_bg_color = "#2f3136"
        highlightbackground_color = "#8a8a8a"
        settings_cog = ImageTk.PhotoImage(Image.open("images/settings_cog_discord_dark.png"))
        #virtualPixel is used to make the buttons completely resizable
        virtualPixel = ImageTk.PhotoImage(Image.open("images/virtualPixel_discord_dark.png"))

    root.configure(bg = bg_color)

    change_mods_folder_location_button = Button(root,
        text = "Change mods\nfolder location",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 135,
        height = 50,
        command = change_mods_folder_location)
    change_mods_folder_location_button.place(x = 54, y = 18)

    root.mainloop()


def get_user_settings():
    global settings
    #settings will contain every user setting and its value
    settings = {}

    try:
        for i in open(settings_file, "r"):
            #Split the line and save it in a key-value format in settings
            key_value = i.split(" = ")

            #If, by new line errors, various lines are together, raise an error and load the default settings
            if key_value.len() != 2:
                raise

            settings[key_value[0]] = key_value[1]
            
    except:
        get_default_settings()
        save_current_settings()

    return settings


def get_default_settings():
    global settings
    settings = {
        "mods_folder":"C:/Users/sergi/AppData/Roaming/.minecraft/mods",  #TODO: Make this user independent
        "theme":"light"
    }
    
    return settings


def save_current_settings():
    global settings
    #Delete the content in the settings file
    open(settings_file, "w").close()

    #Write the new settings into the file
    with open(settings_file, "a") as file:
        for key in settings:
            file.write(f"{key} = {settings[key]}\n")


def change_mods_folder_location():
    global settings
    new_mods_folder_location = filedialog.askdirectory()
    settings["mods_folder"] = new_mods_folder_location
    save_current_settings()