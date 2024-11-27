
from tkinter import Label
from PIL import Image, ImageTk
import customtkinter as ctk
from customtkinter import CTkImage
import sqlite3
import random
from tkinter import messagebox
import io
import database

def func_login():
    import login1

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("1920x1080")
app.title('Mystery Cars')

#--------------------------------------------------------------------------------#
pessoa_foto = None
contador_tentativas = 0
imagens = []
def obter_pessoa_aleatoria(): 
    global pessoa_foto, imagens
    conn = sqlite3.connect('mystery_cars_real1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pilotos")
    pessoas = cursor.fetchall()
    pessoa_foto = random.choice(pessoas)
    print(pessoa_foto)
    id_piloto = pessoa_foto[0]
    cursor.execute("SELECT * FROM pilotos_jogo WHERE id = ?", (id_piloto,))
    imagens = cursor.fetchall()
    conn.close()
    return pessoa_foto

def mostrar_imagem(blob):
    if blob:
        image = Image.open(io.BytesIO(blob))
        image = image.resize((35, 35), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)
    return None



 
 
def comparar_pessoa():
    global pessoa_foto
    nome_digitado = entry_tentativa.get().strip()
        
    conn = sqlite3.connect('mystery_cars_real1.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM pilotos WHERE LOWER(nome) = LOWER(?)", (nome_digitado,))
    resultado = cursor.fetchone()
    
    print(f"Resultado da consulta: {resultado}")
 
    if resultado:


        id, nome, foto, equipe_blob, nacionalidade_blob, idade, ultima_temporada = resultado
 
        resultado_text = ""
        cor_letra =  "green"
        cor_fundo = "green"  
        cor_fundo_temp = "green"
        cor_fundo_equipe = "green"
        cor_fundo_nacionalidade = "green"
        cor_fundo_idade = "green"

        if nome == pessoa_foto[1]:
            resultado_text += "Nome correto! "

        else:
            resultado_text += "Nome incorreto. "
            cor_fundo = "red"
            cor_letra = 'red'
 
        if equipe_blob == pessoa_foto[3]:
            resultado_text += "Equipe correta! "
        else:
            resultado_text += "Equipe incorreta. "
            cor_fundo_equipe = "red"
 
        if nacionalidade_blob == pessoa_foto[4]:
            resultado_text += "Nacionalidade correta! "
        else:
            resultado_text += "Nacionalidade incorreta. "
            cor_fundo_nacionalidade = "red"
 
        if idade == pessoa_foto[5]:
            resultado_text += "Idade correta! "
        else:
            resultado_text += "Idade incorreta. "
            cor_fundo_idade = "red"
 
        if ultima_temporada == pessoa_foto[6]:
            resultado_text += "Última temporada correta!"
        else:
            resultado_text += "Última temporada incorreta."
            cor_fundo_temp = "red"
       
        label_nome_resultado1.configure(text_color=cor_letra)
        frame_equipe.configure(fg_color=cor_fundo_equipe)
        frame_idade.configure(fg_color=cor_fundo_idade)
        frame_nacionalidade.configure(fg_color=cor_fundo_nacionalidade)
        frame_foto_result.configure(fg_color=cor_fundo)
        frame_temp.configure(fg_color=cor_fundo_temp)
 
        equipe_img = mostrar_imagem(equipe_blob)
        nacionalidade_img = mostrar_imagem(nacionalidade_blob)
        piloto_img = mostrar_imagem(foto)
 
        if equipe_img:
            label_equipe_resultado1.configure(image=equipe_img)
            label_equipe_resultado1.image = equipe_img 
        if nacionalidade_img:
            label_nacionalidade_resultado1.configure(image=nacionalidade_img)
            label_nacionalidade_resultado1.image = nacionalidade_img 
        if  piloto_img:
            label_foto_resultado1.configure(image=piloto_img)
            label_foto_resultado1.image = piloto_img
        
        label_nome_resultado1.configure(text=f"{nome}", font=ctk.CTkFont(family="Formula1 Display Bold", size=12, weight="bold"))
        label_idade_resultado1.configure(text=f"{idade}", font=ctk.CTkFont(family="Formula1 Display Bold", size=12, weight="bold"))
        label_ult_temporada_resultado1.configure(text=f"{ultima_temporada}", font=ctk.CTkFont(family="Formula1 Display Bold", size=12, weight="bold"))
        
          
        
        if resultado_text != "Nome correto! Equipe correta! Nacionalidade correta! Idade correta! Última temporada correta!":
            atualizar_imagem()
        else:
            imagem = Image.open(io.BytesIO(foto))  
            new_width = 380
            new_height = 368
            imagem = imagem.resize((new_width, new_height), Image.ANTIALIAS)
            piloto_img = ImageTk.PhotoImage(imagem)
            label_foto.configure(image=piloto_img)
            label_foto.image = piloto_img  
            messagebox.showinfo("Você Ganhou!", "Parabéns, você acertou!")
            entry_tentativa.configure(state="disabled")
 
    else:
        messagebox.showerror("Erro", "Nome não encontrado no banco de dados.")      
 
    conn.close()

pessoa_foto = obter_pessoa_aleatoria()

#--------------------------------------------------------------------------------------------------------------------------#

frame_top = ctk.CTkFrame(app, width=1920, height=200, fg_color='red', border_width=0)
frame_top.grid(row=0, column=0, sticky="ew")

image_info = "informacao 2.png"
image1 = Image.open(image_info)
new_width = 30
new_height = 30
resized_image = image1.resize((new_width, new_height))
icon_informacao = ImageTk.PhotoImage(resized_image)
def abrir_informacao():
    messagebox.showinfo("Informação", """Dicas para Jogar o Jogo de Adivinhar Pilotos de F1
    Analise as cores do uniforme e capacete: Mesmo com a imagem embaçada, os pilotos geralmente têm esquemas de cores únicos que representam suas equipes. Por exemplo, vermelho e branco podem remeter à Ferrari, enquanto azul pode sugerir a Red Bull. Tente identificar essas cores como pistas.

    Observe a postura e o ambiente: A posição do piloto, o tipo de carro ou qualquer outro detalhe de fundo pode dar pistas sobre a época ou a equipe. Pilotos de diferentes eras podem ter estilos de pilotagem ou detalhes de equipamento ligeiramente diferentes.

    Aposte em campeões e pilotos famosos: Se estiver muito em dúvida, comece a adivinhar os pilotos mais conhecidos, como os campeões mundiais (Lewis Hamilton, Michael Schumacher, Ayrton Senna) ou aqueles com muita visibilidade, pois eles têm mais chances de aparecer no jogo.

    Preste atenção nas dicas adicionais: Quando errar, as dicas que aparecem, como idade, equipe e nacionalidade, podem ajudar muito. Se o jogo mencionar que o piloto tem 35 anos e corre para a Mercedes, você já pode limitar suas opções.

    Use o conhecimento das equipes: Saber quais pilotos correram para cada equipe em determinadas épocas é uma vantagem. Por exemplo, se a dica for sobre a Red Bull, você pode pensar em Sebastian Vettel ou Max Verstappen.

    Lembre-se das eras do automobilismo: Se a dica for sobre a idade ou a era em que o piloto competiu, ajuste suas tentativas de acordo. Por exemplo, se for um piloto mais velho, pense em nomes das décadas de 90 ou 2000. Se for um jovem, pense em pilotos recentes.

    Foque nas pistas visuais, mesmo que mínimas: Capacetes, uniformes e até estilos de cabelo podem ser identificadores importantes. Muitos pilotos personalizam seus capacetes, como o capacete verde e amarelo de Ayrton Senna, o que pode ser uma pista mesmo em uma imagem desfocada.

    Teste o piloto da vez: Se estiver jogando durante uma temporada de F1 em andamento, comece apostando nos pilotos da temporada atual, pois é possível que o jogo inclua aqueles que estão mais em alta no momento.""")


figura_informacao = ctk.CTkButton(frame_top, image=icon_informacao, width=0, text='', hover_color='#A80101', fg_color='red', command=abrir_informacao)
figura_informacao.image = icon_informacao
figura_informacao.grid(row=0, column=1, padx=(0, 405), pady=20)



image_estats = "estatistica 2.png"
image_stats = Image.open(image_estats)
new_width = 35
new_height = 30
resized_image_stats = image_stats.resize((new_width, new_height))
icon_estatus = ImageTk.PhotoImage(resized_image_stats)

figura_estatus = ctk.CTkButton(frame_top, image=icon_estatus, width=0, text='', hover_color='#A80101', fg_color='red')
figura_estatus.image = icon_estatus
figura_estatus.grid(row=0, column=3, padx=(425, 0), pady=20)

image_configs = "config.png"
image_config = Image.open(image_configs)
new_width = 45
new_height = 30
resized_image_config = image_config.resize((new_width, new_height))
icon_config = ImageTk.PhotoImage(resized_image_config)

figura_config = ctk.CTkButton(frame_top, image=icon_config, width=0, text='', hover_color='#A80101', fg_color='red')
figura_config.image = icon_config
figura_config.grid(row=0, column=4, padx=(8, 320), pady=20)

image_user = "usuario2.png"
image_user = Image.open(image_user)
new_width = 35
new_height = 35
resized_image_user = image_user.resize((new_width, new_height))
icon_user = ImageTk.PhotoImage(resized_image_user)

figura_user = ctk.CTkButton(frame_top, image=icon_user, width=10, text='', fg_color='red', hover_color='#A80101', command=func_login)
figura_user.image = icon_user
figura_user.grid(row=0, column=0, padx=(270, 8), pady=20)

label_titulo = ctk.CTkLabel(frame_top, text='MYSTERY CARS', 
                           font=ctk.CTkFont(family="Formula1 Display Bold", size=30, weight="bold", slant="italic"),
                           text_color='white', fg_color='red')
label_titulo.grid(row=0, column=2, padx=(50,30), pady=20)

#--------------------------------------------------------------------------------------------------------------------------------------------#

frame_botaos_secao = ctk.CTkFrame(app, width=1920, height=40, fg_color='#15151E', border_width=0)
frame_botaos_secao.grid(row=1, column=0, padx=0, pady=0, sticky='ew')

botao_modo_normal = ctk.CTkButton(frame_botaos_secao, width=0, text='NORMAL', font=ctk.CTkFont(family="Formula1 Display Bold", size=20, weight="bold"), fg_color='#15151E', text_color='white', hover_color='#A80101')
botao_modo_normal.grid(row=0, column=0, padx=(770, 20), pady=5)

separacao1 = ctk.CTkLabel(frame_botaos_secao, bg_color='#15151E', text='/', font=ctk.CTkFont(family="Formula1 Display Bold", size=20, weight="bold"))
separacao1.grid(row=0, column=1, padx=(0,0), pady=0)

botao_modo_f1 = ctk.CTkButton(frame_botaos_secao, width=0, text='F1', font=ctk.CTkFont(family="Formula1 Display Bold", size=20, weight="bold"), fg_color='#15151E', text_color='white', hover_color='#A80101')
botao_modo_f1.grid(row=0, column=2, padx=(40, 40), pady=5)

separacao2 = ctk.CTkLabel(frame_botaos_secao, bg_color='#15151E', text='/', font=ctk.CTkFont(family="Formula1 Display Bold", size=20, weight="bold"))
separacao2.grid(row=0, column=3, padx=(0,0), pady=0)

botao_ranking = ctk.CTkButton(frame_botaos_secao, width=0, text='RANKING', font=ctk.CTkFont(family="Formula1 Display Bold", size=20, weight="bold"), fg_color='#15151E', text_color='white', hover_color='#A80101')
botao_ranking.grid(row=0, column=4, padx=(20, 775), pady=5)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

image_fundo = "senna2.png"
image_senna = Image.open(image_fundo)
new_width = 1920
new_height = 1000
resized_image = image_senna.resize((new_width, new_height))
fundo_senna = ImageTk.PhotoImage(resized_image)

frame_geral = ctk.CTkFrame(app, width=1920, height=1000, border_width=0)
frame_geral.grid(row=2, column=0, sticky='ew')

label_fundo = ctk.CTkLabel(frame_geral, image=fundo_senna, width=0, text='')
label_fundo.image = fundo_senna
label_fundo.grid(sticky='nwes')

frame_jogo = ctk.CTkFrame(frame_geral, width=400, height=420, border_width=10, corner_radius=30, border_color='red', bg_color='#303033', fg_color='#303033')
frame_jogo.place(relx=0.49, rely=0.25, anchor=ctk.CENTER)

label_foto = ctk.CTkLabel(frame_jogo, text='', bg_color='#303033', fg_color='#303033')
label_foto.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

def atualizar_imagem():
    global contador_tentativas, imagens
    colunas_imagens = [4, 3, 2] 
    if contador_tentativas < len(colunas_imagens):
        imagem_blob = imagens[0][colunas_imagens[contador_tentativas]] 
        imagem = Image.open(io.BytesIO(imagem_blob))
        new_width = 380
        new_height = 368
        imagem = imagem.resize((new_width, new_height), Image.ANTIALIAS)
        imagem = ImageTk.PhotoImage(imagem)
        if imagem:
            label_foto.configure(image=imagem)
            label_foto.image = imagem
            contador_tentativas += 1 
    else:
        messagebox.showinfo("Você Perdeu", "Você excedeu o número de tentativas.")
        entry_tentativa.configure(state="disabled")

atualizar_imagem()  

# Entry com sugestões
entry_tentativa = ctk.CTkEntry(frame_geral, placeholder_text='Tentativa 1 de 3', placeholder_text_color='#8D8D8D', width=280, height=40, font=ctk.CTkFont(family="Formula1 Display Regular", size=15),fg_color='white', border_width=2, border_color='red', corner_radius=10, justify='center', text_color="#8D8D8D")
entry_tentativa.place(relx=0.49, rely=0.449, anchor=ctk.CENTER)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

frame_resultado = ctk.CTkFrame(frame_geral, width=600, height=200, fg_color='#575C61', bg_color='#303033', corner_radius=20)
frame_resultado.place(relx=0.49, rely=0.6, anchor=ctk.CENTER)
frame_resultado.place_forget()

nome_foto1 = ctk.CTkLabel(frame_resultado, text='FOTO', text_color='Black', font=ctk.CTkFont(family="Formula1 Display Regular", size=12), width=0, height=0)
nome_foto1.place(relx=0.165, rely=0.19)

frame_foto_result = ctk.CTkFrame(frame_resultado, width=45, height=45)
frame_foto_result.place(relx=0.16, rely=0.29)

label_foto_resultado1 = ctk.CTkLabel(frame_foto_result, text='', width=0, height=0)
label_foto_resultado1.place(relx=0.47, rely=0.47, anchor=ctk.CENTER)

frame_equipe = ctk.CTkFrame(frame_resultado, width=45, height=45, fg_color='red')
frame_equipe.place(relx=0.31, rely=0.29)

nome_equipe1= ctk.CTkLabel(frame_resultado, text='EQUIPE', text_color='Black', font=ctk.CTkFont(family="Formula1 Display Regular", size=12), width=0, height=0)
nome_equipe1.place(relx=0.305, rely=0.19)

label_equipe_resultado1 = ctk.CTkLabel(frame_equipe, text='', width=0, height=0)
label_equipe_resultado1.place(relx=0.47, rely=0.47, anchor=ctk.CENTER)

frame_nacionalidade = ctk.CTkFrame(frame_resultado, width=45, height=45, fg_color='red')
frame_nacionalidade.place(relx=0.46, rely=0.29)

nome_nacionalidade1= ctk.CTkLabel(frame_resultado, text='NAT', text_color='Black', font=ctk.CTkFont(family="Formula1 Display Regular", size=12), width=0, height=0)
nome_nacionalidade1.place(relx=0.47, rely=0.19)

label_nacionalidade_resultado1 = ctk.CTkLabel(frame_nacionalidade, text='', width=0, height=0)
label_nacionalidade_resultado1.place(relx=0.47, rely=0.47, anchor=ctk.CENTER)

frame_idade = ctk.CTkFrame(frame_resultado, width=45, height=45, fg_color='red')
frame_idade.place(relx=0.61, rely=0.29)

nome_idade1= ctk.CTkLabel(frame_resultado, text='IDADE', text_color='Black', font=ctk.CTkFont(family="Formula1 Display Regular", size=12), width=0, height=0)
nome_idade1.place(relx=0.61, rely=0.19)

label_idade_resultado1 = ctk.CTkLabel(frame_idade, text='', width=0, height=0)
label_idade_resultado1.place(relx=0.285, rely=0.325)

frame_temp = ctk.CTkFrame(frame_resultado, width=45, height=45, fg_color='red')
frame_temp.place(relx=0.76, rely=0.29)

nome_temp1= ctk.CTkLabel(frame_resultado, text='TEMP', text_color='Black', font=ctk.CTkFont(family="Formula1 Display Regular", size=12), width=0, height=0)
nome_temp1.place(relx=0.76, rely=0.19)

label_ult_temporada_resultado1 = ctk.CTkLabel(frame_temp, text='', width=0, height=0)
label_ult_temporada_resultado1.place(relx=0.1, rely=0.3)

label_nome_resultado1 = ctk.CTkLabel(frame_resultado, text="",width=30, height=0, font=ctk.CTkFont(family="Formula1 Display Regular", size=50))
label_nome_resultado1.place(relx=0.41, rely=0.06)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

suggestions_frame = ctk.CTkFrame(frame_geral, fg_color='#575C61', corner_radius=10)
suggestions_frame.place(relx=0.49, rely=0.5, anchor=ctk.N)
suggestions_frame.place_forget()  

suggestions = ["Ayrton Senna", "Charles Leclerc", "Lewis Hamilton", "Max Verstappen", "Alain Prost", "Sebastian Vettel", "Alexander Albon", "Franco Colapinto", "Carlos Sainz", "Pierre Gasly", "Esteban Ocon", "Lando Norris", "George Russell", "Valtteri Bottas", "Sergio Perez", "Zhou Guanyu", "Fernando Alonso", "Kevin Magnussen", "Lian Lawson", "Yuki Tsunoda", "Lance Stroll", "Oscar Piastri", "Nico Hulkenberg"]



def on_keyrelease(event):
    typed_text = entry_tentativa.get()
    update_suggestions(typed_text)

def update_suggestions(typed_text):
    for widget in suggestions_frame.winfo_children():
        widget.destroy()

    if typed_text:
        filtered_suggestions = [s for s in suggestions if typed_text.lower() in s.lower()]
        for suggestion in filtered_suggestions:
            label = ctk.CTkLabel(suggestions_frame, text=f'{suggestion}', font=ctk.CTkFont(family="Formula1 Display Regular", size=15, slant="italic"), width=300, fg_color='#D9D9D9', text_color='black')
            label.pack(fill="x") 
            label.bind("<Button-1>", lambda e, s=suggestion: select_suggestion(s)) 
        suggestions_frame.place(relx=0.492, rely=0.47, anchor=ctk.N) 
    else:
        suggestions_frame.place_forget()  

def select_suggestion(suggestion):
    entry_tentativa.delete(0, ctk.END)  
    entry_tentativa.insert(0, suggestion) 
    suggestions_frame.place_forget()  

entry_tentativa.bind("<KeyRelease>", on_keyrelease)


def on_enter(event):
    comparar_pessoa()
    frame_resultado.place(relx=0.49, rely=0.6, anchor=ctk.CENTER)
    entry_tentativa.delete(0, ctk.END)
    
        

entry_tentativa.bind("<Return>", on_enter)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

frame_ranking = ctk.CTkFrame(frame_geral, width=500, height=340, fg_color='#32393E')
frame_ranking.place(relx=0.007, rely= 0.63)

header = []
for col, text in enumerate(header):
    header_label = ctk.CTkLabel(frame_ranking, text=text, fg_color='gray', text_color='white', width=160)
    header_label.grid(row=0, column=col, padx=5, pady=(3, 0), sticky='nw')

ranking_data = [
    (1, "Jogador 1", 100),
    (2, "Jogador 2", 90),
    (3, "Jogador 3", 85),
    (4, "Jogador 4", 80),
    (5, "Jogador 5", 75),
]

for row, (position, name, points) in enumerate(ranking_data, start=1):
    color = 'red' if row % 2 == 1 else 'white'  
    label_position = ctk.CTkLabel(frame_ranking, text=str(position), fg_color=color, text_color='black', width=160)
    label_position.grid(row=row, column=0, padx=5, pady=(3, 0), sticky='nw')
    
    label_name = ctk.CTkLabel(frame_ranking, text=name, fg_color=color, text_color='black', width=160)
    label_name.grid(row=row, column=1, padx=5, pady=(3, 0), sticky='nw')
    
    label_points = ctk.CTkLabel(frame_ranking, text=str(points), fg_color=color, text_color='black', width=160)
    label_points.grid(row=row, column=2, padx=5, pady=(3, 0), sticky='nw')

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

frame_dicas = ctk.CTkFrame(frame_geral, width=500, height=340, fg_color='#32393E')
frame_dicas.place(relx=0.70, rely=0.54)

label_dica = ctk.CTkLabel(frame_dicas, text='DICAS', text_color='red', font=ctk.CTkFont(family="Formula1 Display Regular", size=16))
label_dica.place(relx=0.07, rely= 0.04)

textbox_dicas = ctk.CTkTextbox(frame_dicas, width=480, height=320, fg_color='#32393E', text_color='white', font=ctk.CTkFont(family="Formula1 Display Regular", size=11))
textbox_dicas.place(relx=0.07, rely=0.1)



dicas_text = (
    """• Objetivo do Jogo: Aparecerá uma foto embaçada de um piloto de 
    Fórmula 1. Sua missão é adivinhar o nome correto desse piloto. 
    Se errar, você receberá dicas para te ajudar a acertar na próxima 
    tentativa!\n\n"""
    """• Passo a Passo:
Passo 1: Quando a foto aparecer, escreva o nome do piloto que 
você acha que é.
Passo 2: Se você acertar o nome completo do piloto, parabéns, 
você venceu essa rodada!
Passo 3: Se errar, você receberá uma dica como idade, equipe, ou 
nacionalidade do piloto para tentar de novo.\n\n"""
    """• Dicas para Ajudar:
Errou o nome? Fique tranquilo! O jogo vai te dar pistas como:
A idade do piloto.
O nome da equipe pela qual ele correu ou corre atualmente.
A nacionalidade (por exemplo, "britânico", "alemão").
Use essas informações para ajustar suas tentativas na próxima rodada.\n\n"""
    """• Como ganhar: Continue tentando até adivinhar o nome correto usando 
    as dicas fornecidas!\n""")
    

textbox_dicas.insert("0.0", dicas_text)
textbox_dicas.configure(state="disabled") 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



app.mainloop()