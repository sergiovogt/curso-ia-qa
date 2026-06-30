# Prompt — Generador de casos de prueba desde el ticket

> Pieza 1 del kit. Costo cero. Genera el borrador de los casos en el formato del template de Luciana, para que solo agregues los casos negativos y de borde que ves con tu criterio.

## Prompt

```
Actuá como QA de Adalove. Te paso un ticket de desarrollo.

Generá los casos de prueba en formato de tabla con estas columnas exactas:
ID | Condición | Pasos | Resultado esperado | Estado | Observación | Tester

Reglas:
- ID: formato TC-001, TC-002, ...
- Incluí casos positivos (camino feliz) Y casos negativos / de borde.
- "Pasos": numerados, concretos, accionables.
- "Estado" y "Tester": dejalos vacíos (los completo al ejecutar).
- No inventes funcionalidad que no esté en el ticket.

Ticket:
"""
[PEGÁ ACÁ LA DESCRIPCIÓN DEL TICKET]
"""
```

## Formato de salida esperado (columnas del template de Luciana)

| ID | Condición | Pasos | Resultado esperado | Estado | Observación | Tester |
|----|-----------|-------|--------------------|--------|-------------|--------|
| TC-001 | Cambio de estado válido | 1. Login. 2. Cambiar estado de una tarea a "completada". | El estado "completada" se ve en la lista al instante, sin recargar. |  |  |  |
| TC-002 | Persistencia tras recarga | 1. Cambiar estado. 2. Recargar la página. | El estado nuevo se mantiene tras recargar. |  |  |  |
| TC-003 | Cambio al mismo estado | 1. Cambiar una tarea al estado que ya tenía. | No hay error; el estado se mantiene. |  |  |  |
| TC-004 | Cambios consecutivos | 1. Cambiar el estado de 3 tareas seguidas. | Las 3 reflejan su nuevo estado en la lista. |  |  |  |

> La IA arma el andamiaje (camino feliz + casos obvios). **Los casos negativos finos y las regresiones por paranoia son tuyos** — "testeá esperando que falle". Revisá, agregá y ajustá antes de ejecutar.
