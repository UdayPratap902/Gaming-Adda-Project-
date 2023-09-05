import tkinter
import random
import pygame
pygame.mixer.init()
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30


def startGame(event):
    global score
    global timeleft
    if timeleft == 30:
        countdown()
    elif timeleft == 0:
        score = 0
        timeleft = 30
        countdown()
    else:
        nextColour(event)
    nextColour(event)


def nextColour(event):
    global score
    global timeleft
    if timeleft == 30:
        countdown()
        nextColour(event)
    elif timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
            pygame.mixer.music.load(
                r"U:\PythonApp\MiniProject\GamingAdda\mixkit-bonus-earned-in-video-game-2058.wav")
            pygame.mixer.music.play(loops=1)
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        pygame.mixer.music.load(
            r"U:\PythonApp\MiniProject\GamingAdda\timeup.wav")
        pygame.mixer.music.play(loops=1)


root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("1500x800")
instructions = tkinter.Label(
    root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 30))
instructions.pack()
scoreLabel = tkinter.Label(
    root, text="Press space to start", font=('Helvetica', 16))
scoreLabel.pack()
timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()
e = tkinter.Entry(root)
root.bind('<Return>', nextColour)
root.bind('<space>', startGame)
e.pack()
e.focus_set()
root.mainloop()
