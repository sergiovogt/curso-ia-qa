# Prompt — Traductor técnico dev→QA

> Pieza 1 del kit. Costo cero: pegalo en cualquier IA (ChatGPT, Claude, Copilot, Cursor) junto con el ticket. No necesitás instalar nada.

Cuando un ticket menciona un concepto técnico que no conocés, en vez de frenarte, pedile a la IA que lo traduzca a lenguaje de QA.

## Prompt

```
Actuá como QA senior de Adalove. Te paso un ticket de desarrollo.

Explicame en lenguaje de QA, sin tecnicismos innecesarios:
1. Qué se cambió o se va a cambiar, en una frase.
2. Qué debería probar yo como QA para validar este cambio.
3. Qué conceptos técnicos menciona el ticket que conviene que entienda
   antes de empezar (explicá cada uno en una línea).
4. Qué casos negativos o de borde se te ocurren para este cambio.

Ticket:
"""
[PEGÁ ACÁ LA DESCRIPCIÓN DEL TICKET]
"""
```

## Ejemplo con el ticket de la sesión (TASK-142)

Ticket: *"Al cambiar el estado de una tarea, el cambio no se refleja en la lista hasta recargar la página. El endpoint PATCH /tasks/:id devuelve 200, pero el componente del frontend no hace refetch tras la respuesta."*

La IA debería devolver algo como:
1. **Qué se cambió:** el comportamiento al actualizar el estado de una tarea desde la pantalla.
2. **Qué probar:** que al cambiar el estado, la lista muestre el nuevo estado al instante, sin recargar.
3. **Conceptos:** *PATCH* = pedido que actualiza parte de un recurso; *200* = el servidor respondió OK; *refetch/re-render* = que la pantalla vuelva a pedir o redibujar los datos tras el cambio.
4. **Casos de borde:** cambiar al mismo estado que ya tenía, cambiar varias tareas seguidas, cambiar estado y luego recargar (¿persiste?), error de red en mitad del cambio.

> Recordá: el punto 4 es un disparador, no una lista cerrada. Los casos negativos que valen son los que vos ves con tu criterio.
