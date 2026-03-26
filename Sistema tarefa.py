import sqlite3

def conectar():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            concluida INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def adicionar_tarefa(titulo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    print("\n---- TAREFAS ----")
    for tarefa in tarefas:
        status = "✅" if tarefa[2] == 1 else "❌"
        print(f"{tarefa[0]} - {tarefa[1]} {status}")

def concluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Tarefa concluída!")

def deletar_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Tarefa deletada!")

criar_tabela()

while True:
    print("\n---- MENU ----")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Deletar tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Nome da tarefa: ")
        adicionar_tarefa(titulo)

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        listar_tarefas()
        id = int(input("ID da tarefa para concluir: "))
        concluir_tarefa(id)

    elif opcao == "4":
        listar_tarefas()
        id = int(input("ID da tarefa para deletar: "))
        deletar_tarefa(id)

    elif opcao == "5":
        print("Saindo...")
        break