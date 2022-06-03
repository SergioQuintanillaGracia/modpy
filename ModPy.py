from tkinter import *

root = Tk()
root.title("ModPy Alpha 0.1")
root.geometry("350x500")  #Resolution of the window
root.resizable(False, False)  #Make it so you can't resize it

frame_offset_x = 6
frame_offset_y = frame_offset_x


button_frame = Frame(root, width = 350 - frame_offset_x * 2, height = 60, highlightbackground="#afafaf", highlightthickness=1)
button_frame.place(x = frame_offset_x, y = frame_offset_y)


root.mainloop()