import sqlite3

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# Conectar ao banco de dados
conn = sqlite3.connect('mystery_cars_real1.db')
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS pilotos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) UNIQUE,
    foto BLOB,
    equipe BLOB,
    nacionalidade BLOB,
    idade INTEGER,
    ultima_temporada INTEGER
);
""")

# Inserir dados no banco de dados
'''cursor.execute("""
INSERT INTO pilotos (nome, foto, equipe, nacionalidade, idade, ultima_temporada) VALUES 
    ("Alexander Albon",  ?, ?, ?, 28, 2024),
    ("Franco Colapinto",  ?, ?, ?, 21, 2024),
               ("Pierre Gasly",  ?, ?, ?, 28, 2024),
               ("Esteban Ocon",   ?, ?, ?, 28, 2024),
               ("Carlos Sainz",   ?, ?, ?, 30, 2024),
               ("Lando Norris",   ?, ?, ?, 25, 2024),
               ("George Russell", ?, ?, ?, 26, 2024),
               ("Valtteri Bottas",  ?, ?, ?, 36, 2024),
               ("Sergio Perez", ?, ?, ?, 34, 2024),
               ("Zhou Guanyu",  ?, ?, ?, 25, 2024),
               ("Fernando Alonso", ?, ?, ?, 43, 2024),
               ("Kevin Magnussen",  ?, ?, ?, 32, 2024),
               ("Lian Lawson",  ?, ?, ?, 22, 2024),
               ("Yuki Tsunoda",   ?, ?, ?, 24, 2024),
               ("Lance Stroll",   ?, ?, ?, 25, 2024),
               ("Oscar Piastri",   ?, ?, ?, 22, 2024),
               ("Nico Hulkenberg", ?, ?, ?, 37, 2024) """,

(read_file("albon.png"), read_file("willians.png"), read_file("Tailandia.png"), read_file("colapinto.png"), read_file("willians.png"),  read_file("Argentina.png"), 
 read_file("gasly.png"),  read_file("alpine.png"), read_file("Franca.png"), read_file("ocon.png"),  read_file("alpine.png"), read_file("franca.png"), read_file("sainz.png"),
 read_file("ferrari.png"),  read_file("Espanha.png"), read_file("norris.png"), read_file("mclaren.png"),  read_file("Reino.png"), read_file("russel.png"),  read_file("mercedes.png"),
 read_file("Reino.png"),  read_file("bottas.png"),  read_file("sauber.png"),  read_file("Finlandia.jpg"), read_file("perez.png"),  read_file("redburro.png"),  read_file("Mexico.png"),
 read_file("zhou.png"),  read_file("sauber.png"),  read_file("China.png"),  read_file("alonso.png"),  read_file("aston.png"),  read_file("Espanha.png"),
 read_file("magnussen.png"),  read_file("hass.png"),  read_file("Dinamarca.png"),  read_file("lawson.png"),  read_file("rb.png"),  read_file("Zelandia.png"),
 read_file("tsunoda.png"),  read_file("rb.png"),  read_file("Japao.png"),   read_file("stroll.png"),  read_file("aston.png"),  read_file("Canada.png"),
 read_file("piastri.png"),  read_file("mclaren.png"),  read_file("Australia.png"),   read_file("hulkenberg.png"),  read_file("hass.png"), read_file("Alemanha.png")

))'''

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   email TEXT NOT NULL UNIQUE,
   password TEXT NOT NULL
);               
""")

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS pilotos_jogo (
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     nome TEXT NOT NULL UNIQUE,
     foto1 BLOB NOT NULL,
     foto2 BLOB NOT NULL,
     foto3 BLOB NOT NULL
);
""")

'''cursor.execute("""
INSERT INTO pilotos_jogo (nome, foto1, foto2, foto3) VALUES
               ("Alexander Albon",  ?, ?, ?),
                ("Franco Colapinto",  ?, ?, ?),
               ("Pierre Gasly",  ?, ?, ?),
               ("Esteban Ocon",   ?, ?, ?),
               ("Carlos Sainz",   ?, ?, ?),
               ("Lando Norris",   ?, ?, ?),
               ("George Russell", ?, ?, ?),
               ("Valtteri Bottas",  ?, ?, ?),
               ("Sergio Perez", ?, ?, ?),
               ("Zhou Guanyu",  ?, ?, ?),
               ("Fernando Alonso", ?, ?, ?),
               ("Kevin Magnussen",  ?, ?, ?),
               ("Lian Lawson",  ?, ?, ?),
               ("Yuki Tsunoda",   ?, ?, ?),
               ("Lance Stroll",   ?, ?, ?),
               ("Oscar Piastri",   ?, ?, ?),
               ("Nico Hulkenberg", ?, ?, ?)"""
       , (
           read_file("albon 1.png"),  read_file("albon 2.png"), read_file("albon 4.png"),
           read_file("colapinto 1.png"),  read_file("colapinto 2.png"),  read_file("colapinto 4.png"),
           read_file("gasly 1.png"),  read_file("gasly 2.png"),  read_file("gasly 4.png"),
           read_file("ocon 1.png"),  read_file("ocon 2.png"), read_file("ocon 4.png"),
           read_file("sainz 1.png"),  read_file("sainz 2.png"),  read_file("sainz 4.png"),
           read_file("norris 1.png"),  read_file("norris 2.png"),   read_file("norris 4.png"),
           read_file("russel 1.png"),  read_file("russel 2.png"), read_file("russel 4.png"),
           read_file("bottas 1.png"),  read_file("bottas 2.png"),   read_file("bottas 4.png"),
           read_file("perez 1.png"),  read_file("perez 2.png"),  read_file("perez 4.png"),
           read_file("zhou 1.png"),  read_file("zhou 2.png"), read_file("zhou 4.png"),
           read_file("alonso 1.png"),  read_file("alonso 2.png"),  read_file("alonso 4.png"),
           read_file("magnussen 1.png"),  read_file("magnussen 2.png"),   read_file("magnussen 4.png"),
           read_file("lawson 1.png"),  read_file("lawson 2.png"),  read_file("lawson 4.png"),
           read_file("tsunoda 1.png"),  read_file("tsunoda 2.png"),   read_file("tsunoda 4.png"),
           read_file("stroll 1.png"),  read_file("stroll 2.png"),   read_file("stroll 4.png"),
           read_file("piastri 1.png"),  read_file("piastri 2.png"),    read_file("piastri 4.png"),
           read_file("hulkenberg 1.png"),  read_file("hulkenberg 2.png"),   read_file("hulkenberg 4.png")


       ))'''


# Confirmar as alterações
conn.commit()

# Fechar a conexão
conn.close()

print("Conectado ao banco de dados e dados inseridos com sucesso.")
