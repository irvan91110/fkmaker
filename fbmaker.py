from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import random 
import time


def SetupSelenium():
    ##
    binary = FirefoxBinary("firefox/firefox.exe")
    selenium = r"Firefox/geckodriver.exe"
    ##
    firefox_profile = webdriver.FirefoxProfile("firefox/profile")
    firefox_profile.set_preference(
        "general.useragent.override",
        "[Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36.]",
    )
    browser = webdriver.Firefox(
        executable_path=selenium, firefox_binary=binary, firefox_profile=firefox_profile
    )
    ##
    browser.delete_all_cookies()
    return browser

def fullnamegen():
    global fullname 
    firnamelist = ["adam", "Scott", "Michael", "Andrew", "Mark", "Fernando", "Faith", "Steve", "Lee", "Amani", "Liv", "Nick A", "James", "Jake", "Brett", "Graham", "Fraser", "Jacob", "Chelsea", "Phil", "George", "Charley", "Emma", "Steph"]
    lastnamelist = ["andiva", "arista", "nasution"]
    first = random.choice(firnamelist)
    last = random.choice(lastnamelist)
    fullname = first + " " + last 


def clicks(css):
    browser.find_element_by_class_name(css).click()

def dropdown(ids,text,type):
    ##
    if type == 1 :   
        Select(browser.find_element_by_xpath("//select[@id='"+ ids + "']")).select_by_visible_text(text)
    elif  type == 2:
        Select(browser.find_element_by_xpath("//select[@id='"+ ids + "']")).select_by_index(text)
    elif type == 3:
         Select(browser.find_element_by_xpath("//select[@id='"+ ids + "']")).select_by_index(text)

def login(email, password, nomerhp):
    browser.get("https://touch.facebook.com/reg/?cid=103")
    time.sleep(2)
    ##fullname
    fullnamegen()
    browser.find_element_by_id("firstname_input").send_keys(fullname)
    clicks('_54k8')
    
    time.sleep(2)
    ##BIRTH DATE 
    dropdown('year',str(random.randrange(1980,2002)),1)
    dropdown('month',str(random.randrange(0,11)),2)
    dropdown('day',str(random.randrange(0,28)),2)
    clicks('_54k8')

    ##phone number
    browser.find_element_by_id("contactpoint_step_input").send_keys('+6285156540536')
    clicks('_54k8')

    ##jenis kelamin
    browser.find_element_by_class_name("_15db").click()
    clicks('_54k8')

    ##Katasandi
    browser.find_element_by_id("password_step_input").send_keys('Irvaners123')
    browser.find_element_by_name('submit').click()

    print(browser.find_elements_by_xpath("//*[contains(text(), 'Please enter a valid phone number.')]"))







browser = SetupSelenium()
wait = WebDriverWait(browser, 120)


email = "email"
password = "password"
nomerhp = 
login(email, password, nomerhp)
