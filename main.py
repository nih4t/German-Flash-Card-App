from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
image_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(410, 263, image=image_front)
canvas.pack()

window.mainloop()
