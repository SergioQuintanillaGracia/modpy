from tkinter import ttk, Label, Button, Toplevel, HORIZONTAL, DISABLED, NORMAL
from PIL import ImageTk, Image
from dark_title_bar import *


def open_window(theme):
    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
    global root, virtualPixel

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
        font = ("Arial", 14, "bold"),
        bg = bg_color,
        fg = fg_color,
        image = virtualPixel, compound = "c",
        width = 120,
        height = 22)
    import_from_label.place(in_ = root, x = 60, y = 7)

    folder_button = Button(root,
        text = "Folder",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 65,
        height = 26,
        command = print)
    folder_button.place(x = 6, y = 41)

    zip_button = Button(root,
        text = ".zip",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 65,
        height = 26,
        command = print)
    zip_button.place(x = 84, y = 41)

    modpy_button = Button(root,
        text = ".modpy",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 65,
        height = 26,
        command = print)
    modpy_button.place(x = 162, y = 41)