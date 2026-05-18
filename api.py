from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

def conectar():
    return sqlite3.connect("tarefas.db")

def init_db():
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

init_db()

@app.route("/")
def inicio():
    return "API de tarefas funcionando!"

@app.route("/tarefas")
def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    lista = []
    for tarefa in tarefas:
        lista.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": bool(tarefa[2])
        })

    return jsonify(lista)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)