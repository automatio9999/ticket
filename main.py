import csv
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.os_manager import ChromeType

from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
def setup_driver(headless: bool = False) -> WebDriver:
    options = Options()

    if headless:
        options.add_argument("--headless=new")  # New headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Stealth options
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)

    # Performance options
    options.add_argument("--disable-images")
    # options.add_argument("--disable-javascript")  # Use carefully
    options.add_argument("--blink-settings=imagesEnabled=false")
    service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    return webdriver.Chrome(service=service, options=options)

def main():
    base = "https://md.itic.occinc.com/excavatorTickets"
    username = "bdean@unitedconstructionservicesllc.com"
    pwd = "United2017!"


    username_xpath = '//*[@id="username"]'
    pwd_xpath = '//*[@id="pass"]'
    login_xpath = '//*[@id="btn-login"]'

    driver = setup_driver(True)
    driver.get(base)
    #wait =  WebDriverWait(driver, 10)
    #username_elm = find_element_or_none(wait, username_xpath)
    #if username_elm:
    #    username_elm.send_keys(username)
    #pwd_elm = find_element_or_none(wait, pwd_xpath)
    #sleep(1.23)
    #if pwd_elm:
    #    pwd_elm.send_keys(pwd)
    #sleep(1.53)
    #login_btn = find_element_or_none(wait, login_xpath)

    #if login_btn:
    #    login_btn.click()
    ##sleep(5*60)
    #tickets = find_elements(WebDriverWait(driver, 5*60), '//*[@id="ExcavatorTicketTable"]/tbody/tr')
    #i = 0
    #data = []
    #if tickets:
    #    for t in tickets:
    #        if i == 20:
    #            break
    #        id = t.find_element(By.XPATH, './td[1]/a/text()')
    #        url = t.find_element(By.XPATH, './td[1]/a/@href')
    #        release = t.find_element(By.XPATH, './td[2]')
    #        response = t.find_element(By.XPATH, './td[3]')
    #        cross_street = t.find_element(By.XPATH, './td[5]')
    #        expire = t.find_element(By.XPATH, './td[8]')
    #        ticket = dict(id=id,url=url,release=release,response=response,cross_street=cross_street,expire=expire)
    #        data.append(ticket)
    #        i+=1

        #"miss_utility_date":"release_date",
        #"miss_should_clear":"response_due_date",
        #"miss_should_expire":"expire_date",
    fields = {
        "job_name": "VLSR",
        "cross_street": "5TH ST NW",
        "type_ticket": "STANDARD NXT",

        "status_history": [
            {"DCDOT01": "Not complete/In progress (Responded per folder placement.)"},
            {"MCI03": "Not yet responded"},
            {"PEPCODC": "Clear/No conflict"},
            # etc...
        ],
        "status": "open pending",
        "id_ticket":"26038654",
        "updated_id_ticket": "could not found for this one",
        "miss_utility_date": "01/16/26 08:05 pm",
        "miss_should_clear": "01/23/26 07:00 am",
        "miss_should_expire": "02/10/26 07:00 am",
        "expire_date_days": "36",
        "miss_clear_date": "date when all status history are markeClear/No Conflict (?)",
        "overdue_days": "TBD",
    }
    write_csv("data.csv", ["username","password"], [[username,pwd], ["azerty","123123"]])
    driver.quit()


def write_csv(filename:str, header: list[str], body: list[list[str]])->None:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)


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


def find_elements(wait: WebDriverWait, xpath: str) -> list[WebElement] | None:
    try:
        children = wait.until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath))
        )
        return children
    except:
        return None


if __name__ == "__main__":
    main()
