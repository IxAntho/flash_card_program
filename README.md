# Flashy - French Flashcard Program

---

## Description

Flashy is a simple flashcard program designed to aid users in studying the 100 most common French words. It presents users with French words on one side of the flashcard and their corresponding English translations on the other side. The program allows users to test their knowledge by flipping the flashcards and indicating whether they've remembered the correct translation or not.

---

## Features

1. **Flashcard Display:** The program displays flashcards with French words on the front and their English translations on the back.
2. **Interactive Buttons:** Users can interact with the flashcards by clicking on buttons to indicate whether they've remembered the correct translation.
3. **Random Word Selection:** Flashy randomly selects words from a predefined list of 100 common French words for users to study.
4. **Data Persistence:** The program saves user progress by storing words that need further practice in a CSV file (`words_to_learn.csv`). This file ensures that users continue to study the words they find challenging.

---

## Instructions for Use

1. **Launching the Program:** Run the program by executing the Python script (`flashy.py`).
2. **Flashcard Display:** Upon launching, the program displays a flashcard with a French word on the front.
3. **Flipping the Card:** Click on the flashcard to flip it and reveal the English translation on the back.
4. **Feedback Buttons:** Use the "Wrong" or "Right" buttons to indicate whether you've remembered the correct translation.
5. **Progress Tracking:** The program automatically removes words from the list once they've been correctly translated, ensuring that users focus on words that require further practice.
6. **Exiting the Program:** Close the program window to exit.

---

## Requirements

- Python 3.x
- Tkinter library
- Pandas library

Ensure that all required dependencies are installed before running the program.

---

## Files Included

1. `flashy.py`: Python script containing the main program code.
2. `data/french_words.csv`: CSV file containing the list of 100 common French words and their English translations.
3. `data/words_to_learn.csv`: CSV file for storing words that require further practice.
4. `images/`: Directory containing image files used for the flashcard interface.

---

## Note

- Ensure that the CSV files (`french_words.csv` and `words_to_learn.csv`) are placed in the `data/` directory relative to the Python script.
- Make sure that the image files (`card_back.png`, `card_front.png`, `wrong.png`, and `right.png`) are available in the `images/` directory relative to the Python script.

---

## Acknowledgments

- This program utilizes the Tkinter library for GUI development and the Pandas library for data manipulation.
- The French word list used in this program is sourced from a curated list of common French vocabulary.

---

## Author

Anthony Barrios

---

## Contact

For any inquiries or feedback, please contact isabar735@icloud.com.

