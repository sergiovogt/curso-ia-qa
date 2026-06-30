# Pasos de prueba — TASK-142 (input para Test Sprite)

> Documento de pasos que se le carga a Test Sprite (modo frontend). Sale de los casos
> generados con el prompt `generador-casos.md`. Test Sprite lo ejecuta sobre la app
> `curso-ia-qa` corriendo en http://localhost:5000.

## Contexto

App: Gestor de Tareas. Usuario de prueba: `demo` / `demo`.
Bug a validar: al cambiar el estado de una tarea, el nuevo estado no se refleja en la
lista hasta recargar la página.

## Pasos

1. Abrir http://localhost:5000
2. Iniciar sesión con usuario `demo` y contraseña `demo`.
3. Verificar que se ve la lista de tareas.
4. En la tarea "Probar cambio de estado de una tarea", cambiar el estado a "completada".
5. **Verificar (sin recargar):** la columna Estado de esa fila debe mostrar "completada".
6. Recargar la página.
7. Verificar que el estado "completada" se mantiene tras la recarga.

## Resultado esperado

- Paso 5 debería pasar, pero **falla** por el bug: la UI no se actualiza sin recargar.
- Paso 7 pasa: tras recargar, el estado correcto aparece (el backend sí guardó el cambio).

Esa discrepancia entre el paso 5 y el paso 7 es exactamente TASK-142, y queda registrada
en el video que genera Test Sprite.
