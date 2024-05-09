from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login = input("login:")
password = input("password:")

def manage_cookies(driver):
    cookies_xpath = "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
    conditions_popup = EC.presence_of_element_located((By.XPATH, cookies_xpath))
    decline_button = WebDriverWait(driver, 5).until(conditions_popup)
    print(decline_button)

    # decline_button = cookies_popup.find_element(By.XPATH, "/div/div[2]/div/button[2]")
    decline_button.click()
    print("cookies decline")

def log_in(driver):
    login = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
    password = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

    login.send_keys("lol")
    password.send_keys("1234" + Keys.ENTER)


def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get('https://www.instagram.com/')

    print(driver.title)
    manage_cookies(driver)
    log_in(driver)


    driver.quit()


if __name__ == "__main__":
    main()