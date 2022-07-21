import undetected_chromedriver as uc
import time
import pickle

PATH = "/Users/aamoussa/Desktop/selenium/chromedriver"

if __name__ == '__main__':
	driver = uc.Chrome()

	driver.get("https://overseer.1337.ma/user/200")
	time.sleep(20)
	cokie = driver.get_cookies()
	print(cokie)
	pickle.dump(cokie, open("cokie.pkl", "wb"))
	time.sleep(60)

