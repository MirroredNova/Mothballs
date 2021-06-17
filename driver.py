import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = 'C:\\Users\\aneth\\Desktop\\PycharmWorkspace\\webdrivers\\chromedriver.exe'
url = 'https://www.youtube.com/watch?v=F7SP7w_EUU4&feature=emb_logo'
directory = 'C:\\Users\\aneth\\Desktop\\Moth_Screenshots\\'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

def run():
    try:
        driver.get(url)
        body = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        body.send_keys('f')
        body.send_keys(Keys.SPACE)

        container = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[id='movie_player'] > div > video")))

        time.sleep(2)
        now = datetime.now()
        image_name = directory + "MothLivestream" + now.strftime("%Y-%m-%d_%H%M%S") + ".png"
        container.screenshot(image_name)
        print("Image saved to: " + image_name)

    except Exception:
        run()
    finally:
        driver.close()
        sys.exit()

run()