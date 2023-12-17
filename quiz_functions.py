import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random


class QuizGame:
    def __init__(self, window, questions):
        self.window = window
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.lives = 3
        self.help_used = False # Variável do 50:50
        self.skip_used = False  # Variável do Pular

        # Adiciona o caminho das imagens dos corações
        self.hearts_full_img = ImageTk.PhotoImage(Image.open('image/coracao-cheio.jpg').resize((30, 30)))
        self.hearts_empty_img = ImageTk.PhotoImage(Image.open('image/coracao-vazio.jpg').resize((30, 30)))

        # Cria uma lista para armazenar os Labels dos corações
        self.hearts_labels = []
        for _ in range(3):
            heart_label = tk.Label(window, image=self.hearts_full_img)
            self.hearts_labels.append(heart_label)

        # Posiciona os corações na parte superior direita da janela
        for i, heart_label in enumerate(self.hearts_labels):
            heart_label.place(relx=1.0, rely=0, anchor=tk.NE, x=-30 - i * 30, y=10)

        # Adiciona o caminho da imagem do logo
        self.logo_img = ImageTk.PhotoImage(Image.open('image/log.png').resize((45, 45)))
        logo_label = tk.Label(window, image=self.logo_img, bg='#ECECEC')
        logo_label.pack(pady=10)

        # Restante da inicialização...
        self.question_label = tk.Label(window, text='', wraplength=300, bg='#ECECEC', fg='#333333', font=('Arial', 12, 'bold'))
        self.question_label.pack(pady=20)

        self.correct_answer = tk.IntVar()

        self.option1_btn = tk.Button(window, text='', width=30, bg='#3498db', fg='#FFFFFF', state=tk.DISABLED, font=('Arial', 10, 'bold'))
        self.option1_btn.pack(pady=10)

        self.option2_btn = tk.Button(window, text='', width=30, bg='#3498db', fg='#FFFFFF', state=tk.DISABLED, font=('Arial', 10, 'bold'))
        self.option2_btn.pack(pady=10)

        self.option3_btn = tk.Button(window, text='', width=30, bg='#3498db', fg='#FFFFFF', state=tk.DISABLED, font=('Arial', 10, 'bold'))
        self.option3_btn.pack(pady=10)

        self.option4_btn = tk.Button(window, text='', width=30, bg='#3498db', fg='#FFFFFF', state=tk.DISABLED, font=('Arial', 10, 'bold'))
        self.option4_btn.pack(pady=10)

        # Botão 50:50    
        self.help_btn = tk.Button(window, text='50:50', width=9, height=2, bg='#3498db', fg='#FFFFFF', command=self.use_help, font=('Arial', 10, 'bold'))
        self.help_btn.place(relx=0.35, rely=0.78, anchor=tk.NE)

        # Botão Pular
        self.skip_btn = tk.Button(window, text='Pular', width=9, height=2, bg='#3498db', fg='#FFFFFF', command=self.skip_question, font=('Arial', 10, 'bold'))
        self.skip_btn.place(relx=0.57, rely=0.78, anchor=tk.NE)

        self.play_again_btn = tk.Button(window, text='Jogar Novamente', width=30, bg='#4CAF50', fg='#FFFFFF', command=self.play_again, font=('Arial', 10, 'bold'))

        self.display_question()

    def update_hearts(self):
        for i, heart_label in enumerate(self.hearts_labels):
            if i < self.lives:
                heart_label.config(image=self.hearts_full_img)
            else:
                heart_label.config(image=self.hearts_empty_img)

    def check_answer(self, answer):
        if answer == self.correct_answer.get():
            self.score += 1
        else:
            self.lives -= 1
            self.update_hearts()
            if self.lives == 0:
                self.show_result("Você perdeu todas as vidas!")
                return

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result(f"Parabéns! Você completou o quiz.\n\nPontuação final: {self.score}/{len(self.questions)}")

    def display_question(self):
        question, option1, option2, option3, option4, answer = self.questions[self.current_question]
        self.question_label.config(text=question)
        self.option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: self.check_answer(1))
        self.option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: self.check_answer(2))
        self.option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: self.check_answer(3))
        self.option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: self.check_answer(4))
        self.correct_answer.set(answer)

    def show_result(self, message):
        messagebox.showinfo("Quiz Finalizado", message)
        self.option1_btn.config(state=tk.DISABLED)
        self.option2_btn.config(state=tk.DISABLED)
        self.option3_btn.config(state=tk.DISABLED)
        self.option4_btn.config(state=tk.DISABLED)
        self.play_again_btn.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.help_used = False
        self.skip_used = False  # Reinicia a variável de pulo
        self.lives = 3
        self.update_hearts()
        random.shuffle(self.questions)
        self.display_question()

        self.option1_btn.config(state=tk.NORMAL)
        self.option2_btn.config(state=tk.NORMAL)
        self.option3_btn.config(state=tk.NORMAL)
        self.option4_btn.config(state=tk.NORMAL)

        self.help_btn.config(state=tk.NORMAL)
        self.skip_btn.config(state=tk.NORMAL)  # Habilita o botão de pular novamente

        self.play_again_btn.place_forget()

    def use_help(self):
        if not self.help_used:
            incorrect_options = [self.option1_btn, self.option2_btn, self.option3_btn, self.option4_btn]
            correct_answer_index = self.correct_answer.get() - 1
            incorrect_options.pop(correct_answer_index)
            incorrect_options.pop(random.choice(range(len(incorrect_options))))

            for btn in incorrect_options:
                btn.config(state=tk.DISABLED)

            self.help_used = True
            self.help_btn.config(state=tk.DISABLED)
            

    def skip_question(self):
        if not self.skip_used:
            self.current_question += 1
            self.display_question()
            self.skip_used = True
            self.skip_btn.config(state=tk.DISABLED)  # Desabilita o botão de pular após o uso
