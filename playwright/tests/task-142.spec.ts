import { test, expect } from '@playwright/test';

// TASK-142 — Test E2E generado a partir del caso de prueba (Pieza 3 del kit).
//
// El QA define el caso; la IA escribe el test; el dev lo mantiene.
//
// Este test FALLA mientras el bug está activo (la UI no refleja el cambio sin
// recargar). Cuando el dev arregle el frontend para que haga refetch/re-render,
// el test pasa y queda corriendo en cada deploy como regresión.

test('el estado de la tarea se refleja en la lista sin recargar', async ({ page }) => {
  // Login
  await page.goto('/');
  await page.getByTestId('login-user').fill('demo');
  await page.getByTestId('login-password').fill('demo');
  await page.getByTestId('login-submit').click();

  // Lista visible
  await expect(page.getByTestId('task-table')).toBeVisible();

  // Cambiar el estado de la tarea 4 a "completada"
  const fila = page.locator('[data-task-id="4"]');
  await fila.getByTestId('task-select').selectOption('completada');

  // Aserción clave: el nuevo estado debe verse en la lista SIN recargar.
  // Falla mientras TASK-142 esté activo.
  await expect(fila.getByTestId('task-estado')).toHaveText('completada');
});

test('el cambio de estado persiste tras recargar', async ({ page }) => {
  await page.goto('/');
  await page.getByTestId('login-user').fill('demo');
  await page.getByTestId('login-password').fill('demo');
  await page.getByTestId('login-submit').click();

  const fila = page.locator('[data-task-id="4"]');
  await fila.getByTestId('task-select').selectOption('en progreso');

  // El backend sí guarda el cambio: tras recargar, el estado correcto aparece.
  await page.reload();
  await expect(page.locator('[data-task-id="4"]').getByTestId('task-estado'))
    .toHaveText('en progreso');
});
