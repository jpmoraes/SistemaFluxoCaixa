import tkinter as tk
from tkinter import messagebox
import login

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")

        self.frame_menu = tk.Frame(self.root)
        self.criar_tela_Menu()


    def criar_tela_Menu(self): 
       botao_voltar = tk.Button(self.root, text="Voltar", command=self.voltar_para_login)
       botao_voltar.pack()

       label_Tela = tk.Label(self.root, 
                            text="Seja Bem-Vindo ao Fluxtec",
                            width=100,
                            height=5,
                            font=("-weight bold -size 12")
                            )
       label_Tela.pack()
        

    def voltar_para_login(self):
        self.root.destroy()

        # Mostrar a tela de login novamente
        login_window = tk.Tk()
        app_login = login.Login(login_window)
        login_window.mainloop()