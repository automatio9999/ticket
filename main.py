from os import getenv
from utils import write_spreadsheet 
from driver import setup_driver
from ticket import login_ticket, normalize, wait_loading_finish, get_main_data, get_ticket_data

def main():
    #username = getenv("ACCOUNT_USERNAME")
    #pwd = getenv("ACCOUNT_PASSWORD")
    username = "bdean@unitedconstructionservicesllc.com"
    password = "United2017!"
    driver = setup_driver(True)

    login_ticket(driver, username, password)
    wait_loading_finish(driver)
    data = get_main_data(driver)
    tickets = get_ticket_data(driver, data)
    driver.quit()

    normalized = normalize(tickets)
    write_spreadsheet("sample.xlsx", normalized)

if __name__ == "__main__":
    main()
