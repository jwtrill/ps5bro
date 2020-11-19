from selenium import webdriver
import time

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

# will cookies improve load time?
#options = webdriver.ChromeOptions()
#options.add_argument('user-data-dir=www.supremenewyork.com')

@timeme
def order():
    # add to cart
    driver.find_element_by_class_name('button spin-button prod-ProductCTA--primary button--primary').click()

    # wait for checkout button element to load
##    time.sleep(.5)
##    checkout_element = driver.find_element_by_class_name('button spin-button prod-ProductCTA--primary button--primary')
##    checkout_element.click()

    # fill out checkout screen fields
##    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
##    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
##    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
##    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
##    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
##    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
##    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
##    driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])


##    process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
##    process_payment.click()
##
##
if __name__ == '__main__':
    # load chrome
    driver = webdriver.Chrome('./chromedriver')

    # get product url
    driver.get("https://www.walmart.com/ip/Old-Spice-Body-Wash-for-Men-Timber-with-Sandalwood-25-fl-oz/839315548")
    ##add to cart button
    driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button').click()
    time.sleep(1)
    ##check out button
    driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]').click()
    time.sleep(1)
    ##enter email address
    driver.find_element_by_xpath('//*[@id="sign-in-email"]').send_keys('PUTEMAIL')
    ##enter password
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input').send_keys('PUTPASSWORD')
    ##sign in button
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/button').click()
    ##place order button
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button').click()
    

