# main.py
import tkinter as tk
from quiz_functions import QuizGame
import pandas as pd

# Ler o arquivo xlsx
df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

# Criando Janela
window = tk.Tk()
window.title('Quiz')
window.geometry('400x450')

quiz_game = QuizGame(window, questions)

window.mainloop()