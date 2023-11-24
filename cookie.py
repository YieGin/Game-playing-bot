from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
cookie_total = driver.find_element(By.ID, 'money')

# Define upgrade elements
upgrades = {
    'buyCursor': 15,
    'buyGrandma': 100,
    'buyFactory': 500,
    'buyMine': 2000,
    'buyShipment': 7000
}

purchased_upgrades = {key: False for key in upgrades}  # Track purchased upgrades


end_time = time.time() + 1000  # 100 seconds from now
while time.time() < end_time:
    cookie.click()
    
    # Check and convert the total cookies to an integer
    total_cookies = int(cookie_total.text.replace(',', ''))  # Removing commas for conversion

    # Iterate over upgrades to check if any can be purchased
    for upgrade_id, cost in upgrades.items():
        if total_cookies >= cost and not purchased_upgrades[upgrade_id]:
            driver.find_element(By.ID, upgrade_id).click()
            purchased_upgrades[upgrade_id] = True
            break  # break the loop after purchasing an upgrade
