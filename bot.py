

from selenium import webdriver
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstagramBot:
    def __init__(self, username, password):
        '''
        Creates an instagram bot instance
        :param username:string :The Instagram username for user
        :param password: string:The Instagram password for user

        '''
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.login()

        time.sleep(5)

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(2)
        accept_cookies_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Permite toate modulele cookie')]")
        accept_cookies_button.click()
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        enter = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        enter.click()
        time.sleep(5)
        # not_now = self.driver.find_element(By.XPATH, "//div[text()='Nu acum']")
        # not_now.click()
        # time.sleep(5)

    def nav_user(self,user):
        # search_button = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//svg[@aria-label='Caută']"))
        # )
        # search_button.click()
        # time.sleep(5)
        # search_input=self.driver.find_element(By.XPATH, "//input[@aria-label='Câmp text pentru căutare']")
        # search_input.send_keys(user)
        # search_input.send_keys(Keys.RETURN)
        self.driver.get('{}/{}'.format(self.base_url,user))
        time.sleep(5)

    def follow_user(self,user):
        self.nav_user(user)
        button = self.driver.find_element(By.XPATH, "//div[contains(@class, '_ap3a') and contains(@class, '_aaco')]")
        if button:
            button.click()
        time.sleep(5)

    def unfollow_user(self,user):
        self.nav_user(user)
        button=self.driver.find_element(By.XPATH,"//div[contains(text(),'Urmăreşti')]")

        if button:
            button.click()
            time.sleep(5)
            unfollow_buton=self.driver.find_element(By.XPATH, "//span[contains(text(),'Nu mai urmări')]")
            unfollow_buton.click()
            time.sleep(5)

if __name__ == '__main__':
    bot = InstagramBot("andrei.rotaru09", "Andrei921$")
    #bot.nav_user(user='lamineyamal')
    #bot.follow_user(user='juventus')
    bot.follow_user(user='lamineyamal')
