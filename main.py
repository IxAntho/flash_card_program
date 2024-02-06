from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"

# Data functionality
data = pandas.read_csv("data/french_words.csv")
french_words_list = data["French"].to_list()
english_words_list = data["English"].to_list()

try:
    data_to_learn = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data.to_csv(path_or_buf="data/words_to_learn.csv", index=False)
    data_to_learn = pandas.read_csv("data/words_to_learn.csv")
else:
    pass


def front_card(word):
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(content_text, text=word, fill="black")
    canvas.itemconfig(card_image, image=card_front_image)


def back_card(word):
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(content_text, text=word, fill="white")
    canvas.itemconfig(card_image, image=card_back_image)


def wrong_random_words():
    num = randint(0, len(data_to_learn) - 1)
    random_pair = data_to_learn.iloc[num]
    french_word = random_pair["French"]
    english_word = random_pair["English"]
    front_card(french_word)
    canvas.after(3000, back_card, english_word)


def right_random_words():
    num = randint(0, len(data_to_learn) - 1)
    random_pair = data_to_learn.iloc[num]
    french_word = random_pair["French"]
    english_word = random_pair["English"]
    front_card(french_word)
    canvas.after(3000, back_card, english_word)
    # Remove the random pair from the DataFrame
    data_to_learn.drop(num, inplace=True)
    # Reset the index after dropping the row
    data_to_learn.reset_index(drop=True, inplace=True)
    data_to_learn.to_csv(path_or_buf="data/words_to_learn.csv", index=False)


# GUI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
content_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=wrong_random_words, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=right_random_words, highlightthickness=0,
                      highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

wrong_random_words()
window.mainloop()
