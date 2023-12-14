import pandas as pd

# Lista de Perguntas:

perguntas = [
    ["Qual é a capital da França?", "Paris", "Londres", "Berlim", "Roma", 1],
    ["Qual é o resultado de 8 + 5?", "12", "13", "15", "18", 2],
    ["Quem pintou a Mona Lisa?", "Picasso", "Da Vinci", "Van Gogh", "Warhol", 2],
    ["Quanto é 6 multiplicado por 7?", "36", "42", "48", "54", 2],
    ["Qual é o maior planeta do sistema solar?", "Marte", "Saturno", "Júpiter", "Vênus", 3],
    ["Quem escreveu a obra 'Dom Quixote'?", "Machado de Assis", "Miguel de Cervantes", "Jorge Luis Borges", "Gabriel García Márquez", 2],
    ["Qual é a fórmula química da água?", "H2O", "CO2", "NaCl", "CH4", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John F. Kennedy", 1],
    ["Qual é o resultado de 4 ao cubo?", "16", "32", "64", "128", 3],
    ["Qual é a capital da Rússia?", "Moscou", "São Petersburgo", "Kiev", "Varsóvia", 1],
    ["Quem descobriu a teoria da relatividade?", "Isaac Newton", "Galileu Galilei", "Albert Einstein", "Nikola Tesla", 3],
    ["Qual é o símbolo químico do ouro?", "Au", "Ag", "Cu", "Fe", 1],
    ["Quem foi o autor da obra 'Romeu e Julieta'?", "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen", 1],
    ["Qual é a capital do Brasil?", "Rio de Janeiro", "Brasília", "São Paulo", "Salvador", 2],
    ["Qual é o resultado de 9 dividido por 3?", "1", "2", "3", "4", 3],
    ["Quem pintou a obra 'A Noite Estrelada'?", "Leonardo da Vinci", "Michelangelo", "Salvador Dalí", "Vincent van Gogh", 4],
    ["Qual é o maior oceano do mundo?", "Atlântico", "Índico", "Pacífico", "Ártico", 3],
    ["Qual é o resultado de 2 elevado a 8?", "8", "16", "64", "256", 4],
    ["Quem escreveu a obra '1984'?", "George Orwell", "Aldous Huxley", "Ernest Hemingway", "F. Scott Fitzgerald", 1],
    ["Qual é o resultado de 15 menos 7?", "5", "6", "7", "8", 3],
    ["Quem foi o pintor do quadro 'A Última Ceia'?", "Pablo Picasso", "Salvador Dalí", "Michelangelo", "Leonardo da Vinci", 4],
    ["Qual é a capital da Alemanha?", "Berlim", "Munique", "Frankfurt", "Hamburgo", 1],
    ["Quem é o autor de 'O Pequeno Príncipe'?", "Antoine de Saint-Exupéry", "J.K. Rowling", "Charles Dickens", "Jane Austen", 3],
    ["Qual é o elemento mais abundante na crosta terrestre?", "Oxigênio", "Silício", "Ferro", "Alumínio", 4],
    ["Quem escreveu 'Cem Anos de Solidão'?", "Gabriel García Márquez", "Mario Vargas Llosa", "Isabel Allende", "Julio Cortázar", 2],
    ["Quem foi o fundador da Microsoft?", "Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Larry Page", 4],
    ["Quem é a autora de 'Orgulho e Preconceito'?", "Jane Austen", "Charlotte Brontë", "Emily Brontë", "Virginia Woolf", 3],
    ["Quem foi o líder sul-africano que lutou contra o apartheid?", "Nelson Mandela", "Desmond Tutu", "F.W. de Klerk", "Steve Biko", 4],
    ["Qual é o país mais populoso do mundo?", "China", "Índia", "Estados Unidos", "Brasil", 3],
    ["Quem é o autor de 'Crime e Castigo'?", "Fiódor Dostoiévski", "Lev Tolstói", "Anton Tchekhov", "Ivan Turguêniev", 4],
    ["Qual é a capital da Austrália?", "Camberra", "Sydney", "Melbourne", "Brisbane", 3],
    ["Quem é considerado o pai da filosofia ocidental?", "Sócrates", "Platão", "Aristóteles", "Heráclito", 1],
    ["Em que ano começou a Primeira Guerra Mundial?", "1914", "1916", "1918", "1920", 1],
    ["Qual é o segundo maior planeta do sistema solar?", "Júpiter", "Saturno", "Netuno", "Urano", 2],
    ["Quem é o autor de 'O Senhor dos Anéis'?", "J.K. Rowling", "C.S. Lewis", "J.R.R. Tolkien", "George R.R. Martin", 3],
    ["Qual é o maior deserto do mundo?", "Deserto do Saara", "Deserto da Arábia", "Deserto do Gobi", "Deserto do Atacama", 1],
    ["Quem foi o primeiro ser humano a ir ao espaço?", "Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Valentina Tereshkova", 1],
    ["Qual é o elemento mais leve da tabela periódica?", "Hidrogênio", "Hélio", "Lítio", "Oxigênio", 1],
    ["Quem pintou 'Guernica'?", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet", 1],
    ["Em que ano ocorreu a Revolução Francesa?", "1789", "1801", "1824", "1840", 1],
    ["Qual é o livro mais vendido de todos os tempos?", "A Bíblia", "Dom Quixote", "Harry Potter e a Pedra Filosofal", "O Alquimista", 1],
    
]

# Cria um DataFrame do pandas:
df = pd.DataFrame(perguntas, columns=["Pergunta", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

# Salva no arquivo do excel

df.to_excel("perguntas.xlsx", index=False)

print("Perguntas inseridas com sucesso no arquivo questions.xlsx!")