from tkinter import *
import os

root = Tk()
root.geometry("1920x1080")

# Create a Canvas widget that fills the entire window
canvas = Canvas(root, width=1528, height=828)
canvas.pack()

# Load the background image and set it as the canvas background
bg_img = PhotoImage(
    file=r"U:\PythonApp\MiniProject\GamingAdda\cool-geometric-triangular-figure-neon-laser-light-great-backgrounds_181624-11068.png")
bg_img = bg_img.zoom(10)   # Optional: zoom in the image to double its size
bg_img = bg_img.subsample(bg_img.width() // 1500)
canvas.create_image(0, 0, image=bg_img, anchor="nw")

# Create a label for the logo and place it on the canvas
logo_label = Label(canvas, text="Gaming Adda-", font=(
    "Algerian", 90), fg="white", bg="black")
logo_label.place(x=100, y=90)

# Load the button image and reduce its size

# Create a button and place it on the canvas


def g1():
    os.system(r"U:\PythonApp\MiniProject\GamingAdda\gameselection.py")


b1 = Button(root, text="---- Start ----", font=("algerian", 22), command=g1)
b1.place(x=670, y=670)
b1['background'] = 'black'
b1['foreground'] = 'white'
root.mainloop()
