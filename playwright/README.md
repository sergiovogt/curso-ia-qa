# Playwright — setup y uso (Pieza 3 del kit)

Playwright corre tests E2E (end-to-end) sobre el navegador. A diferencia de Test Sprite,
es **código** — pero no lo escribís a mano: lo genera la IA, y queda versionado para correr
en cada deploy (regresión).

## Setup

1. Tener la app `curso-ia-qa` corriendo en http://localhost:5000.
2. Instalar dependencias:
   ```
   cd playwright
   npm install
   npx playwright install
   ```
3. Correr los tests:
   ```
   npm test
   ```
4. Ver el reporte:
   ```
   npm run report
   ```

## Las dos formas de generar un test (sin escribir código)

### 1. `codegen` — grabás tus clicks
```
npm run codegen
```
Playwright abre el navegador, hacés las acciones como si probaras a mano, y te genera
el script. Buen punto de partida, pero todavía sin aserciones.

### 2. La IA lo genera desde el caso de prueba
Pegale a la IA el caso de prueba y pedile el test (ejemplo en `script-demo-playwright`):
```
Convertí este caso de prueba en un test E2E de Playwright (TypeScript)...
```
El QA define el caso, la IA escribe el test, el dev lo mantiene e integra al pipeline.

## El test de ejemplo

`tests/task-142.spec.ts` valida TASK-142:
- **Falla** mientras el bug está activo (la UI no refleja el cambio sin recargar).
- Cuando el dev arregle el frontend, **pasa** y queda corriendo en cada deploy.
