import sqlite3
import database

conectar = sqlite3.connect("livros.db")
cursor = conectar.cursor()



def checar_usuario():
    nome = input("Digite o seu nome: ").strip().capitalize()
    cursor.execute("SELECT id, nome FROM usuario WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    if resultado is not None:
        print("Usuario encontrado")
        return resultado[0]

    else:
        print("Usuário nao encontrado no sistema")
        novo = input("Deseja cadastrar esse usuário? R: Sim/Nao: ").lower()
        if novo == "sim":
            cadastrar_usuario(nome)
            return None
        return None




def cadastrar_usuario(nome_novo: str):
    try:
        cursor.execute("INSERT INTO usuario (nome) VALUES (?)", (nome_novo,))
        conectar.commit()
        print("-" * 30)
        print("usuário cadastrado no sistema")
        print("-" * 30)
    except sqlite3.IntegrityError:
        print("-" * 40)
        print("O usuário já possui cadastro no sistema")
        print("-" * 40)


def usuarios_cadastrado():
    cursor.execute("SELECT nome FROM usuario")
    resultado = cursor.fetchall()
    print("Os usuários cadastrados no sistema atualmente são")
    for i in resultado:
        print(f"- {i[0]}")

def adicionar_livro(nome_livro: str ,paginas_totais: int, genero: str, usuario_id: int):
    cursor.execute('INSERT INTO livro (nome_livro, paginas_totais, genero, usuario_id) VALUES (?, ?, ?, ?)', (nome_livro, paginas_totais, genero, usuario_id) )
    conectar.commit()
    print("-" * 50)
    print("Livro adicionado com sucesso.")
    print("-" * 50)


def checar_livro(usuario: int):
    cursor.execute("SELECT * FROM livro WHERE usuario_id = ?", (usuario,))
    resultado = cursor.fetchall()
    print("Atualmente os livros são:")
    print("")
    for i in resultado:
        print(i)
    
while True:
    print("\n1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Cadastrar Usuario")
    print("4 - Sair")

    input_opcao = int(input("Escolha uma opção: "))
    if input_opcao == 4:
        break
    elif input_opcao == 2:
        input_usuario = checar_usuario()
        checar_livro(input_usuario)
    elif input_opcao == 3:
        nome_usuario = input("Digite o nome do usuário que você quer cadastrar: ").lower().capitalize()
        cadastrar_usuario(nome_usuario)
    elif input_opcao == 1:
        usuario_id = checar_usuario()
        if usuario_id == None:
            continue
        nome_livro = input("Digite o nome do livro: ")
        print("-" * 50)
        paginas_totais = input("Digite a quantidade de paginas: ")
        print("-" * 50)
        genero = input("Digite qual é o genero:") 
        print("-" * 50)
        adicionar_livro(nome_livro, paginas_totais, genero, usuario_id)

        


        












