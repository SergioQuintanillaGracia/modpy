from pickle import NONE
from tkinter import Checkbutton, Label, Button, Frame, Toplevel, filedialog, DISABLED, IntVar, messagebox
from PIL import ImageTk, Image
from dark_title_bar import *

settings_file = "settings/settings.txt"

theme_checkbuttons = []
current_theme = NONE


def set_up_window(theme):
    global root, theme_checkbuttons

    #Clear the theme_checkbuttons list in case it's the second time the user opens the settings window
    #and it contains things
    theme_checkbuttons.clear()

    root = Toplevel()
    root.title("Settings")
    root.geometry("250x355")
    root.resizable(False, False)

    #Variables for the checkbuttons
    global check_light_mode, check_discord_dark, check_dark_mode, check_installing_modpack, check_deleting_modpack
    check_light_mode = IntVar()
    check_discord_dark = IntVar()
    check_dark_mode = IntVar()
    check_installing_modpack = IntVar()
    check_deleting_modpack = IntVar()


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

    #Change mods folder UI part

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
    change_mods_folder_location_button.place(x = 54, y = 13)

    #Themes UI part
    global light_mode_checkbutton, discord_dark_checkbutton, dark_mode_checkbutton

    theme_frame = Frame(root, width = 238, height = 130, bg = bg_color, highlightbackground = "#afafaf", highlightthickness = 1)
    theme_frame.place(x = 6, y = 94)

    theme_label = Label(root,
        text = "Themes",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        relief = "groove",
        image = virtualPixel, compound = "c",
        width = 70,
        height = 16)
    theme_label.place(x = 87, y = 83)

    theme_checkbuttons_x_spacing = 45

    light_mode_checkbutton = Checkbutton(theme_frame,
        text = "Light mode",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        variable = check_light_mode,
        selectcolor = button_active_bg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        command = change_theme)
    light_mode_checkbutton.place(x = theme_checkbuttons_x_spacing, y = 16)

    discord_dark_checkbutton = Checkbutton(theme_frame,
        text = "Discord dark",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        variable = check_discord_dark,
        selectcolor = button_active_bg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        command = change_theme)
    discord_dark_checkbutton.place(x = theme_checkbuttons_x_spacing, y = 46)

    dark_mode_checkbutton = Checkbutton(theme_frame,
        text = "Dark mode",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        variable = check_dark_mode,
        selectcolor = button_active_bg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        state = DISABLED,
        command = change_theme)
    dark_mode_checkbutton.place(x = theme_checkbuttons_x_spacing, y = 76)

    theme_checkbuttons.append(light_mode_checkbutton)
    theme_checkbuttons.append(discord_dark_checkbutton)
    theme_checkbuttons.append(dark_mode_checkbutton)

    global current_theme
    current_theme = settings["theme"]
    get_theme_button_variable(current_theme).set(1)

    check_installing_modpack.set(int(settings["install_confirmation"]))
    check_deleting_modpack.set(int(settings["delete_confirmation"]))


    #Confirmations UI part

    confirmation_checkbuttons_x_spacing = 23

    confirmations_frame = Frame(root, width = 238, height = 100, bg = bg_color, highlightbackground = "#afafaf", highlightthickness = 1)
    confirmations_frame.place(x = 6, y = 249)

    confirmations_label = Label(root,
        text = "Show confirmation when:",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        relief = "groove",
        image = virtualPixel, compound = "c",
        width = 209,
        height = 16)
    confirmations_label.place(x = 17, y = 238)

    installing_modpack_checkbutton = Checkbutton(confirmations_frame,
        text = "Installing modpack",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        variable = check_installing_modpack,
        selectcolor = button_active_bg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        command = change_installing_modpack_confirmation)
    installing_modpack_checkbutton.place(x = confirmation_checkbuttons_x_spacing, y = 16)

    deleting_modpack_checkbutton = Checkbutton(confirmations_frame,
        text = "Deleting modpack",
        font = ("Arial", 14),
        bg = bg_color,
        fg = fg_color,
        variable = check_deleting_modpack,
        selectcolor = button_active_bg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        command = change_deleting_modpack_confirmation)
    deleting_modpack_checkbutton.place(x = confirmation_checkbuttons_x_spacing, y = 46)


    root.mainloop()


def get_user_settings():
    global settings, current_theme
    #settings will contain every user setting and its value
    settings = {}

    try:
        for i in open(settings_file, "r"):
            #Split the line and save it in a key-value format in settings
            key_value = i.split(" = ")

            #If, by new line errors, various lines are together, raise an error and load the default settings
            if len(key_value) != 2:
                raise

            settings[key_value[0]] = key_value[1].strip()  #We use strip to remove any \n characters

    except:
        get_default_settings()
        save_current_settings()

    return settings


def get_default_settings():
    global settings, current_theme
    settings = {
        "mods_folder":"C:/Users/sergi/AppData/Roaming/.minecraft/mods",  #TODO: Make this user independent
        "theme":"light",
        "install_confirmation":"0",
        "delete_confirmation":"1"
    }

    print("Default settings applied")
    
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
    global settings, root

    new_mods_folder_location = filedialog.askdirectory()
    settings["mods_folder"] = new_mods_folder_location

    save_current_settings()
    root.focus()


def get_theme_button_variable(theme):
    #Given the name of a theme or a button object, return the variable of the theme
    if theme == "light" or theme == light_mode_checkbutton:
        return check_light_mode
    if theme == "discord dark" or theme == discord_dark_checkbutton:
        return check_discord_dark
    if theme == "dark" or theme == dark_mode_checkbutton:
        return check_dark_mode

def get_theme_name(theme):
    #Given the name of a variable or a button object, return the name of the theme
    if theme == check_light_mode or theme == light_mode_checkbutton:
        return "light"
    if theme == check_discord_dark or theme == discord_dark_checkbutton:
        return "discord dark"
    if theme == check_dark_mode or theme == dark_mode_checkbutton:
        return "dark"


def change_theme():
    #Will manage the change between light, discord dark and dark modes
    global current_theme

    get_theme_button_variable(current_theme).set(0)
    
    marked_theme_count = 0

    for theme in theme_checkbuttons:
        if get_theme_button_variable(theme).get() == 1:
            marked_theme_count += 1
            current_theme = get_theme_name(theme)
            break

    if marked_theme_count == 0:
        get_theme_button_variable(current_theme).set(1)
        return

    #Save the new theme in settings
    settings["theme"] = current_theme
    save_current_settings()

    messagebox.showinfo("Theme update", "The new theme will be applied when you restart ModPy.")


def change_installing_modpack_confirmation():
    settings["install_confirmation"] = check_installing_modpack.get()
    save_current_settings()


def change_deleting_modpack_confirmation():
    settings["delete_confirmation"] = check_deleting_modpack.get()
    save_current_settings()