from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

# here you fill in your myanimelist lgoin credentials
# they don't go anywhere dw this script is not made to steal login credentials in a weeb fantsy forum
username = "USERNAME_FILL_IN_HERE_AND_LEAVE_THE_QUOTATION_MARKS_INTACT"
password = "PASSWORD_FILL_IN_HERE_AND_LEAVE_THE_QUOTATION_MARKS_INTACT"

# as you can see the script is made for chrome browser and runs in default 100% magnification
driver = webdriver.Chrome()
driver.get("http://myanimelist.net/login.php?from=%2F")
page = driver.page_source
driver.maximize_window()
# DO NOT PUT YOUR CREDENTIALS BELOW THIS LINE ONLY IN THE PART ABOVE
login = driver.find_element_by_id("loginUserName")
login.send_keys(username)
time.sleep(1)
login = driver.find_element_by_id("login-password")
login.send_keys(password)
login.send_keys(Keys.ENTER)
time.sleep(1)

# in line 29 replace the link to my (Lux_Lucis) list page with the one redirecting to yours
# otherwise you'll be attempting to clean my list instead of your own... good luck with that.
# i left mine there as an example to clarify what the required link/page looks like and where to insert it
driver.get(
    "https://myanimelist.net/animelist/Lux_Lucis")
time.sleep(6)
driver.find_element_by_xpath(
    '//*[@id="gdpr-modal-bottom"]/div/div/div[2]/button').click()
time.sleep(5)

result = len(driver.find_elements_by_class_name(
    'list-item'))
print(f'No. of Rows: {result}')

for _ in range(result):
    driver.find_element_by_class_name(
        'edit').click()
    time.sleep(3)
    
    driver.switch_to_frame(
    'fancybox-frame')
    driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/div[3]/form/input').click()
    time.sleep(3)
    
    alert_obj = driver.switch_to.alert
    alert_obj.accept()
    time.sleep(3)

    delete = driver.refresh()
    delete = time.sleep(3)
# note that all the sleep functions above can be modified in order to make the script faster
# however it might result in a prompt requesting confirmation that you are not a bot
# idk how many of these you can tank before you are auto-banned
# at 2 second sleep intervals i've enocuntered it once after ~150 deleted entries 
# at 3 second intervals it was a smooth sailing
