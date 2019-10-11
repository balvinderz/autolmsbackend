from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import *


def automate(usernamefromuser, passwordfromuser):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    # driver.get("http://mydy.dypatil.edu/")
    #username = driver.find_element_by_id("username")
    # username.send_keys(usernamefromuser)
    driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=" +
               usernamefromuser+"&wantsurl=")
    #loginbtn = driver.find_element_by_id('loginbtn')
    # loginbtn.click()
    password = driver.find_element_by_id('password')
    password.send_keys(passwordfromuser)
    loginbtn = driver.find_element_by_id('loginbtn')
    loginbtn.click()
    table = driver.find_element_by_class_name('generaltable')
    soup = BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')
    trs = soup.find('tbody').find_all('tr')
    for tr in trs:
        a = tr.find('a')
        driver.get(a['href'])

    driver.close()
