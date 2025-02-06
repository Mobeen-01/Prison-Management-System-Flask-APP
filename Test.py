from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r'chromedriver')

driver.get('http://localhost:8000')
time.sleep(4)
driver.close()
driver = webdriver.Chrome(executable_path=r'chromedriver')
driver.get('http://localhost:8000/home')
time.sleep(4)
driver.close()
driver = webdriver.Chrome(executable_path=r'chromedriver')
driver.get('http://localhost:8000/Product')
time.sleep(4)
driver.close()
driver = webdriver.Chrome(executable_path=r'chromedriver')
driver.get('http://localhost:8000/Location')
time.sleep(4)
driver.close()
driver = webdriver.Chrome(executable_path=r'chromedriver')
driver.get('http://localhost:8000/ProductMovement')
time.sleep(4)
driver.close()
