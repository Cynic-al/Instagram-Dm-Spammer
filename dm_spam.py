from time import sleep

from selenium import webdriver

browser = webdriver.Firefox()

browser.implicitly_wait(5)

def login(username,password):
    browser.get('https://www.instagram.com/')

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_botton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    login_botton.click()

def homepage():
    not_now = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    not_now.click()

    not_now_notification = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    not_now_notification.click()

def dms_(user,spam_amount,message):
    dms = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div")
    dms.click()

    compose_dm = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button")
    compose_dm.click()

    reciver = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")
    reciver.click()
    reciver.send_keys(user)

    user_ = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div")
    user_.click()

    next_button = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div")
    next_button.click()

    for i in range(spam_amount, message):
        type_dm = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        type_dm.click()
        type_dm.send_keys(message)

        send = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        send.click()

login("username" , "password")
homepage()
dms_("user you want to spam" , amount of dms you want to send, "the message")