from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date
from random import random
import os


class WtspBot:
    def __init__(self):
        chromedriver = 'chromedriver.exe'
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get('https://web.whatsapp.com')
        sleep(10)



    def send_msg_to(self, contact, msg, rep):
        self.driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(contact)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
        sleep(2)
        for i in range(rep):
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)






