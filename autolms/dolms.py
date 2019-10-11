from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import *
import time
def automate(usernamefromuser, passwordfromuser):
    chrome_options = Options()
    #driver = webdriver.Chrome(options=chrome_options)
    chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    
    driver = webdriver.Chrome(r'/Users/balvinder/Documents/ring/chromedriver',options=chrome_options)

    driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=" +
               usernamefromuser+"&wantsurl=")
    #loginbtn = driver.find_element_by_id('loginbtn')
    # loginbtn.click()
    password = driver.find_element_by_id('password')
    password.send_keys(passwordfromuser)
    loginbtn = driver.find_element_by_id('loginbtn')
    loginbtn.click()
    driver.get('http://mydy.dypatil.edu/rait/blocks/academic_status/ajax.php?action=myclasses')
    table = driver.find_element_by_class_name('generaltable')
    soup = BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')
    trs = soup.find('tbody').find_all('tr')
    urllist=[]
    for tr in trs:
        a = tr.find('a')
        print(a)
        url=a['href']
        #print(url)
        
        #url=driver.current_url
        try:
            ind = url.rindex("=")
            idd=url[ind+1:]
            customurl="http://mydy.dypatil.edu/rait/course/customview.php?id="+idd
            driver.get(customurl)
            print(customurl)
        
            pendingurls = driver.find_elements_by_class_name('pending')
            time.sleep(2)
            for pending in pendingurls:
                urllist.append(pending.get_attribute('href'))
                #print(pending.get_attribute('href'))
                
        except Exception as e:
            print(e)
            print("error")
    for url in urllist:
        driver.get(url)
    driver.close()
