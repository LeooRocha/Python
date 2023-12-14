import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Função dos botões
def funcao_clicar():
    print("Você clicou no botão")

def funcao_abrir():
    pass

# Caixas de Diálogo:
'''def mensagem():
    messagebox.showinfo("Título", "Estou aprendendo Python!")
'''
# Cria uma janela
janela = tk.Tk()
janela.title("Exemplo Tkinter")

# Cria um Menu
menu_bar = tk.Menu()
janela.config(menu=menu_bar)

file_menu= tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Abrir", command=funcao_abrir)

# Cria um rótulo "Usuário"
label = tk.Label(janela,text="Usuário")
label.pack()

# Criar uma área para inserir texto
entrada_txt = tk.Entry(janela, width=10)
entrada_txt.pack()

# Criar outro label
lbl_senha = tk.Label(janela, width=10, text="Senha")
lbl_senha.pack()

# Cria uma entrada para digitar a senha
txt_senha = tk.Entry(janela, width=10, )
txt_senha.pack()

# Cria um Botão
botao = tk.Button(janela, text="Login", command = funcao_clicar())
botao.pack()

# Aplica estilo ao botão
'''estilo = ttk.Style("TButto", foreground="green", padding=(10,10))
estilo.configure("TButton", font=("Arial", 12, "bold"))'''

# Aplica estilo ao Labbel
'''estilo=ttk.Style()
estilo.configure("TLabel", foreground="green", padding=(10,10), font=("Arial", 12, "bold"))'''

janela.mainloop()
