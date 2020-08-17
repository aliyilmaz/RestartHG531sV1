#!/usr/bin/python

def RestartHG531sV1(url, username, password):
    
    from time import sleep
    from selenium import webdriver

    browser = webdriver.Chrome("./chromedriver")    
    browser.delete_all_cookies()
    browser.get(url)
    
    UsernameField = browser.find_element_by_name("Username")
    PasswordField = browser.find_element_by_name("Password")

    UsernameField.send_keys(username)
    PasswordField.send_keys(password)

    browser.find_element_by_id('btnLogin').click()
    sleep(2)
    browser.get(url+'html/management/reset.asp')
    browser.find_element_by_name('btnReboot').click()
    browser.switch_to.alert.accept()
    print('The modem is restarted.')
    sleep(50)
    
    browser.close()
    
RestartHG531sV1('http://192.168.1.1/', 'vodafone', 'vodafone')