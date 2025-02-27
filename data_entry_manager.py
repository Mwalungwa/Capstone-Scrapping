import time

from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver.common.by import By


class DataEntryManager:

    def __init__(self):
        self.driver = None
        self.chrome_options = None

    def start_session(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url)
        time.sleep(3)

    def fill_form(self,address,price,link):
        address_entry = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_entry.send_keys(address)
        # time.sleep(10)
        price_entry = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_entry.send_keys(price)
        # time.sleep(10)
        link_entry = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_entry.send_keys(link)
        # time.sleep(10)
        submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()
        time.sleep(3)

    def close_session(self):
        self.driver.close()





