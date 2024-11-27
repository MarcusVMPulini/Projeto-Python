from tkinter import Label, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import database
import sqlite3

login = ctk.CTk()
login.geometry("960x540")
login.title('Login')
login.resizable(False, False)

ctk.set_appearance_mode("dark")

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('mystery_cars_real1.db')  # Update with your actual database path
        self.cursor = self.conn.cursor()

    def ensure_connection(self):
        # No need to check for closed, just return if already connected
        if self.conn is None:
            self.conn = sqlite3.connect('mystery_cars_real1.db')
            self.cursor = self.conn.cursor()

# Create a global instance of the database
database = Database()

def teloguei():
    email = label_email.get()
    password = label_senha.get()

    try:
        # Ensure the connection is open
        database.ensure_connection()

        # Execute the login query
        database.cursor.execute(""" 
        SELECT * FROM Users WHERE email = ? AND password = ?
        """, (email, password))
        
        VerifyLogin = database.cursor.fetchone()
        
        if VerifyLogin:
            db_email, db_password = VerifyLogin[2], VerifyLogin[3]  # Assuming index 1 is email and 2 is password
            if email == db_email and password == db_password:
                messagebox.showinfo("Login", "Login realizado com sucesso")
                login.destroy()
            else:
                messagebox.showerror("Login", "Email ou senha incorretos")
        else:
            messagebox.showerror("Login", "Email ou senha incorretos")

    except sqlite3.Error as e:
        messagebox.showerror("Erro no banco de dados", str(e))
    except Exception as e:
        messagebox.showerror("Erro", str(e))



def tecadastrei():
    nome = label_nome.get()
    email = label_email.get()
    password = label_senha.get()

    if (nome == '' and email == '' and password == ''):
        messagebox.showerror(title="Error", message="Preencha todos os campos")
        


    try:
        # Attempt to execute a command
        database.cursor.execute("""
            INSERT INTO Users (name, email, password) VALUES (?, ?, ?)
        """, (nome, email, password))
        database.conn.commit()
        messagebox.showinfo(title="Informação de cadastro", message="Cadastro realizado com sucesso!")

    except sqlite3.ProgrammingError as e:
        # Handle the case where the database connection is closed
        if "closed" in str(e):
            # Reconnect to the database
            database.conn = sqlite3.connect('mystery_cars_real1.db')  # Update with your actual path
            database.cursor = database.conn.cursor()
            # Retry the insert operation
            database.cursor.execute("""
                INSERT INTO Users (nome, email, password) VALUES (?, ?, ?)
            """, (nome, email, password))
            database.conn.commit()
            messagebox.showinfo(title="Informação de cadastro", message="Cadastro realizado com sucesso!")
        else:
            # For other programming errors, show the error
            messagebox.showerror("Erro", str(e))

    except Exception as e:
        # Handle any other exceptions
        messagebox.showerror("Erro", str(e))



def logar():

    

        
    button_cliqueaqui.place_forget()
    button_cliqueaqui.grid_forget()
    botao_cadastrar.place_forget()
    botao_cadastrar.grid_forget()
    label_clique_aqui.configure(text='Se não tem uma conta,')
    label_clique_aqui.place(rely=0.54, relx=0.387)
    label_nome.place(x=50000)
    botao_login = ctk.CTkButton(frame_login, text="Login", bg_color='red', fg_color='red', hover_color='#A80101', command=teloguei)
    botao_login.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    label_email.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
    label_senha.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
    escrito_login.configure(text=" LOGIN ")
    escrito_login.place(relx=0.495, rely=0.2, anchor=ctk.CENTER)
    

    def voltar():
        
        botao_login.place_forget()
        button_cliqueaqui2.place_forget()

        button_cliqueaqui = ctk.CTkButton(frame_login, text="Clique aqui", fg_color='#1D1919', hover_color='#1D1919', font=ctk.CTkFont(family="Formula1 Display Bold", size=10, slant="italic"), command=logar, width=2)
        button_cliqueaqui.place(relx = 0.52, rely = 0.612)

        escrito_login.configure(text="CADASTRAR")

        label_nome.grid(row=1, column=0, padx=400, pady=(150, 0), sticky="n")

        label_email.grid(row=2, column=0, padx=160, pady=(15, 0), sticky="n")

        label_senha.grid(row=3, column=0, padx=160, pady=(15, 0), sticky="n")


        botao_cadastrar.configure(text='Cadastrar')
        botao_cadastrar.grid(row=5, column=0, padx=160, pady=(20, 0))

 

        label_clique_aqui.configure(text='Se ja tem uma conta,')
        label_clique_aqui.place(relx = 0.397, rely = 0.61)

    button_cliqueaqui2 = ctk.CTkButton(frame_login, text="Clique aqui", fg_color='#1D1919', hover_color='#1D1919', font=ctk.CTkFont(family="Formula1 Display Bold", size=10, slant="italic"), width=17, command=voltar)
    button_cliqueaqui2.place(rely=0.543, relx=0.521)
    
    
    

    


    


#    Configura a coluna 0 para ter uma largura fixa
login.grid_columnconfigure(0, weight=0)


# Frame para o login
frame_login = ctk.CTkFrame(login, width=576, height=540, fg_color='#1D1919')
frame_login.grid(row=0, column=1,sticky="nsew")  # Expande o frame para a coluna 1

# Configura a coluna 1 para expandir e preencher o espaço restante
login.grid_columnconfigure(1, weight=1)

button_cliqueaqui = ctk.CTkButton(frame_login, text="Clique aqui", fg_color='#1D1919', hover_color='#1D1919', font=ctk.CTkFont(family="Formula1 Display Bold", size=10, slant="italic"), command=logar)
button_cliqueaqui.place(relx = 0.484, rely = 0.612)

escrito_login = ctk.CTkLabel(frame_login, text='CRIAR CONTA', font=ctk.CTkFont(family="Formula1 Display Bold", size=30, slant="italic"), text_color='white')
escrito_login.grid(row=0, column=0, padx=355, pady=(55,0), sticky="n")

label_nome = ctk.CTkEntry(frame_login, placeholder_text="Nome")
label_nome.grid(row=1, column=0, padx=160, pady=(70, 0), sticky="n")

label_email = ctk.CTkEntry(frame_login, placeholder_text="Email")
label_email.grid(row=2, column=0, padx=160, pady=(15, 0), sticky="n")

label_senha = ctk.CTkEntry(frame_login, placeholder_text="Senha", show='•')
label_senha.grid(row=3, column=0, padx=160, pady=(15, 0), sticky="n")

botao_cadastrar = ctk.CTkButton(frame_login, text="Cadastrar", bg_color='red', fg_color='red', hover_color='#A80101', command=tecadastrei)
botao_cadastrar.grid(row=5, column=0, padx=160, pady=(20, 0))

label_clique_aqui = ctk.CTkLabel(frame_login, text='Se ja tem uma conta,', font=ctk.CTkFont(family="Formula1 Display Regular", size=10, slant="italic"), )
label_clique_aqui.place(relx = 0.397, rely = 0.61)




# Configura a linha 0 para ter o peso apropriado para expandir o conteúdo
login.grid_rowconfigure(0, weight=1)
login.mainloop()