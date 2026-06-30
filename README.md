# curso-ia-qa — Kit de arranque QA con IA

Repo de ejemplo de la **Capacitación #4: QA con IA** (Adalove, 2026-06-30).

Una app web mínima con un bug deliberado (TASK-142) y el kit de tres piezas que se
recorre en la sesión, siguiendo el hilo **"el ticket como punto de partida"**.

## El ticket de la sesión

> **TASK-142 — "El estado de la tarea no se actualiza en pantalla al cambiarlo"**
> Al cambiar el estado de una tarea, el cambio no se refleja en la lista hasta recargar
> la página. El endpoint `PATCH /tasks/:id` devuelve 200, pero el componente del frontend
> no hace refetch tras la respuesta.

## Estructura

```
curso-ia-qa/
├── app/              # Gestor de Tareas (Flask + UI) con el bug deliberado
├── prompts/          # Pieza 1: traductor técnico + generador de casos (costo cero)
├── testsprite/       # Pieza 2: README de setup + pasos de ejemplo
└── playwright/       # Pieza 3: proyecto configurado + test E2E de ejemplo
```

## Arranque rápido

```
cd app
python -m venv venv
source venv/bin/activate      # Linux/Mac/WSL
# venv\Scripts\activate       # Windows (PowerShell/CMD)
pip install -r requirements.txt
python app.py                 # http://localhost:5000  (demo / demo)
```

> El `venv/` queda fuera del control de versiones (ver `.gitignore`). Para salir del entorno: `deactivate`.

Cambiá el estado de una tarea: vas a ver que la lista **no se actualiza** hasta recargar.
Ese es TASK-142, el bug que atraviesa todas las demos.

## El recorrido (los 4 pasos de la sesión)

1. **Leer el ticket** — la IA lo lee desde ClickUp (vía MCP).
2. **Entender + generar casos** — `prompts/traductor-tecnico.md` y `prompts/generador-casos.md`.
3. **Ejecutar y dejar evidencia** — `testsprite/` (sin código, video como evidencia).
4. **Versionar para regresión** — `playwright/` (con código, generado por IA).
