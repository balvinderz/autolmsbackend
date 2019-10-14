from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import *
import time
import re
import uuid


def automate(usernamefromuser, passwordfromuser, doquiz, dodiscussionforum):
    chrome_options = Options()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(options=chrome_options)
    chrome_options.add_experimental_option(
        "prefs", {'profile.managed_default_content_settings.javascript': 2, "download.default_directory": "NUL", "download.prompt_for_download": False, })

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER PATH"), options=chrome_options)
    #driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=" +
               usernamefromuser+"&wantsurl=")
    # loginbtn = driver.find_element_by_id('loginbtn')
    # loginbtn.click()
    try:
        password = driver.find_element_by_id('password')
        password.send_keys(passwordfromuser)
    except:
        return "Invalid Email-id or Password"
    loginbtn = driver.find_element_by_id('loginbtn')
    loginbtn.click()
    time.sleep(2)
    if(driver.current_url != "http://mydy.dypatil.edu/rait/my/"):
        return "Invalid Email-id or Password"
    driver.get(
        'http://mydy.dypatil.edu/rait/blocks/academic_status/ajax.php?action=myclasses')
    table = driver.find_element_by_class_name('generaltable')
    soup = BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')
    trs = soup.find('tbody').find_all('tr')
    urllist = []
    for tr in trs:
        a = tr.find('a')
        # print(a)
        url = a['href']
        # print(url)

        # url=driver.current_url
        try:
            idd = re.findall("\d.*", url)[0]
            customurl = "http://mydy.dypatil.edu/rait/course/customview.php?id="+idd
            driver.get(customurl)
            print(customurl)

            pendingurls = driver.find_elements_by_class_name('pending')
            # time.sleep(2)
            for pending in pendingurls:
                urllist.append(pending.get_attribute('href'))
                # print(pending.get_attribute('href'))

        except Exception as e:
            print(e)
            print("error")
    for url in urllist:
        if("quiz" in url and doquiz == 1):
            try:
                inputbutton = driver.find_element_by_css_selector(
                    "#region-main > div:nth-child(3) > div.box.quizattempt > div > form > div > input[type=submit]:nth-child(1)")
                inputbutton.click()
                currenturl = driver.current_url
                attemptid = re.findall("\d.*\w", currenturl)[0]
                driver.get(
                    "http://mydy.dypatil.edu/rait/mod/quiz/summary.php?attempt="+attemptid)
                submitbutton = driver.find_elements_by_tag_name(
                    "form")[1].find_elements_by_css_selector("input[type=submit]")[0]
                submitbutton.click()
                continue
            except:
                continue
        elif("forum" in url and dodiscussionforum == 1):
            driver.get(url)
            try:
                button = driver.find_element_by_css_selector(
                    "#newdiscussionform > div > input[type=submit]:nth-child(2)")
                button.click()
                subject = driver.find_element_by_id("id_subject")
                subject.send_keys(".")
                message = driver.find_element_by_id("id_message")
                message.send_keys(".")
                submitbutton = driver.find_element_by_id("id_submitbutton")
                submitbutton.click()

                continue
            except:
                continue
        driver.get(url)
    driver.close()
    return "Done"


#automate("nis.ash.rt17@rait.ac.in", "dypatil@123")
