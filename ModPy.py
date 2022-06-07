from functools import partial
from tkinter import Tk, Button, Label, Frame
from tkinter.messagebox import askokcancel, WARNING
from PIL import ImageTk, Image
import os
import shutil
import time
from threading import Thread
from dark_title_bar import *


import settings as s
import progress_window as progressw
import import_modpack as import_func

root = Tk()
root.title("ModPy Beta 1")
root.geometry("350x520")  #Resolution of the window
root.resizable(False, False)  #Make it so you can't resize it

#settings is a dictionary that contains every user setting and its value
settings = s.get_user_settings()

mods_folder = settings["mods_folder"]

theme = settings["theme"]

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


#Frame offset variables are used to separate the frames from the edges of the window
widget_offset_x = 6
widget_offset_y = widget_offset_x


def enable_closing():
    root.protocol("WM_DELETE_WINDOW", root.destroy)


def disable_closing():
    root.protocol("WM_DELETE_WINDOW", lambda: print("Error: Not allowed to close the window"))


def create_button_panel_widgets():
    button_panel_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 60, bg = frame_bg_color, highlightbackground = "#afafaf", highlightthickness=1)
    button_panel_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y)

    import_modpack_button = Button(button_panel_frame,
        text = "Import",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 103 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = import_modpack)
    import_modpack_button.place(in_ = button_panel_frame, x = widget_offset_x, y = widget_offset_y)

    create_modpy_button = Button(
        text = "Create modpy file",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 193 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    create_modpy_button.place(in_ = button_panel_frame, x = 101, y = widget_offset_y)

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
    global settings

    destroy_modpack_buttons()
    s.set_up_window(theme)
    
    settings = s.get_user_settings


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

    for directory in os.listdir("modpacks"):
        modpacks_saved.append(directory)
    

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
                font = ("Arial", 12, "bold"),
                anchor = "w",
                bg = label_bg_color,
                fg = fg_color,
                image = virtualPixel, compound = "c",
                width = 318,
                height = 22))
            
        current_label = modpack_labels[current_position]  #Current label, the one we have to pack and bind a key to

        current_label.pack(padx = widget_offset_x, pady = widget_offset_y / 2)
        
        #We have to use partial() to call the function with arguments and not lambda because with lambda it won't work well,
        #it will use the last value of the arguments and not the one in the loop where the label is created
        current_label.bind("<Button-1>", partial(create_modpack_buttons, current_label, current_position))


def refresh_modpack_list():
    modpacks_saved.clear()
    for i in modpack_labels:
        i.destroy()
    modpack_labels.clear()
    created_modpack_buttons.clear()

    load_modpacks()
    show_modpacks()


def create_modpack_buttons(label, modpack_index, x):  #We use x as an argument because partial() needs an extra argument
    print(f"Modpack {modpack_index}")  #DEBUG LINE

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
        height = 14,
        command = lambda: install_modpack(modpack_index))
    install_button.place(in_ = label, x = 172, y = 1)

    options_button = Button(label,
        text = "Options",
        font = ("Arial", 12, "bold"),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 58,
        height = 14,
        command = lambda: print(f"{modpack_index} - options"))
    options_button.place(in_ = label, x = 228, y = 1)

    delete_button = Button(label,
        text = "✖",
        font = ("Arial", 19),
        bg = button_bg_color,
        fg = "#ff0000",
        activebackground = button_active_bg_color,
        activeforeground = "#ff0000",
        image = virtualPixel, compound = "c",
        width = 14,
        height = 14,
        command = lambda: delete_modpack(modpack_index))
    delete_button.place(in_ = label, x = 297, y = 1)

    created_modpack_buttons.append(install_button)
    created_modpack_buttons.append(options_button)
    created_modpack_buttons.append(delete_button)


def destroy_modpack_buttons(x = 0):
    for button in created_modpack_buttons:
        button.destroy()


def modpack_scroll(event):
    #If there are less than 14 modpacks, do not scroll to avoid bugs
    if len(modpacks_saved) < 14:
        return

    scroll_sensibility = 1

    for i in modpack_labels:
        current_x = i.winfo_x() - 1  #For some reason, if we don't add -1, the labels will go right
                                         #I think it is because the method returns an extra pixel or
                                         #the place method doesn't count the border or smth
        current_y = i.winfo_y()

        first_label = modpack_labels[0]
        last_label = modpack_labels[-1]

        if event.delta > 0:
            y_increment = 25 * scroll_sensibility
            #Top limit for the labels:
            #If the first label will go over the top when we add the scroll value, move it to the top and not more
            if first_label.winfo_y() + y_increment > 0:
                y_increment = -first_label.winfo_y() + 3  #The 3 (removed) is for the spacing between the frame and the label

        elif event.delta < 0:
            y_increment = -25 * scroll_sensibility
            #Bottom limit for the labels:
            #If the last label will go down the bottom when we add the scroll value, move it to the bottom and not more
            if last_label.winfo_y() + y_increment < 412:
                y_increment = 417 - last_label.winfo_y()


        i.place_forget()
        i.place(x = current_x, y = current_y + y_increment)


def import_modpack():
    #Create another file that will create a window to import from a folder, .zip or .modpy
    #The latter one is a file that contains the links where the mods need to be downloaded from
    import_func.open_window(theme, root)

    thread = Thread(target = import_modpack_check_for_refresh)
    thread.start()


def import_modpack_check_for_refresh():
    while True:
        if import_func.finished_importing == True:
            refresh_modpack_list()
            break
        time.sleep(0.1)


def install_modpack(modpack_index):
    if int(settings["install_confirmation"]) == 1:
        user_has_confirmed = askokcancel("Modpack installation",
        "You are about to install a modpack.\nYour current mods will be deleted.\nDo you want to continue?",
        icon = WARNING)
    
        if not user_has_confirmed:
            return

    #Start progress window
    progressw.open_window("Installing...", theme, modpacks_saved[modpack_index])

    #Create a thread to execute the actions over the progress window
    #If we don't use a thread, the window will not open until all the actions are finished
    thread = Thread(target = _install_actions, args = (modpack_index,))
    thread.start()


def _install_actions(modpack_index):
    modpack_route = f"modpacks/{modpacks_saved[modpack_index]}/"

    #Disable closing
    disable_closing()

    #Delete the mods folder
    progressw.change_info_text("Deleting mods folder...")
    try:
        shutil.rmtree(mods_folder)
    except:
        print("Mods folder does not exist, avoiding deleting it...")
    progressw.change_progress(10)

    #Copy the files of the modpack to the mods folder
    progressw.change_info_text("Copying mods...")
    shutil.copytree(modpack_route, mods_folder)
    progressw.change_progress(100)

    #End progress window
    progressw.change_info_text("Finished installing modpack")
    progressw.end()

    #Enable closing
    enable_closing()

    print("Finished installing modpack")


def delete_modpack(modpack_index):
    if int(settings["delete_confirmation"]) == 1:
        user_has_confirmed = askokcancel("Modpack deletion",
        "You are about to delete a modpack.\nDo you want to continue?",
        icon = WARNING)
    
        if not user_has_confirmed:
            return

    #Start progress window
    progressw.open_window("Deleting...", theme, modpacks_saved[modpack_index])

    #Create a thread to execute the actions over the progress window
    #If we don't use a thread, the window will not open until all the actions are finished
    thread = Thread(target = _delete_actions, args = (modpack_index,))
    thread.start()


def _delete_actions(modpack_index):
    modpack_route = f"modpacks/{modpacks_saved[modpack_index]}/"

    #Disable closing
    disable_closing()

    #Delete the modpack folder
    progressw.change_info_text("Removing modpack...")
    shutil.rmtree(modpack_route)
    progressw.change_progress(100)

    #End progress window
    progressw.change_info_text("Finished deleting modpack")
    progressw.end()

    #Enable closing
    enable_closing()

    #Refresh the modpack list (TODO)
    refresh_modpack_list()


create_button_panel_widgets()
create_modpack_list_structure()
load_modpacks()
show_modpacks()


root.mainloop()