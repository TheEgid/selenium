from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium
import time


link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
try:

    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(15)

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(2)
    browser.quit()
