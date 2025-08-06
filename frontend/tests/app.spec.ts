import { test, expect } from '@playwright/test';

test.describe('SF Mobile Food Facilities App', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:5173');
  });

  test('renders the food facilities list', async ({ page }) => {
    await page.waitForSelector('.ant-list-item'); // wait for list items
    const items = await page.locator('.ant-list-item').all();
    expect(items.length).toBeGreaterThan(0);
  });

  test('can search by applicant name', async ({ page }) => {
    await page.waitForSelector('.ant-input-search'); // wait for input

    const searchInput = page.locator('input[placeholder="Search by applicant or street name"]');
    await searchInput.fill('TACO');
    await page.waitForTimeout(1000); 

    const results = await page.locator('.ant-list-item');
    expect(await results.count()).toBeGreaterThanOrEqual(1);
  });

  test('can search by partial address', async ({ page }) => {
    const searchInput = page.locator('input[placeholder="Search by applicant or street name"]');
    await searchInput.fill('SAN');
    await page.waitForTimeout(1000);
    const results = await page.locator('.ant-list-item');
    expect(await results.count()).toBeGreaterThanOrEqual(1);
  });

  test('can filter by status', async ({ page }) => {
    const statusSelect = page.getByRole('combobox');
    await statusSelect.click();

    // Wait for dropdown to appear and show items
    const dropdown = page.locator('.ant-select-dropdown');
    await expect(dropdown).toBeVisible();

    // Target the first visible option with APPROVED text
    const approvedOption = dropdown.locator('.ant-select-item-option', { hasText: 'APPROVED' }).first();
    await expect(approvedOption).toBeVisible();
    await approvedOption.click();

    // Wait for filtering to apply
    await page.waitForTimeout(1000);

    const results = await page.locator('.ant-list-item');
    const count = await results.count();
    expect(count).toBeGreaterThanOrEqual(1);

    // Since there can be 100s of results, we wil be checking only first 5 for assertion
    const itemsToCheck = Math.min(5, count);
    for (let i = 0; i < itemsToCheck; i++) {
      const text = await results.nth(i).textContent();
      expect(text).toContain('APPROVED');
    }
  });

  test('shows no result message if search yields nothing', async ({ page }) => {
    const searchInput = page.locator('input[placeholder="Search by applicant or street name"]');
    await searchInput.fill('zzzzzzzz');
    await page.waitForTimeout(500);
    await expect(page.getByText('No food facilities found.')).toBeVisible();
  });
});
