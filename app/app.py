"""
curso-ia-qa — Gestor de Tareas (app de ejemplo para la Capacitación #4: QA con IA)

App web mínima con UI: login + lista de tareas + cambiar estado.

⚠️ BUG DELIBERADO (TASK-142):
Al cambiar el estado de una tarea, el endpoint PATCH /tasks/<id> responde 200,
pero el frontend NO refleja el cambio en la lista hasta recargar la página.
Es el bug que atraviesa todas las demos de la sesión.

Correr (con entorno virtual):
    python -m venv venv
    source venv/bin/activate      # Linux/Mac/WSL
    venv\\Scripts\\activate        # Windows (PowerShell/CMD)
    pip install -r requirements.txt
    python app.py
    # http://localhost:5000  (usuario: demo / contraseña: demo)
"""
import os
import sqlite3
from flask import (
    Flask, g, render_template, request, redirect, url_for, session, jsonify
)

DB_PATH = os.path.join(os.path.dirname(__file__), "tasks.db")
ESTADOS = ["pendiente", "en progreso", "completada"]

app = Flask(__name__)
app.secret_key = "curso-ia-qa-demo"  # solo para la demo, no usar en producción


# --- Base de datos ---------------------------------------------------------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Crea la tabla y carga tareas de ejemplo si la DB no existe."""
    first_time = not os.path.exists(DB_PATH)
    db = sqlite3.connect(DB_PATH)
    db.execute(
        """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'pendiente'
        )"""
    )
    if first_time:
        db.executemany(
            "INSERT INTO tasks (titulo, estado) VALUES (?, ?)",
            [
                ("Validar login con credenciales válidas", "pendiente"),
                ("Validar mensaje de error con clave incorrecta", "pendiente"),
                ("Revisar carga de la lista de tareas", "en progreso"),
                ("Probar cambio de estado de una tarea", "pendiente"),
            ],
        )
    db.commit()
    db.close()


# --- Autenticación (mínima, para la demo) ----------------------------------

def login_required(view):
    from functools import wraps

    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("user") == "demo" and request.form.get("password") == "demo":
            session["user"] = "demo"
            return redirect(url_for("index"))
        error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# --- Vistas ----------------------------------------------------------------

@app.route("/")
@login_required
def index():
    tasks = get_db().execute("SELECT id, titulo, estado FROM tasks ORDER BY id").fetchall()
    return render_template("list.html", tasks=tasks, estados=ESTADOS)


@app.route("/tasks/<int:task_id>", methods=["PATCH"])
@login_required
def update_task(task_id):
    """Actualiza el estado de una tarea. Responde 200 con el nuevo estado.

    El backend funciona correctamente: el bug está en el frontend (ver list.html).
    """
    nuevo_estado = (request.get_json(silent=True) or {}).get("estado")
    if nuevo_estado not in ESTADOS:
        return jsonify({"error": "estado inválido"}), 400
    db = get_db()
    cur = db.execute("UPDATE tasks SET estado = ? WHERE id = ?", (nuevo_estado, task_id))
    db.commit()
    if cur.rowcount == 0:
        return jsonify({"error": "tarea no encontrada"}), 404
    return jsonify({"id": task_id, "estado": nuevo_estado}), 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
