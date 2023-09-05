from tkinter import *
import pygame
import os

root = Tk()

root.geometry("1920x1080")
# root.configure(bg="teal")
# pygame.mixer.init()
# pygame.mixer.music.load(r"C:\Users\Dell\Documents\cod\a.wav")
# pygame.mixer.music.play(loops=1)


# Create a Canvas widget that fills the entire window
canvas = Canvas(root, width=1528, height=828)
canvas.pack()

# Load the background image and set it as the canvas background
bg_img = PhotoImage(
    file=r"U:\PythonApp\MiniProject\GamingAdda\new-world-island-4k-wallpaper-3840x2160.png")
bg_img = bg_img.zoom(2)   # Optional: zoom in the image to double its size
bg_img = bg_img.subsample(bg_img.width() // 1500)
canvas.create_image(0, 0, image=bg_img, anchor="nw")


# button work

img1 = PhotoImage(file=r"U:\PythonApp\MiniProject\GamingAdda\s2.png")
img2 = PhotoImage(file=r"U:\PythonApp\MiniProject\GamingAdda\s4.png")
img3 = PhotoImage(file=r"U:\PythonApp\MiniProject\GamingAdda\s3.png")
img4 = PhotoImage(file=r"U:\PythonApp\MiniProject\GamingAdda\s1.png")


def g1():
    os.system(r"U:\PythonApp\MiniProject\GamingAdda\andapakdo.py")


def g2():
    os.system(r"U:\PythonApp\MiniProject\GamingAdda\tictactoe.py")


def g3():
    os.system(r"U:\PythonApp\MiniProject\GamingAdda\Colorgame.py")


def g4():
    os.system(r"U:\PythonApp\MiniProject\GamingAdda\snakegame.py")


b1 = Button(root, text="game1", image=img1, command=g1)
b1.place(x=800, y=145)
b2 = Button(root, text="game2", image=img2, command=g2)
b2.place(x=540, y=145)
b3 = Button(root, text="game3", image=img3, command=g3)
b3.place(x=540, y=400)
b4 = Button(root, text="game4", image=img4, command=g4)
b4.place(x=800, y=400)

root.mainloop()
