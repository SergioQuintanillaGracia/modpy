from tkinter import ttk, Label, Button, Toplevel, HORIZONTAL, DISABLED, NORMAL
from PIL import ImageTk, Image
from dark_title_bar import *


def open_window(window_title, theme, main_root_, modpack_name, windows_to_destroy = ()):
    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
    global root, main_root, virtualPixel, windows_to_destroy_list

    windows_to_destroy_list = windows_to_destroy
    main_root = main_root_

    #Clear the theme_checkbuttons list in case it's the second time the user opens the settings window
    #and it contains things

    root = Toplevel()
    root.title(window_title)
    root.geometry("250x150")
    root.resizable(False, False)

    root.protocol("WM_DELETE_WINDOW", lambda: print("Error: Not allowed to close the window"))


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


    modpack_name_label = Label(root,
        text = modpack_name,
        font = ("Arial", 13, "bold"),
        bg = label_bg_color,
        fg = fg_color,
        image = virtualPixel, compound = "c",
        width = 200,
        height = 22)
    modpack_name_label.place(in_ = root, x = 25, y = 7)

    global progressbar

    progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 230, mode = "determinate")
    progressbar.place(x = 10, y = 41)

    global progress_information_label, ok_button, close_modpy_button

    progress_information_label = Label(root,
        text = "Starting...",
        font = ("Arial", 11),
        anchor = "w",
        bg = bg_color,
        fg = fg_color,
        image = virtualPixel, compound = "c",
        width = 224,
        height = 18)
    progress_information_label.place(x = 10, y = 69)

    ok_button = Button(root,
        text = "OK",
        font = ("Arial", 12),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 36,
        height = 26,
        state = DISABLED,
        command = ok_button_actions)
    ok_button.place(x = 19, y = 100)

    close_modpy_button = Button(root,
        text = "Close ModPy",
        font = ("Arial", 12),
        bg = button_bg_color,
        fg = fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 106,
        height = 26,
        state = DISABLED,
        command = main_root.destroy)
    close_modpy_button.place(x = 93, y = 100)


def change_info_text(new_text):
    global progress_information_label
    progress_information_label["text"] = new_text


def change_progress(new_progress):
    global progressbar
    progressbar["value"] = new_progress


def end():
    global progressbar, ok_button, close_modpy_button

    progressbar["value"] = 100

    root.protocol("WM_DELETE_WINDOW", root.destroy)
    
    ok_button["state"] = NORMAL
    close_modpy_button["state"] = NORMAL


def ok_button_actions():
    global windows_to_destroy_list
    for i in windows_to_destroy_list:
        i.destroy()

    root.destroy()