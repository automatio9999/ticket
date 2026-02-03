from os import getenv
from utils import write_spreadsheet 
from driver import setup_driver
from ticket import login_ticket, normalize, wait_loading_finish, get_main_data, get_ticket_data

def main():
    username = getenv("MY_USERNAME")
    password = getenv("MY_PASSWORD")
    if username and password:
        driver = setup_driver(True)
        login_ticket(driver, username, password)
        print("connected.")
        wait_loading_finish(driver)
        data = get_main_data(driver)
        tickets = get_ticket_data(driver, data)
        driver.quit()
        normalized = normalize(tickets)
        write_spreadsheet("sample.xlsx", normalized)
    else:
        print("username/password secrets not set.")

if __name__ == "__main__":
    main()
