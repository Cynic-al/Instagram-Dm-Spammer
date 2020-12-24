import PySimpleGUI as sg

from time import sleep

from selenium import webdriver

layout = [[sg.Text('Enter your username:') , sg.Input(key = '--Input1--')],
[sg.Text('Enter your password:') , sg.Input(key = '--Input2--')] ,
[sg.Text('Enter the other user:') , sg.Input(key = '--Input3--')] ,
[sg.Text('Enter your message:') , sg.Input(key = '--Input4--')],
[sg.Text('How many times do you want to send this message?: ') , sg.Input(key = '--Input5--')] ,
[sg.Text('Username',key = '--Output1--')] ,
[sg.Text('Password',key = '--Output2--')] ,
[sg.Text('Other user',key = '--Output3--')] ,
[sg.Text('Message', key = '--Output4--')] ,
[sg.Text('Amount' , key = '--Output5--')] ,
[sg.Button('OK') , sg.Button('Exit')] ,
[sg.Text('You must close the window for the program to finish')]] 


window = sg.Window('Instagram Dm Spammer' , layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    window['--Output1--'].update(values['--Input1--']) ,
    window['--Output2--'].update(values['--Input2--']) , 
    window['--Output3--'].update(values['--Input3--']) , 
    window['--Output4--'].update(values['--Input4--']) ,
    window['--Output5--'].update(values['--Input5--']) 
    if event == 'OK':
        username = values['--Input1--']  
        password = values['--Input2--']
        user = values['--Input3--']
        message = values['--Input4--']
        spam_amount = int(values['--Input5--'])

window.close()

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

    for i in range(spam_amount):
        type_dm = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        type_dm.click()
        type_dm.send_keys(message)

        send = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        send.click()

login(username , password)
homepage()
dms_(user, spam_amount , message)

browser.close()