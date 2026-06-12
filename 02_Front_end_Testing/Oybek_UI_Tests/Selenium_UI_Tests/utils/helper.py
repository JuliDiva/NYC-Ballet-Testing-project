import os
from datetime import datetime

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def create_driver(browser: str = "chrome"):
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.page_load_strategy = "eager"
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    return driver


def close_driver(driver):
    try:
        if driver:
            driver.quit()
    except Exception as e:
        print(f"Browser close failed: {e}")


def take_screenshot(driver, folder="screenshots_NYCB"):
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/error_{now}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")
    return path


def wait_for_element_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_element_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_url_contains(driver, text, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(text)
    )


def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def scroll_by(driver, pixels=500):
    driver.execute_script(f"window.scrollBy(0, {pixels});")