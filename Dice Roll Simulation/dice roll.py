import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("600x360")
window.title("Dice Roll Simulation")

# def roll_dice():
#     a = random.randint(1,6)
#     label = tk.Label(window, text=a).pack()



dice = ["Dice Roll Simulation/images/d1.png","Dice Roll Simulation/images/d2.png","Dice Roll Simulation/images/d3.png","Dice Roll Simulation/images/d4.png","Dice Roll Simulation/images/d5.png","Dice Roll Simulation/images/d6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x=40, y=100)
label2.place(x=300, y=100)


def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2
button = tk.Button(window,text="ROLL",bg="green", fg = "white", font= "Times 20 bold", command=dice_roll)
button.pack()



window.mainloop()