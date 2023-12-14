import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk, Image 
import pandas as pd
import random

score = 0
current_question = 0  

# Ler o arquivo xlsx
df = pd.read_excel('perguntas.xlsx')
questions = df.sample(n=10).values.tolist()

# Criando Janela
window = tk.Tk()
window.title('Quiz')
window.geometry('400x360')

# Cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#00a5a5"
button_text_color = "black"
window.config(bg=background_color)
window.option_add('*Font', 'Arial')

# Função para Verificar a resposta
def check_answer(answer):
    global score, current_question
    
    if answer == correct_answer.get():
        score += 1
    current_question += 1
    
    if current_question < len(questions):
        display_question()
    else:
        show_result()

# Função para Exibir a próxima pergunta
def display_question():
    global score, current_question
    
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))
    correct_answer.set(answer)

# Função para Exibir o Resultado final
def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz.\n\nPontuação final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()


# Função para Jogar novamente
def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    display_question()
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()
    
    

# LOGO:
img_0 = Image.open('image/log.png')
img_0 = img_0.resize((45, 45))
img_0 = ImageTk.PhotoImage(img_0)
logo_label = tk.Label(window, image=img_0, bg=background_color)
logo_label.pack(pady=10)  


# Interface:
question_label = tk.Label(window, text='', wraplength=300, bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option1_btn.pack(pady=10)

option2_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option2_btn.pack(pady=10)

option3_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option3_btn.pack(pady=10)

option4_btn = tk.Button(window, text='', width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=('Arial', 10, 'bold'))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(window, text='Jogar Novamente', width=30, bg=button_color, fg=button_text_color, command=play_again, font=('Arial', 10, 'bold'))


# Rodapé --------------------------------------------------------------
rodape_label = tk.Label(window, text='By Yury Mota', font=('Verdana 8'), bg=background_color, fg='black')
rodape_label.pack(anchor=tk.W, pady=10)


display_question()
window.mainloop()
