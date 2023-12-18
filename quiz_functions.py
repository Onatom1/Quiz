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
        self.help_used = False  # Variável do 50:50
        self.skip_used = False  # Variável do Pular
        self.hint_used = False  # Variável da Dica

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

        # Restante da inicialização
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
        self.help_btn = tk.Button(window, text='50:50', width=8, height=1, bg='#3498db', fg='#FFFFFF', command=self.use_help, font=('Arial', 10, 'bold'))
        self.help_btn.place(relx=0.37, rely=0.81, anchor=tk.NE)

        # Botão Pular
        self.skip_btn = tk.Button(window, text='Pular', width=8, height=1, bg='#3498db', fg='#FFFFFF', command=self.skip_question, font=('Arial', 10, 'bold'))
        self.skip_btn.place(relx=0.59, rely=0.81, anchor=tk.NE)

        # Botão Dica
        self.hint_btn = tk.Button(window, text='Dica', width=8, height=1, bg='#3498db', fg='#FFFFFF', command=self.use_hint, font=('Arial', 10, 'bold'))
        self.hint_btn.place(relx=0.81, rely=0.81, anchor=tk.NE)

        # Adiciona um Label para exibir a dica
        self.hint_label = tk.Label(window, text='', font=('Arial', 50, 'italic'), wraplength=300)

        self.play_again_btn = tk.Button(window, text='Jogar Novamente', width=30, bg='#4CAF50', fg='#FFFFFF', command=self.play_again, font=('Arial', 10, 'bold'))

        self.display_question()

        # Rodapé --------------------------------------------------------------
        self.rodape_label = tk.Label(window, text='By Yury Mota', font=('Verdana 6'), bg='#FFFFFF', fg='#000000')
        self.rodape_label.place(relx=0.10, rely=0.95, anchor=tk.N)

# Função para atualizar a exibição dos corações
    def update_hearts(self):
        for i, heart_label in enumerate(self.hearts_labels):
            if i < self.lives:
                heart_label.config(image=self.hearts_full_img)
            else:
                heart_label.config(image=self.hearts_empty_img)

# Função para Verificar a resposta
    def check_answer(self, answer):
        if answer == self.correct_answer.get():
            self.score += 1
        else:
            self.lives -= 1
            self.update_hearts()  # Atualiza os corações depois de perder uma vida
            if self.lives == 0:
                self.show_result("Você perdeu todas as vidas!") # Mensagem para quando todas as vidas são perdidas
                return

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result(f"Parabéns! Você completou o quiz.\n\nPontuação final: {self.score}/{len(self.questions)}")

# Função para Exibir a próxima pergunta
    def display_question(self):
        question, option1, option2, option3, option4, answer, hint = self.questions[self.current_question]
        # Oculta a dica antes de exibir a próxima pergunta
        self.hint_label.place_forget()
        self.question_label.config(text=question)
        self.option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: self.check_answer(1))
        self.option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: self.check_answer(2))
        self.option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: self.check_answer(3))
        self.option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: self.check_answer(4))
        self.correct_answer.set(answer)

# Função para Exibir o Resultado final
    def show_result(self, message):
        messagebox.showinfo("Quiz Finalizado", message)
        self.option1_btn.config(state=tk.DISABLED)
        self.option2_btn.config(state=tk.DISABLED)
        self.option3_btn.config(state=tk.DISABLED)
        self.option4_btn.config(state=tk.DISABLED)
        self.hint_label.place_forget()  # Oculta o Label da dica

        # Posicionamento do botão "Jogar Novamente"
        self.play_again_btn.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# Função para Jogar novamente
    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.help_used = False  # Reinicia a variável do 50:50 usada
        self.skip_used = False  # Reinicia a variável de pulo
        self.hint_used = False  # Reinicia a variável de dica usada
        self.lives = 3          # Reinicia o número de vidas
        self.update_hearts()    # Atualiza a exibição dos corações
        random.shuffle(self.questions) # Embaralha as perguntas
        self.display_question()

        # Reconfigura todos os botões de opção para o estado normal
        self.option1_btn.config(state=tk.NORMAL)
        self.option2_btn.config(state=tk.NORMAL)
        self.option3_btn.config(state=tk.NORMAL)
        self.option4_btn.config(state=tk.NORMAL)

        # Reconfigura os botões de ajuda para o estado normal
        self.help_btn.config(state=tk.NORMAL)
        self.skip_btn.config(state=tk.NORMAL)  
        self.hint_btn.config(state=tk.NORMAL)

        self.play_again_btn.place_forget() # Oculta o botão "Jogar Novamente"

    # Função 50:50
    def use_help(self):
        if not self.help_used:
            # Desabilita temporariamente os botões das opções incorretas
            incorrect_options = [self.option1_btn, self.option2_btn, self.option3_btn, self.option4_btn]
            correct_answer_index = self.correct_answer.get() - 1 # Índice da resposta correta
            
            # Remove duas opções incorretas
            incorrect_options.pop(correct_answer_index)
            incorrect_options.pop(random.choice(range(len(incorrect_options))))

            # Desabilita os botões
            for btn in incorrect_options:
                btn.config(state=tk.DISABLED)

            # Atualiza a variável de controle
            self.help_used = True
            # Desabilita o botão de ajuda até o final do jogo
            self.help_btn.config(state=tk.DISABLED)

    # Função de pular pergunta:
    def skip_question(self):
        if not self.skip_used:
            self.current_question += 1
            self.display_question()
            self.skip_used = True
            self.skip_btn.config(state=tk.DISABLED)  # Desabilita o botão de pular após o uso

    # Função de dica
    def use_hint(self):
        if not self.hint_used:
            self.hint_used = True
            self.hint_btn.config(state=tk.DISABLED) # Desabilita o botão de dica após o uso
            self.hint_label.config(text=f'{self.questions[self.current_question][6]}', font=('Arial', 10, 'italic'), wraplength=300) # Exibe a dica
            self.hint_label.place(relx=0.5, rely=0.7, anchor=tk.N, y=20) # Posicionamento
            self.window.after(10000, self.hide_hint) # Oculta a dica automaticamente após 10 segundos

# Função para ocultar automaticamente a dica após 10 segundos
    def hide_hint(self):
        self.hint_label.place_forget()  # Oculta o Label da dica