import pytest
import psycopg2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_report_dir = "allure-results"

@pytest.fixture(scope="session")
def db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="postgres",
        user="postgres",
        password="secret"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            status VARCHAR(50) 
            )
    """)
    conn.commit()

    yield conn
    conn.close()
