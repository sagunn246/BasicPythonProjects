from tkinter import *
import random

low = 1
high = 1000
window = Tk()


def click():
    global ran_num
    global low
    global high
    ran_num = random.randint(low, high)
    label.config(text=ran_num)


window.title("Random Number Generator")

image = PhotoImage(file="po.png")
image = image.subsample(7, 7)
label = Label(window, text="?")
label.pack()
label.config(font=("Monospace", 50))
button = Button(window, text="Generate")
button.config(command=click)
button.config(font=("Ink free", 50, "bold"))
button.config(background="#ff6200")
button.config(fg="#fffb1f")
button.config(activebackground="red")
button.config(activeforeground="#fffb1f")
button.config(compound="bottom")
button.config(image=image)
button.config(cursor="hand2")
button.pack()

window.mainloop()
