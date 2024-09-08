import tkinter as tk
import pandas as pd
import os

german_word = ""
english_translation = ""
timer_id = None

BACKGROUND_COLOR = "#B1DDC6"
learned_file_path = "./data/learned_words.csv"


def chose_word():
    global german_word
    global english_translation
    if data.empty:
        # No more words left in the original data
        return
    random_entry = data.sample().iloc[0]  # Select a random row
    german_word = random_entry['german']
    english_translation = random_entry['english']
    canvas.itemconfig(word_text, text=german_word, fill="black")
    canvas.itemconfig(language_text, text="German", fill="black")
    canvas.itemconfig(card, image=image_front)


def flip_positive():
    image_back = tk.PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(card, image=image_back)
    canvas.image = image_back  # Keep a reference to avoid garbage collection
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_translation, fill="white")
    canvas.update()


def learned():
    global data
    global learned_words

    # Save the learned word to the learned_words DataFrame
    learned_words = pd.concat(
        [learned_words, pd.DataFrame({'german': [german_word], 'english': [english_translation]})], ignore_index=True)

    # Remove the learned word from the original data
    data = data[~((data['german'] == german_word) & (data['english'] == english_translation))]

    # Save the updated DataFrames to their respective files
    data.to_csv("./data/de.csv", index=False)
    learned_words.to_csv(learned_file_path, index=False)

    chose_word()



# Set up the UI
window = tk.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = tk.Canvas(window, height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
image_front = tk.PhotoImage(file="./images/card_front.png")
card = canvas.create_image(410, 263, image=image_front)
canvas.grid(column=0, row=0, columnspan=3)
language_text = canvas.create_text(410, 160, text="German", fill="black", font=("Arial", 28, "italic"))

image_right = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(window, image=image_right, command=learned, highlightthickness=0, borderwidth=0)
right_button.grid(column=2, row=1)

image_flip = tk.PhotoImage(file="./images/flip.png")
flip_button = tk.Button(window, image=image_flip, command=flip_positive, bg=BACKGROUND_COLOR, highlightthickness=0,
                        borderwidth=0)
flip_button.grid(column=1, row=1)

image_wrong = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(window, image=image_wrong, command=chose_word, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)

word_text = canvas.create_text(410, 263, text="", fill="black", font=("Arial", 50, "bold"))

# Load data
data = pd.read_csv("./data/de.csv")

# Check if the learned_words file exists, otherwise create an empty DataFrame
if os.path.exists(learned_file_path):
    learned_words = pd.read_csv(learned_file_path)
else:
    learned_words = pd.DataFrame(columns=['german', 'english'])

# Start with a new card
chose_word()

# Start the Tkinter event loop
window.mainloop()
