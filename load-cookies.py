import undetected_chromedriver as uc
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

PATH = "/Users/aamoussa/Desktop/selenium/chromedriver"
dict = {}
if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://overseer.1337.ma/user/122")
    cookies = pickle.load(open("cokie.pkl", "rb"))
    for cookie in cookies :
        driver.add_cookie(cookie)
    driver.get("https://overseer.1337.ma/user/122")
    time_spent = driver.find_element(By.ID , "__next")
    text = time_spent.text
    result = text.split('\n')
    time_spent = result[5].replace(' days were spent on the common core', '')
    dict['time_spent'] = time_spent
    json_object = json.dumps(dict, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    # driver.get("https://discord.com/channels/788078738905628682/884398456641298472")
    # cookies = pickle.load(open("discord_cokie.pkl", "rb"))
    # for cookie in cookies :
    #     driver.add_cookie(cookie)
    # driver.get("https://discord.com/channels/788078738905628682/884398456641298472")
    time.sleep(60)

    
