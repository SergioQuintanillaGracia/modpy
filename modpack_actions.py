import shutil
from tkinter import Label, Button, Toplevel, DISABLED, filedialog
from tkinter.messagebox import askokcancel, WARNING
from PIL import ImageTk, Image
import os
from threading import Thread
from dark_title_bar import *

import progress_window as progressw
import settings as s


def open_import_window(theme_, m_root):
    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
    global root, main_root, virtualPixel, import_folder_pressed, import_zip_pressed, import_modpy_pressed
    global theme, finished_importing

    theme = theme_
    
    finished_importing = False

    main_root = m_root
    import_folder_pressed = False
    import_zip_pressed = False
    import_modpy_pressed = False

    #Clear the theme_checkbuttons list in case it's the second time the user opens the settings window
    #and it contains things

    root = Toplevel()
    root.title("Import modpack")
    root.geometry("241x81")
    root.resizable(False, False)


    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
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


    import_from_label = Label(root,
        text = "Import from:",
        font = ("Arial", 12, "bold"),
        bg = bg_color,
        fg = fg_color,
        image = virtualPixel, compound = "c",
        width = 120,
        height = 22)
    import_from_label.place(in_ = root, x = 60, y = 7)

    folder_button = Button(root,
        text = "Folder",
        font = ("Arial", 12),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 41,
        height = 21,
        command = import_folder)
    folder_button.place(x = 6, y = 41)

    zip_button = Button(root,
        text = ".zip",
        font = ("Arial", 12),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 41,
        height = 21,
        state = DISABLED,
        command = import_zip)
    zip_button.place(x = 84, y = 41)

    modpy_button = Button(root,
        text = ".modpy",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 41,
        height = 21,
        state = DISABLED,
        command = import_modpy)
    modpy_button.place(x = 162, y = 41)


def install_modpack(modpack_index, theme, root, modpacks_saved):
    if int(s.settings["install_confirmation"]) == 1:
        user_has_confirmed = askokcancel("Modpack installation",
        "You are about to install a modpack.\nYour current mods will be deleted.\nDo you want to continue?",
        icon = WARNING)
    
        if not user_has_confirmed:
            return

    #Start progress window
    progressw.open_window("Installing...", theme, root, modpacks_saved[modpack_index])

    #Create a thread to execute the actions over the progress window
    #If we don't use a thread, the window will not open until all the actions are finished
    thread = Thread(target = _install_actions, args = (modpack_index, modpacks_saved))
    thread.start()


def _install_actions(modpack_index, modpacks_saved):
    modpack_route = f"modpacks/{modpacks_saved[modpack_index]}/"

    #Disable closing
    disable_closing()

    #Delete the mods folder
    progressw.change_info_text("Deleting mods folder...")
    try:
        shutil.rmtree(s.settings["mods_folder"])
    except:
        print("Mods folder does not exist, avoiding deleting it...")
    progressw.change_progress(10)

    #Copy the files of the modpack to the mods folder
    progressw.change_info_text("Copying mods...")
    shutil.copytree(modpack_route, s.settings["mods_folder"])
    progressw.change_progress(100)

    #End progress window
    progressw.change_info_text("Finished installing modpack")
    progressw.end()

    #Enable closing
    enable_closing()

    print("Finished installing modpack")


def enable_closing():
    try:
        root.protocol("WM_DELETE_WINDOW", root.destroy)
    except: pass
    try:
        main_root.protocol("WM_DELETE_WINDOW", main_root.destroy)
    except: pass


def disable_closing():
    try:
        root.protocol("WM_DELETE_WINDOW", lambda: print("Error: Not allowed to close the window"))
    except: pass
    try:
        main_root.protocol("WM_DELETE_WINDOW", lambda: print("Error: Not allowed to close the window"))
    except: pass


def import_folder():
    #Let the user choose the folder
    modpack_route = filedialog.askdirectory()
    
    if modpack_route == "":
        return

    new_modpack_route = f"modpacks/{os.path.basename(modpack_route)}"

    #Start progress window
    progressw.open_window("Importing modpack", theme, main_root, os.path.basename(modpack_route), (root,))

    #Create a thread to execute the actions over the progress window
    #If we don't use a thread, the window will not open until all the actions are finished
    thread = Thread(target = _import_folder_actions, args = (modpack_route, new_modpack_route))
    thread.start()


def _import_folder_actions(modpack_route, new_modpack_route):
    global finished_importing

    #Disable closing
    disable_closing()

    #Copy content of the modpack route to the modpacks folder
    progressw.change_info_text("Copying mods...")
    shutil.copytree(modpack_route, new_modpack_route)
    progressw.change_progress(100)

    #End progress window
    progressw.change_info_text("Finished importing modpack")
    progressw.end()

    #Enable closing
    enable_closing()

    finished_importing = True


def import_zip():
    #Let the user choose the folder
    modpack_route = filedialog.askopenfile()
    
    if modpack_route == "":
        return

    new_modpack_route = f"modpacks/{os.path.basename(modpack_route)}"

    #Start progress window
    progressw.open_window("Importing modpack", theme, main_root, os.path.basename(modpack_route), (root,))

    #Create a thread to execute the actions over the progress window
    #If we don't use a thread, the window will not open until all the actions are finished
    thread = Thread(target = _import_folder_actions, args = (modpack_route, new_modpack_route))
    thread.start()


def _import_zip_actions(modpack_route, new_modpack_route):
    global finished_importing

    #Disable closing
    disable_closing()

    #Copy content of the modpack route to the modpacks folder
    progressw.change_info_text("Copying mods...")
    shutil.copytree(modpack_route, new_modpack_route)
    progressw.change_progress(100)

    #End progress window
    progressw.change_info_text("Finished importing modpack")
    progressw.end()

    #Enable closing
    enable_closing()

    finished_importing = True


def import_modpy():
    #Disable closing
    disable_closing()