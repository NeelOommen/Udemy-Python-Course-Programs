BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

dict_data = data.to_dict(orient='records')
current_card = {}

def next_card():
    global current_card, flip_timer
    current_card = random.choice(dict_data)
    window.after_cancel(flip_timer)
    #french section
    canvas.itemconfig(canvas_bg, image=card_front_data)
    canvas.itemconfig(card_title, fill='black', text='French')
    canvas.itemconfig(card_value, fill='black',text=current_card['French'])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    #english section
    canvas.itemconfig(canvas_bg, image=card_back_data)
    canvas.itemconfig(card_title, fill='white', text='English')
    canvas.itemconfig(card_value, fill='white', text=current_card['English'])


def is_known():
    dict_data.remove(current_card)
    t_data = pandas.DataFrame(dict_data)
    t_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Flash Cards')
window.config(bg = BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_data = PhotoImage(file='images/card_front.png')
card_back_data = PhotoImage(file='images/card_back.png')
canvas_bg = canvas.create_image(400, 269, image=card_front_data)
card_title = canvas.create_text(400, 150, text='', fill='black', font=('Ariel', 40, 'italic'))
card_value = canvas.create_text(400, 263, text='', fill='black', font=('Ariel', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

incorrect_button_image = PhotoImage(file='images/wrong.png')
incorrect_button = Button(image=incorrect_button_image, highlightthickness=0, command=next_card)
incorrect_button.grid(row=1, column=0)

correct_button_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_button_image, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()