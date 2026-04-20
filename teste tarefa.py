import sqlite3
import os

def conectar():
    return sqlite3.connect("test_banco.db")

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

def test_adicionar_tarefa():
    criar_tabela()
    adicionar_tarefa("Estudar Python")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE titulo = 'Estudar Python'")
    tarefa = cursor.fetchone()
    conn.close()
    assert tarefa is not None
    print("teste passou!")

test_adicionar_tarefa()
os.remove("test_banco.db")