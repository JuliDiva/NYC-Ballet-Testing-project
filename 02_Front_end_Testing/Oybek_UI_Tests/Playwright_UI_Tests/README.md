# Playwright UI Tests - NYC Ballet Shop

This project contains automated UI tests for the NYC Ballet Shop website.

## Tech Stack

- Playwright
- TypeScript
- Page Object Model (POM)
- VS Code

## Project Structure

```txt
pages/
tests/
playwright.config.ts
package.json
```

## How to Run Tests

Install dependencies:

```bash
npm install
```

Run all tests:

```bash
npx playwright test
```

Run tests with browser visible:

```bash
npx playwright test --headed
```

Open test report:

```bash
npx playwright show-report
```

## Test Coverage

- Homepage navigation
- Product listing
- Product sorting
- Product filtering
- Product cards validation
- Out of stock product validation
- Currency validation
- Duplicate product validation

## Author

Oybek Moonbek

QA Automation Engineer

GitHub: https://github.com/<your-github>