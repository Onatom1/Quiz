import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
import random



# Inicializações
score = 0
current_question = 0
lives = 3  # Vidas
help_used = False  # 50:50
skip_used = False  # Variável do Pular

# Ler o arquivo xlsx
df = pd.read_excel('Perguntas.xlsx')
questions = df.sample(n=10).values.tolist()

# Criando Janela
window = tk.Tk()
window.title('Quiz')
window.geometry('400x450')

# Cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#3498db"
button_text_color = "#FFFFFF"
window.config(bg=background_color)
window.option_add('*Font', 'Arial')

# Adiciona o caminho das imagens dos corações
hearts_full_img = ImageTk.PhotoImage(Image.open('image/coracao-cheio.jpg').resize((30, 30)))
hearts_empty_img = ImageTk.PhotoImage(Image.open('image/coracao-vazio.jpg').resize((30, 30)))

# Cria uma lista para armazenar os Labels dos corações
hearts_labels = []

# Inicialmente, exibe os três corações cheios
for _ in range(3):
    heart_label = tk.Label(window, image=hearts_full_img, bg=background_color)
    hearts_labels.append(heart_label)

# Posiciona os corações na parte superior direita da janela
for i, heart_label in enumerate(hearts_labels):
    heart_label.place(relx=1.0, rely=0, anchor=tk.NE, x=-30 - i * 30, y=10)


# Função para atualizar a exibição dos corações
def update_hearts():
    # Atualiza os corações de acordo com a quantidade de vidas restantes
    for i, heart_label in enumerate(hearts_labels):
        if i < lives:
            heart_label.config(image=hearts_full_img)
        else:
            heart_label.config(image=hearts_empty_img)


# Função para Verificar a resposta
def check_answer(answer):
    global score, current_question, lives

    if answer == correct_answer.get():
        score += 1
    else:
        lives -= 1
        update_hearts()  # Atualiza os corações após perder uma vida
        if lives == 0:
            show_result("Você perdeu todas as vidas!")  # Mensagem personalizada para quando todas as vidas são perdidas
            return

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result(f"Parabéns! Você completou o quiz.\n\nPontuação final: {score}/{len(questions)}")


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
def show_result(message):
    messagebox.showinfo("Quiz Finalizado", message)
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    # Posição do botão "Jogar Novamente"
    play_again_btn.place(relx=0.5, rely=0.95, anchor=tk.CENTER)  # Exibe o botão "Jogar Novamente"
    



# Função para Jogar novamente
def play_again():
    global score, current_question, lives, help_used, skip_used
    score = 0
    current_question = 0
    help_used = False  # Reinicia a variável do 50:50 usada
    skip_used = False  # Reinicia a variável de pular usada
    lives = 3  # Reinicia o número de vidas
    update_hearts()  # Atualiza a exibição dos corações
    random.shuffle(questions)
    display_question()

    # Reconfigura todos os botões de opção para o estado normal
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)

    # Reconfigura o botão de ajuda para o estado normal
    help_btn.config(state=tk.NORMAL)
    skip_btn.config(state=tk.NORMAL)

    play_again_btn.place_forget()  # Oculta o botão "Jogar Novamente"
    
    
def use_help():
    global help_used

    if not help_used:
        # Desabilita temporariamente os botões das opções incorretas
        incorrect_options = [option1_btn, option2_btn, option3_btn, option4_btn]
        correct_answer_index = correct_answer.get() - 1  # Índice da resposta correta (0-based)

        # Remove duas opções incorretas (se houver mais de duas)
        incorrect_options.pop(correct_answer_index)
        incorrect_options.pop(random.choice(range(len(incorrect_options))))

        for btn in incorrect_options:
            btn.config(state=tk.DISABLED)

        # Atualiza a variável de controle
        help_used = True

        # Desabilita o botão de ajuda até o final do jogo
        help_btn.config(state=tk.DISABLED)
        

def skip_question():
    global current_question, skip_used
    if not skip_used:
        current_question += 1
        display_question()
        skip_used = True
        skip_btn.config(state=tk.DISABLED)  # Desabilita o botão de pular após o uso

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

help_btn = tk.Button(window, text='50:50', width=9, height=2, bg=button_color, fg=button_text_color, command=use_help, font=('Arial', 10, 'bold'))
help_btn.place(relx=0.35, rely=0.78, anchor=tk.NE)

skip_btn = tk.Button(window, text='Pular', width=9, height=2, bg=button_color, fg=button_text_color, command=skip_question, font=('Arial', 10, 'bold'))
skip_btn.place(relx=0.57, rely=0.78, anchor=tk.NE)

play_again_btn = tk.Button(window, text='Jogar Novamente', width=30, bg='#4CAF50', fg=button_text_color, command=play_again, font=('Arial', 10, 'bold'))


# Rodapé --------------------------------------------------------------
rodape_label = tk.Label(window, text='By Yury Mota', font=('Verdana 6'), bg=background_color, fg='#000000')
rodape_label.place(relx=0.10, rely=0.95, anchor=tk.N)

display_question()
window.mainloop()