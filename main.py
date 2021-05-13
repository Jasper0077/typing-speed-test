from tkinter import *
import re
from PIL import Image, ImageTk

BROWN = "#cc9b6d"
LIGHT_BROWN = "#f1ca89"
PEACH = "#f2dac3"
GREY = "#c8c2bc"
WHITE = "#ffffff"
FONT_NAME = "Courier"
TEXT = "this is a simple paragraph\n" \
       "that was meant to be nice\n" \
       "and easy typing which will\n" \
       "why there can have mommas\n" \
       "no periods or any\n" \
       "thus you should write\n" \
       "good plus nicely later\n" \
       "we find it easy to\n" \
       "pick up and learn\n" \
       "coding really fast for\n" \
       "real no kidding it's true"


#  ---------------- FUNC ------------------------


def check_speed():
    entry.config(state="disabled")
    texts_entry = entry.get()
    texts_list = []
    # Multiple split separator with re
    print(re.split(' |\n', texts_entry))
    print(re.split(' |\n', TEXT))
    for text_entry in re.split(' |\n', texts_entry):
        # Check if the entried text is in the TEXT file
        if text_entry in re.split(' |\n', TEXT):
            # Count the text if yes
            texts_list.append(text_entry)
    wpm = len(texts_list)
    # Output the wpm to user
    title_label.config(text=f"Your wpm is: {wpm}", font=(FONT_NAME, 30, "bold"), fg=PEACH)


def start():
    entry.config(state="normal")
    # Set timer to 60 secs
    window.after(60000, check_speed)
    # User can finish earlier before time ends and check their result.
    start_button.config(text="Done", command=check_speed)


#  --------------------- UI ---------------------
window = Tk()
window.title("Typing speed test")
window.config(padx=40, pady=30, bg=LIGHT_BROWN)
title_label = Label(text="Typing Test", font=(FONT_NAME, 35, "bold"), fg=BROWN, bg=LIGHT_BROWN)
title_label.grid(column=1, row=0)

# Read the Image
image = Image.open("eevee.png")
resize_image = image.resize((50, 50))

img = ImageTk.PhotoImage(resize_image)

# Eevee img UI
label1 = Label(image=img, bg=LIGHT_BROWN)
label1.image = img
label1.grid(column=0, row=0)

# Texts display
canvas = Canvas(height=300, width=400, bg=WHITE)
texts = canvas.create_text(200, 150, text=TEXT, fill=BROWN, justify="center", font=(FONT_NAME, 14, "bold"))
canvas.grid(column=1, row=1)

# Texts input
entry = Entry(window, width=40, bg=BROWN, fg="white", font=(FONT_NAME, 14, "bold"), state="disabled")
entry.grid(column=1, row=2)

# Button UI
start_button = Button(text="Start", padx=20, pady=15, bg=GREY, highlightthickness=0, command=start)
start_button.grid(column=1, row=3)

window.mainloop()

# text = "Hello I am Jasper. I love, coding."
# text_list = text.split(" ")
# print(text_list)
