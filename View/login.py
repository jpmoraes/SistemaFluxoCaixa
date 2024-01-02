import tkinter as tk
from tkinter import messagebox
import menuPrincipal as mp
import Controller.login as contLog

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry('340x300+500+200')
        self.frame_login = tk.Frame(self.root)
        self.criar_tela_login()

    def criar_tela_login(self):
        label_Tela = tk.Label(
            self.root,
            text="Fluxtec",
            width=100,
            height=5,
            font=("-weight bold -size 12")
        )
        label_Tela.pack()

        label_usuario = tk.Label(self.frame_login, text="Usuário:")
        label_usuario.pack()

        self.entrada_usuario = tk.Entry(self.frame_login)
        self.entrada_usuario.pack()

        label_senha = tk.Label(self.frame_login, text="Senha:")
        label_senha.pack()

        self.entrada_senha = tk.Entry(self.frame_login, show="*")
        self.entrada_senha.pack()

        botao_login = tk.Button(self.frame_login, text="Login", command=self.verificar_login)
        botao_login.pack()

        self.frame_login.pack()

    def verificar_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        acessarLog = contLog.LoginController()        

        if  acessarLog.verify_login(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.abrir_menu_principal()
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos")

    def abrir_menu_principal(self):
        self.root.withdraw()  # Oculta a janela de login
        menu = tk.Toplevel(self.root)  # Cria uma nova janela de menu
        menu_principal = mp.MenuPrincipal(menu)  # Instancia o MenuPrincipal passando a nova janela
        menu.protocol("WM_DELETE_WINDOW", self.mostrar_janela_login)  # Define a função para voltar ao login ao fechar a janela de menu

    def mostrar_janela_login(self):
        self.root.deiconify()  # Exibe a janela de login novamente


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
