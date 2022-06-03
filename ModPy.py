from tkinter import *
from PIL import ImageTk, Image

#Change the theme to get different colors
theme = "light"

if theme == "light":
    bg_color = "#f0f0f0"
    highlightbackground_color = "#afafaf"

if theme == "discord dark":
    bg_color = "#202225"
    highlightbackground_color = "#afafaf"


root = Tk()
root.title("ModPy Beta 1")
root.geometry("350x500")  #Resolution of the window
root.resizable(False, False)  #Make it so you can't resize it
root.configure(bg = bg_color)


#Frame offset variables are used to separate the frames from the edges of the window
widget_offset_x = 6
widget_offset_y = widget_offset_x

#virtualPixel is used to make the buttons completely resizable
virtualPixel = ImageTk.PhotoImage(Image.open("images/virtualPixel.png"))


def create_button_panel_widgets():
    button_panel_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 60, bg = bg_color, highlightbackground = "#afafaf", highlightthickness=1)
    button_panel_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y)

    add_button = Button(
        text = "+",
        font = ("Arial", 55),
        bg = "#c3c3c3",
        activebackground = "#c3c3c3",
        image = virtualPixel, compound = "c",
        width = 60 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    add_button.place(in_ = button_panel_frame, x = widget_offset_x, y = widget_offset_y)

    remove_button = Button(
        text = "-",
        font = ("Arial", 55),
        bg = "#c3c3c3",
        activebackground = "#c3c3c3",
        image = virtualPixel, compound = "c",
        width = 60 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    remove_button.place(in_ = button_panel_frame, x = 58, y = widget_offset_y)

    import_from_file_button = Button(
        text = "Import from file",
        font = ("Arial", 14),
        bg = "#c3c3c3",
        activebackground = "#c3c3c3",
        image = virtualPixel, compound = "c",
        width = 180 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    import_from_file_button.place(in_ = button_panel_frame, x = 110, y = widget_offset_y)

    global settings_cog  #If you don't make an image variable global, you won't be able to use it
    settings_cog = ImageTk.PhotoImage(Image.open("images/settings_cog.png"))
    settings_button = Button(
        relief = "flat",
        image = settings_cog,
        command = print)
    settings_button.place(in_ = button_panel_frame, x = 283, y = widget_offset_y - 2)


def create_modpack_list_widgets():
    button_panel_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 60, highlightbackground = "#afafaf", highlightthickness=1)
    button_panel_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y)


create_button_panel_widgets()


root.mainloop()