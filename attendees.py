
"""
You will see so many time.sleep(). It is because my internet so slow hahahah. You can adjust this.
"""

import sys, time
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
except:
    msg = "Please install all the requirements, pip install -r requirements.txt"
    print(msg)
    sys.exit(msg)

email_login = "your email login"
password_login = "your password login"
attendance_lists = "attendees.txt" #using coma as delimiter

event_id = "your event id" #open your event url, and see ?eid at the end of url, eg https://www.eventbrite.com.au/myevent?eid=123456
ticket_id = "your quantity id" #use inspect element, and see id for this column. detail on readme


fp = webdriver.FirefoxProfile()
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("https://www.eventbrite.com.au/attendees-add?eid=" + str(event_id))
email = browser.find_element(By.ID , "email")
password = browser.find_element(By.ID ,"password")
email.send_keys(email_login)
password.send_keys(password_login)
loginButton =browser.find_element(By.XPATH , '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div/form/div[4]/div/button')

time.sleep(2)
loginButton.click()
time.sleep(5)


# open file attencance.txt and iterate
with open(attendance_lists) as file:
    lines = file.readlines()
    # this will processing the attendees one by one
    for line in lines:
        tokens = line.split(",")
        firstname = tokens[0]
        surname = tokens[1]
        email = tokens[2]
        print("processing " + firstname + " " + surname + " (" + email + ")")            
        try:
            browser.get("https://www.eventbrite.com.au/attendees-add?eid=" + str(event_id))
            time.sleep(3)
            quantity = browser.find_element(By.ID,ticket_id)
            quantity.send_keys("1")
            continueBtn = browser.find_element(By.XPATH ,"/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/section/section/form/div[3]/a")
            time.sleep(2)
            continueBtn.click()
            time.sleep(3)
            iframe = browser.find_element(By.TAG_NAME,"iframe")
            time.sleep(1)
            browser.switch_to.frame(iframe)
            time.sleep(5)
            html = browser.find_element(By.TAG_NAME,'html')
            time.sleep(1)
            uname1 = browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/form/div[1]/div/div/div[2]/div/div[1]/div/div/input")
            uname1.send_keys(firstname)
            browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/form/div[1]/div/div/div[3]/div/div/div/div/input").send_keys(surname)
            browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/form/div[1]/div/div/div[4]/div/div/div/div/input").send_keys(email)
            time.sleep(1)
            browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/form/div[2]/div/div/div[1]/div/div/div/div/input").send_keys(firstname)
            browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/form/div[2]/div/div/div[2]/div/div/div/div/input").send_keys(surname)
            browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[1]/div/div[1]/form/div[2]/div/div/div[3]/div/div/div/div/input").send_keys(email)
            html.send_keys(Keys.END)
            register = browser.find_element(By.XPATH ,"/html/body/div/div/div/div[1]/div/main/div/div[2]/div/nav/div[1]/button")
            time.sleep(1)
            register.click()
            time.sleep(3)       
            browser.switch_to.default_content()
            time.sleep(15) 
            print("Done processing " + firstname + " " + surname + " (" + email + ")")
        except Exception as e:
            print(e)
            print("Error while processing" + firstname + " " + surname)

browser.close()