from functools import partial
from pickle import NONE
from tkinter import Canvas, Tk, Button, Label, Frame
from PIL import ImageTk, Image
import os
from dark_title_bar import *

import settings as s

root = Tk()
root.title("ModPy Beta 1")
root.geometry("350x520")  #Resolution of the window
root.resizable(False, False)  #Make it so you can't resize it

#Change the theme to get different colors
theme = "light"
config_folder = "config/"
mods_folder = str(os.getenv("APPDATA")) + "/.minecraft/mods/"

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
    frame_bg_color = "#2f3136"
    highlightbackground_color = "#8a8a8a"
    settings_cog = ImageTk.PhotoImage(Image.open("images/settings_cog_discord_dark.png"))
    #virtualPixel is used to make the buttons completely resizable
    virtualPixel = ImageTk.PhotoImage(Image.open("images/virtualPixel_discord_dark.png"))


root.configure(bg = bg_color)


#Frame offset variables are used to separate the frames from the edges of the window
widget_offset_x = 6
widget_offset_y = widget_offset_x


def create_button_panel_widgets():
    button_panel_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 60, bg = frame_bg_color, highlightbackground = "#afafaf", highlightthickness=1)
    button_panel_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y)

    add_modpack_button = Button(
        text = "Add Modpack",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 141 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    add_modpack_button.place(in_ = button_panel_frame, x = widget_offset_x, y = widget_offset_y)

    import_from_file_button = Button(button_panel_frame,
        text = "Import from file",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 152 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    import_from_file_button.place(in_ = button_panel_frame, x = 139, y = widget_offset_y)

    settings_button = Button(
        relief = "flat",
        bg = frame_bg_color,
        activebackground = button_active_bg_color,
        image = settings_cog,
        command = open_settings)
    settings_button.place(in_ = button_panel_frame, x = 283, y = widget_offset_y - 2)


def create_modpack_list_structure():
    global modpack_list_frame
    
    modpack_list_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 442, bg = frame_bg_color, highlightbackground = "#afafaf", highlightthickness=1)
    modpack_list_frame.place(in_ = root, x = 6, y = 72)

    root.bind("<MouseWheel>", modpack_scroll)  #NOTE: In Linux, <MouseWheel> is <Button-4> and <Button-5>


def open_settings():
    destroy_modpack_buttons()
    s.open_settings_window(theme)


#This list holds the name of every modpack that has been saved by the user
modpacks_saved = []
#This list holds every label objects that are used to show the modpacks
modpack_labels = []
#This list holds every button created when clicking a modpack. It is used to delete every created button
#when the user clicks a modpack, so there are not multiple sets of buttons at the same time in different modpacks.
created_modpack_buttons = []


def load_modpacks():
    #This function will save every modpack that the user has saved in the modpacks_saved list.
    #At the moment, this is just a placeholder so I can continue working on the program.
    #This functionality will be implemented in the future.
    modpacks_saved.append("Test 0 modpack")
    modpacks_saved.append("Test 1 modpack")
    modpacks_saved.append("Test 2 modpack")
    modpacks_saved.append("Test 3 modpack")
    modpacks_saved.append("Test 4 modpack")
    modpacks_saved.append("Test 5 modpack")
    modpacks_saved.append("Test 6 modpack")
    modpacks_saved.append("Test 7 modpack")
    modpacks_saved.append("Test 8 modpack")
    modpacks_saved.append("Test 9 modpack")
    modpacks_saved.append("Test 10 modpack")
    modpacks_saved.append("Test 11 modpack")
    modpacks_saved.append("Test 12 modpack")
    modpacks_saved.append("Test 13 modpack")
    modpacks_saved.append("Test 14 modpack")
    modpacks_saved.append("Test 15 modpack")
    

def show_modpacks():
    #TODO
    #Shows every modpack saved by the user in modpack_list_frame, creating buttons to install, see options and delete them.
    global modpack_list_frame

    for modpack in modpacks_saved:
        current_position = modpacks_saved.index(modpack)  #Current modpack position in the list (index)

        #Add a label to the modpack_labels list
        modpack_labels.append(
            Label(modpack_list_frame,
                text = modpack,
                font = ("Arial", 14),
                anchor = "w",
                bg = label_bg_color,
                fg = fg_color,
                image = virtualPixel, compound = "c",
                width = 318,
                height = 26
                ))
            
        current_label = modpack_labels[current_position]  #Current label, the one we have to pack and bind a key to

        current_label.pack(padx = widget_offset_x, pady = widget_offset_y / 2)
        
        #We have to use partial() to call the function with arguments and not lambda because with lambda it won't work well,
        #it will use the last value of the arguments and not the one in the loop where the label is created
        current_label.bind("<Button-1>", partial(create_modpack_buttons, current_label, str(current_position)))


def create_modpack_buttons(label, modpack, x):  #We use x as an argument because partial() needs an extra argument
    print("Modpack " + modpack)  #DEBUG LINE

    #Delete every other button created next to a modpack name
    destroy_modpack_buttons()

    install_button = Button(label,
        text = "Install",
        font = ("Arial", 12, "bold"),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 45,
        height = 18,
        command = lambda: print(f"{modpack} - install"))
    install_button.place(in_ = label, x = 168, y = 1)

    options_button = Button(label,
        text = "Options",
        font = ("Arial", 12, "bold"),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 58,
        height = 18,
        command = lambda: print(f"{modpack} - options"))
    options_button.place(in_ = label, x = 224, y = 1)

    delete_button = Button(label,
        text = "✖",
        font = ("Arial", 19),
        bg = button_bg_color,
        fg = "#ff0000",
        activebackground = button_active_bg_color,
        activeforeground = "#ff0000",
        image = virtualPixel, compound = "c",
        width = 18,
        height = 18,
        command = lambda: print(f"{modpack} - delete"))
    delete_button.place(in_ = label, x = 293, y = 1)

    created_modpack_buttons.append(install_button)
    created_modpack_buttons.append(options_button)
    created_modpack_buttons.append(delete_button)


def destroy_modpack_buttons(x = 0):
    for button in created_modpack_buttons:
        button.destroy()


def modpack_scroll(event):
    print("Scrolled",event.delta)  #Debug

    scroll_sensibility = 0.3

    for i in modpack_labels:
        current_x = i.winfo_x() - 1  #For some reason, if we don't add -1, the labels will go right
                                         #I think it is because the method returns an extra pixel or
                                         #the place method doesn't count the border or smth
        current_y = i.winfo_y()
        new_y = current_y + event.delta * scroll_sensibility

        

        i.place_forget()
        i.place(x = current_x, y = new_y)


create_button_panel_widgets()
create_modpack_list_structure()
load_modpacks()
show_modpacks()


root.mainloop()