from tkinter import Tk, Button, Toplevel

def open_settings_window(theme):
    #TODO: Move themes to another file that returns a tuple with the values of the variables,
    #      then, in the other files, the variables are assigned the value of this tuple.
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


    root = Toplevel()
    root.title("Settings")
    root.geometry("250x250")


    root.mainloop()