from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from dotenv import load_dotenv
import os
import time

load_dotenv()

PROMISED_DOWN=2
PROMISED_UP=10
CHROME_DRIVER_PATH = "D:\Development\chromedriver.exe"
TWITTER_EMAIL=os.getenv('twitter_mail')
TWITTER_PASSWORD=os.getenv('twitter_password')

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])




class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options,)
        
        
        self.up=0
        self.down=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        sleep(3)
        Accept=self.driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
        Accept.click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(80)
        self.down=float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(f'THIS IS THE DOWNLOAD {self.down}')
        self.up=float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f'THIS IS THE {self.up}')
        self.driver.quit()
        
    
    
    
    print(TWITTER_EMAIL)
    def tweet_at_provider(self):
        self.driver1= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver1.get('https://twitter.com/i/flow/login')
        sleep(2)
        self.driver1.maximize_window()
        
        self.email=WebDriverWait(self.driver1,10).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="text"]')))
        #try:
        #    self.email=WebDriverWait(self.driver1,10).until(EC.presence_of_element_located((By.XPATH,'//input[@autocomplete="username"]')))
        #finally:
        #    self.driver1.quit()
        
        self.email.send_keys(TWITTER_EMAIL)
        sleep(5)
        self.forward1=self.driver1.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        self.forward1.click()
        sleep(5)
        self.login_pass=self.driver1.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.login_pass.send_keys(TWITTER_PASSWORD)
        self.login_button=self.driver1.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        self.login_button.click()
        sleep(3)
        self.tweet_box=self.driver1.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        if self.down<2:
            self.tweet_box.sendKeys(f'@turkcellsuperonline, hızım {self.up}Mbit, yavaşsın bro')
            self.driver1.find_element(By.CLASS,'css-18t94o4')

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()