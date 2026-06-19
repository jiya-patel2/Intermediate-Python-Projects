from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv

FORM_URL = "https://forms.gle/8RFoi4inBWgy2d5H6" 
OPTIONS = webdriver.FirefoxOptions()
driver = webdriver.Firefox()
class FormFiller():
    def __init__(self) -> None :
        driver.get(url=FORM_URL)
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 2)

        def fill_link(self):
            address  = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div")
            rent_per_month = driver.find_element(by=By.XPATH,value= "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div")
            link = driver.find_element(by= By.XPATH, value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div')
            
            
           
