from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import smtplib

def watchVaccine(user, pwd, zips, number, carrier, fromEmail, fromEmailPass):
    hasBeenSeen = {}
    for zipCode in zips:
        hasBeenSeen[zipCode] = False

    driver = webdriver.Chrome()
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19")
    btn = driver.find_element_by_css_selector('span.btn.btn__blue')
    btn.click()

    # Location screening page
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")

    element = driver.find_element_by_id("inputLocation")
    element.clear()
    element.send_keys(zipCode)
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    print('before')
    button2 = driver.find_element_by_css_selector('span.btn.btn__blue')
    print('after')
    button2.click()

    # login page
    driver.get("https://www.walgreens.com/login.jsp?ru=%2Ffindcare%2Fvaccination%2Fcovid-19%2Feligibility-survey%3Fflow%3Dcovidvaccine%26register%3Drx")
    element2 = driver.find_element_by_id("user_name")
    element2.clear()
    element2.send_keys(user)
    element3 = driver.find_element_by_id("user_password")
    element3.clear()
    element3.send_keys(pwd)
    time.sleep(2)
    signin = driver.find_element_by_id("submit_btn")
    signin.click()

    # --- Login blocked here

    # Eligibility page
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/eligibility-survey?flow=covidvaccine&register=rx")
    checkbox0 = driver.find_element_by_id("sq_100i_0")
    checkbox0.click()
    checkbox1 = driver.find_element_by_id("eligibility-check")
    checkbox1.click()

    
    # Vaccine screening page
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/appointment/screening")
    checkbox2 = driver.find_element_by_id("sq_100i_1")
    checkbox2.click()
    checkbox3 = driver.find_element_by_id("sq_102i_1")
    checkbox3.click()
    checkbox4 = driver.find_element_by_id("sq_103i_1")
    checkbox4.click()
    checkbox5 = driver.find_element_by_id("sq_104i_1")
    checkbox5.click()
    button3 = driver.find_element_by_css_selector("input.sv_complete_btn")
    button3.click()
    
    # Results & confirms search
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/appointment/screening/results-eligible/")
    button4 = driver.find_element_by_id("hn-startVisitBlock-gb-terms")
    button4.click()

    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/appointment/patient-info")
    checkbox6 = driver.find_element_by_id('dose1')
    checkbox6.click()
    
    # refresh to find availability
    # while True:
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/appointment/next-available")
    searchbtn = driver.find_element_by_css_selector('span.icon.icon__search.storeSearchIcon')
    searchbtn.click()

    time.sleep(0.75)
    alertElement = driver.find_element_by_css_selector("p.mb10")
    vaccine_message = alertElement.text
    print(vaccine_message)

    # Add part for sending text


def sendText(number, carrier, fromEmail, fromEmailPass, message):
    carriers = {
        'att': '@mms.att.net',
        'tmobile': ' @tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@pm.sprint.com'
    }

    to_number = number+'{}'.format(carriers[carrier])
    Subject = 'Subject: Covid Vaccine:\n\n'
    conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    conn.ehlo()
    conn.login(fromEmail, fromEmailPass)
    conn.sendmail(fromEmail, to_number, Subject + message)
    conn.quit()


if __name__ == "__main__":
    watchVaccine(user, pwd, zips, phone_num, carrier, from_email,  passw)
