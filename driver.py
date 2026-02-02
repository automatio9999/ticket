from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.os_manager import ChromeType


def safe_element_located(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        return None

def find_element_or_none(wait: WebDriverWait, selector: str) -> WebElement | None:
    try:
        elm = wait.until(EC.presence_of_element_located((By.XPATH, selector)))
        return elm
    except:
        return None

def get_text(wait: WebDriverWait, xpath: str) -> str | None:
    try:
        elm = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return elm.text.strip()
    except:
        print(f"xpath not found {xpath}")
        return None

def click_btn(wait: WebDriverWait, xpath: str) -> None: 
    try:
        children = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        children.click()
    except:
        pass

def find_elements(wait: WebDriverWait, xpath: str) -> list[WebElement] | None:
    try:
        children = wait.until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath))
        )
        return children
    except:
        return None

def setup_driver(headless: bool = False) -> WebDriver:
    options = Options()
    if headless:
        options.add_argument("--headless=new")  # New headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    #options.add_argument("--disable-images")
    #options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    return webdriver.Chrome(service=service, options=options)


