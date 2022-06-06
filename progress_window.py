from tkinter import ttk, Label, Button, Toplevel, HORIZONTAL
from PIL import ImageTk, Image
from dark_title_bar import *

def open_window(theme, modpack_name):
    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
    global root

    #Clear the theme_checkbuttons list in case it's the second time the user opens the settings window
    #and it contains things

    root = Toplevel()
    root.title("Installing...")
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


    global progress_bar

    modpack_name_label = Label(root,
        text = modpack_name,
        font = ("Arial", 12, "bold"),
        anchor = "w",
        bg = label_bg_color,
        fg = fg_color,
        image = virtualPixel,
        width = 200,
        height = 22)
    modpack_name_label.place(x = 25, y = 6)

    progress_bar = ttk.Progressbar(root, orient = HORIZONTAL, length = 230, mode = "determinate")
    progress_bar.place(x = 10, y = 34)


    root.mainloop()