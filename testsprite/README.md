# Test Sprite — setup y uso (Pieza 2 del kit)

Test Sprite es testing asistido por IA, sin escribir código: le das los pasos de prueba,
los ejecuta solo, y deja la evidencia (video para frontend, código para backend),
versionada dentro del repo.

## Setup

1. Tener la app `curso-ia-qa` corriendo (con entorno virtual):
   ```
   cd app
   python -m venv venv
   source venv/bin/activate      # Linux/Mac/WSL  ·  venv\Scripts\activate en Windows
   pip install -r requirements.txt
   python app.py                 # http://localhost:5000
   ```
2. Instalar la extensión / MCP de Test Sprite en tu IDE (Cursor o VS Code).
   Seguí la guía oficial de Test Sprite para conectar el MCP.
3. Verificar que el IDE reconoce el MCP de Test Sprite (que aparezca al invocarlo desde el chat).

> Nota: si el IDE no reconoce el MCP al invocarlo, suele ser un tema de la configuración
> del MCP server, no de la app. Revisá la config del MCP antes de seguir.

## Uso (modo frontend)

1. Pedile a la IA del IDE que genere el documento de pasos del proyecto, o usá el que ya
   está en este repo: `pasos-task-142.md`.
2. Invocá Test Sprite, elegí **frontend**, y cargá el archivo de pasos.
3. Test Sprite abre la app, ejecuta los pasos y **graba un video** de cada test.
4. La evidencia queda en una carpeta dentro del repo, versionada junto al código.

## Uso (modo backend)

Igual que frontend, pero elegís **backend**. En vez de video, Test Sprite deja el
**código de prueba** generado (por defecto en Python) en la carpeta de evidencia.

## Qué deja como evidencia

- **Frontend:** video de cada test → reemplaza las capturas pegadas a mano.
- **Backend:** código de prueba (Python por defecto).
- En ambos casos: carpeta versionada dentro del repo, un archivo por test.
