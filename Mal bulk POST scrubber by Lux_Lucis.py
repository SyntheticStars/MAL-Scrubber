from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

# here you fill in your myanimelist lgoin credentials
# they don't go anywhere dw this script is not made to steal login credentials in a weeb fantsy forum
username = "USERNAME_FILL_IN_HERE_AND_LEAVE_THE_QUOTATION_MARKS"
password = "PASSWORD_FILL_IN_HERE_AND_LEAVE_THE_QUOTATION_MARKS"

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

# in line 29 replace the link to my own recent messages page with the one redirecting to yours
# otherwise you'll be attempting to clean my posts instead of your own
# i left mine there as an example to clarify what the required link/page looks like
driver.get(
    "https://myanimelist.net/forum/search?u=Lux_Lucis&q=&uloc=1&loc=-1")
time.sleep(6)
driver.find_element_by_xpath(
    '//*[@id="gdpr-modal-bottom"]/div/div/div[2]/button').click()
driver.find_element_by_xpath(
    '//*[@id="content"]/div/form/div[2]/input').click()
time.sleep(5)

result = len(driver.find_elements_by_css_selector(
    '#forumTopics tbody > tr')) - 1
print(f'No. of Rows: {result}')

# in line 51 after tbody/tr[START DELETING FROM THIS POST] post the row number inside the sq brackets
# it should be a number from 1 to 50 since only 50 of your last posts are displayed at a time
# each post is in a speparate row
# topics can only be deleted by the topic starter within 30 minutes of posting
# some posts deleted by mods remain in the catalgued search results but that just mal being mal
# skip over the row with your topic once the script reaches it and crashes
# skip over the row with posts deleted by mods
# you may have more posts left in your counter if you've posted in clubs
for _ in range(result):
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[3]/div[2]/div/table/tbody/tr[1]/td[2]/a').click()
    time.sleep(1.5)
    
    shitposts = len(driver.find_elements_by_class_name(
        'deletePost'))
    print(f'No. of Posts: {shitposts}')
    
    posts = driver.find_elements_by_class_name(
        'deletePost')
    
    for element in posts:
        # everything at this level of indentation will execute the tango
        # inside this second loop don't change anything unless you KNOW what you're doing
        element.click()
        delete = time.sleep(1)
        delete = driver.find_element_by_class_name(
            'yes').click()
        delete = time.sleep(2.5)

    delete = driver.back()
    delete = time.sleep(1.5)
    delete = driver.refresh()
    delete = time.sleep(2.5)
# note that all the sleep function can be modified in order to make choke points looser
# this is in case mal is slow to repond or your network sucks
# they can also be set a negligible value if you have gigabit network and mal is not being mal
# 1 stands for 1 second and you can use the decimal dot for things like 0.1 or 10.5

# final thing to note is that some quote towers / huge pics / popups and network issues can intercept clicks
# the script will crash but all you have to do is rerun it and see if the issue occurs again then fix 
# whatever it is that is interfering in the browser
# there is no need to change anything in the code for it to work it has successfully deleted over 5.5k messages
# however you can feel free to improve it with new fucntions or fine-tune it to account for posts deleted by mods
# and to skip over threads made by you