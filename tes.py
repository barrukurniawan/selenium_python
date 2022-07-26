import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_a_success_login(self): 

    driver = self.driver
    driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
    time.sleep(3)
    driver.find_element(By.ID,"email").send_keys("tester@jagoqa.com") # isi email
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("testerjago") # isi password
    time.sleep(1)
    driver.find_element(By.ID,"signin_login").click()
    time.sleep(1)

    response_data = driver.find_element(By.ID,"swal2-title").text
    response_message = driver.find_element(By.ID,"swal2-content").text

    self.assertEqual(response_data, 'Welcome tester jago')
    self.assertEqual(response_message, 'Anda Berhasil Login')

