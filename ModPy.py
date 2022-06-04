from tkinter import Tk, Button, Label, Frame
from PIL import ImageTk, Image
import os
from dark_title_bar import *

import settings as s

root = Tk()
root.title("ModPy Beta 1")
root.geometry("350x500")  #Resolution of the window
root.resizable(False, False)  #Make it so you can't resize it

#Change the theme to get different colors
theme = "discord dark"
config_folder = "config/"
mods_folder = str(os.getenv("APPDATA")) + "/.minecraft/mods/"

if theme == "light":
    print("Theme set to \"light\"")
    bg_color = "#f0f0f0"
    button_bg_color = "#c3c3c3"
    button_fg_color = "#000000"
    button_active_bg_color = button_bg_color
    button_active_foreground_color = button_fg_color
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
    button_fg_color = "#d2d3d5"
    button_active_bg_color = button_bg_color
    button_active_foreground_color = button_fg_color
    frame_bg_color = "#2f3136"
    highlightbackground_color = "#8a8a8a"
    settings_cog = ImageTk.PhotoImage(Image.open("images/settings_cog_discord_dark.png"))
    #virtualPixel is used to make the buttons completely resizable
    virtualPixel = ImageTk.PhotoImage(Image.open("images/virtualPixel_discord_dark.png"))


root.configure(bg = bg_color)


#Frame offset variables are used to separate the frames from the edges of the window
widget_offset_x = 6
widget_offset_y = widget_offset_x


dark_title_bar(root)


def create_button_panel_widgets():
    button_panel_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 60, bg = frame_bg_color, highlightbackground = "#afafaf", highlightthickness=1)
    button_panel_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y)

    add_button = Button(
        text = "+",
        font = ("Arial", 55),
        bg = button_bg_color,
        fg = button_fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 60 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    add_button.place(in_ = button_panel_frame, x = widget_offset_x, y = widget_offset_y)

    remove_button = Button(
        text = "-",
        font = ("Arial", 55),
        bg = button_bg_color,
        fg = button_fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 60 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    remove_button.place(in_ = button_panel_frame, x = 58, y = widget_offset_y)

    import_from_file_button = Button(button_panel_frame,
        text = "Import from file",
        font = ("Arial", 14),
        bg = button_bg_color,
        fg = button_fg_color,
        activebackground = button_active_bg_color,
        activeforeground = button_active_foreground_color,
        image = virtualPixel, compound = "c",
        width = 180 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    import_from_file_button.place(in_ = button_panel_frame, x = 110, y = widget_offset_y)

    settings_button = Button(
        relief = "flat",
        bg = button_bg_color,
        activebackground = button_active_bg_color,
        image = settings_cog,
        command = lambda : s.open_settings_window(theme))
    settings_button.place(in_ = button_panel_frame, x = 283, y = widget_offset_y - 2)


def create_modpack_list_widgets():
    modpack_list_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 422, bg = frame_bg_color, highlightbackground = "#afafaf", highlightthickness=1)
    modpack_list_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y + 60 + widget_offset_y)

    #TODO: Add the code to create the modpack list


create_button_panel_widgets()
create_modpack_list_widgets()


root.mainloop()