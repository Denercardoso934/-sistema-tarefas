from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect("tarefas.db")

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

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)