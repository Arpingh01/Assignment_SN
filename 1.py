from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driverpath = "C:\\Users\\DELL\\OneDrive\\Desktop\\SoftNerve\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"
service = Service(driverpath)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    driver.get(url)

    # Wait for the content to load
    wait = WebDriverWait(driver, 10)
    content = wait.until(EC.presence_of_element_located((By.ID, "mw-content-text")))

    # Resize the window to full height of the page to capture complete screenshot
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, scroll_height)
    time.sleep(2)  # Wait to apply resize

    # Take full-page screenshot
    driver.save_screenshot("chapter1_screenshot.png")
    print("chapter1_screenshot.png")

    # Extract chapter text
    chapter_text = content.text

    # Save the text to a file
    with open("chapter1_text.txt", "w", encoding="utf-8") as f:
        f.write(chapter_text)
    print("chapter1_text.txtgit init")

finally:
    time.sleep(2)
    driver.quit()


