import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

MEET_URL = "https://meet.google.com/zsb-pvun-ugk"

def join_meeting():
    print("Launching browser...")
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")  # comment this if you want to see the browser

    prefs = {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.notifications": 1
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(options=options)
    driver.get(MEET_URL)

    print("Waiting for meeting to start...")
    joined = False
    while not joined:
        try:
            join_button = driver.find_element(By.XPATH, '//button[contains(@jsname,"Qx7uuf")]')
            join_button.click()
            print("Joined the meeting.")
            joined = True
        except:
            print("Meeting not yet started. Retrying in 60 seconds...")
            time.sleep(60)
            driver.refresh()

if __name__ == "__main__":
    join_meeting()
