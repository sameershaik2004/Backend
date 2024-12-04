from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

class TodoE2ETests:
    @staticmethod
    def test_create_task():
        driver.get("http://127.0.0.1:8000/admin/")
        # Log in to Django Admin
        driver.find_element(By.ID, "id_username").send_keys("admin")
        driver.find_element(By.ID, "id_password").send_keys("password", Keys.RETURN)
        time.sleep(2)
        # Create task actions here...
        # Extend for View, Update, Delete
