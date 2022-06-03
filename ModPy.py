from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ModPy Alpha 0.1")
root.geometry("350x500")  #Resolution of the window
root.resizable(False, False)  #Make it so you can't resize it

#Frame offset variables are used to separate the frames from the edges of the window
widget_offset_x = 6
widget_offset_y = widget_offset_x

#virtualPixel is used to make the buttons completely resizable
virtualPixel = ImageTk.PhotoImage(Image.open("images/virtualPixel.png"))


def create_button_panel():
    button_panel_frame = Frame(root, width = 350 - widget_offset_x * 2, height = 60, highlightbackground="#afafaf", highlightthickness=1)
    button_panel_frame.place(in_ = root, x = widget_offset_x, y = widget_offset_y)

    plus_sign_image = ImageTk.PhotoImage(Image.open("images/plus_sign.png"))
    add_button = Button(
        font = ("Arial", 55),
        image = plus_sign_image, compound = "c",
        width = 60 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    add_button.place(in_ = button_panel_frame, x = widget_offset_x, y = widget_offset_y)

    remove_button = Button(
        text = "-",
        font = ("Arial", 55),
        image = virtualPixel, compound = "c",
        width = 60 - widget_offset_x * 4 + 2,
        height = 60 - widget_offset_x * 4 + 2,
        command = print)
    remove_button.place(in_ = button_panel_frame, x = 60 + widget_offset_x, y = 60 + widget_offset_y)


create_button_panel()


root.mainloop()