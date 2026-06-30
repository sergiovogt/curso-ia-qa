import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:5000/login');
  await page.getByTestId('login-user').click();
  await page.getByTestId('login-user').fill('demo');
  await page.getByTestId('login-user').press('Tab');
  await page.getByTestId('login-password').fill('demo');
  await page.getByTestId('login-submit').click();
  await page.getByRole('row', { name: '1 Validar login con' }).getByTestId('task-select').selectOption('en progreso');
});