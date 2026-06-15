#  NYC Ballet Shop – Selenium UI Automation Project

Automated UI testing project for the NYC Ballet Shop website built with Python, Selenium WebDriver, unittest, and the Page Object Model (POM) framework.

This project demonstrates practical QA Automation skills including UI validation, cross-browser testing, reusable page objects, explicit waits, and test organization following industry best practices.

---

##  Tech Stack

- Python
- Selenium WebDriver
- unittest
- WebDriver Manager
- Page Object Model (POM)
- Cross-Browser Testing
- Git & GitHub
- CI/CD Fundamentals

---

##  Project Structure

```text
Selenium_UI_Tests/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── collection_page.py
│   └── product_page.py
│
├── tests/
│   └── test_crossbrowser.py
│
├── utils/
│   └── helper.py
│
└── README.md
```

---

##  Test Coverage

### Positive Tests

- Verify "View All" button functionality
- Verify collection page navigation
- Verify product sorting functionality
- Verify availability filter behavior
- Verify Add to Cart button visibility
- Verify product count display

### Negative Tests

- Verify products without names are not displayed
- Verify products without images are not displayed
- Verify unavailable products cannot be added to cart
- Verify correct currency symbol formatting
- Verify duplicate products are not displayed

---

##  Cross-Browser Testing

The test suite successfully runs on:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

---

## ️ Installation

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
.venv/bin/python -m pip install selenium webdriver-manager
```

---

##  Run Tests

Run Chrome tests:

```bash
.venv/bin/python -m unittest tests.test_crossbrowser.ChromeNYCBShopTest
```

Run all cross-browser tests:

```bash
.venv/bin/python -m unittest tests.test_crossbrowser
```

---

##  Latest Results

```text
Browsers Tested: Chrome, Edge, Firefox
Total Tests: 30
Result: PASSED 
```

---

##  Framework Features

- Page Object Model (POM)
- Reusable page methods
- Explicit waits
- Cross-browser execution
- Clean test architecture
- Easy scalability
- Maintainable code structure

---

##  Author

**Oybek Tashpulatov**

QA Automation Engineer

Skills:
- Selenium WebDriver
- Python
- API Testing
- UI Testing
- Test Automation Framework Design
- CI/CD Fundamentals
- Git & GitHub