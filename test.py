from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

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
    ## ps5 disc edition link https://www.walmart.com/ip/PlayStation5-Console/363472942
    ##reload pickle cookie, but doesn't seem to work
    for cookie in pickle.load(open("./penis.pkl", "rb")):
         driver.add_cookie(cookie)
    def waitXpath(xpath):
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def waitClass(className):
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, className)))

    def waitSelector(selector):
        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))


##waits because walmart sucks giant donkey balls
##add to cart button
    ##waitXpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button')    
    ##driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button').click()
    #add-on-atc-container > div:nth-child(1) > section > div.valign-middle.display-inline-block.prod-product-primary-cta.primaryProductCTA-marker > div.prod-product-cta-add-to-cart.display-inline-block > button
    waitSelector('#add-on-atc-container > div:nth-child(1) > section > div.valign-middle.display-inline-block.prod-product-primary-cta.primaryProductCTA-marker > div.prod-product-cta-add-to-cart.display-inline-block > button')
    driver.find_element_by_css_selector('#add-on-atc-container > div:nth-child(1) > section > div.valign-middle.display-inline-block.prod-product-primary-cta.primaryProductCTA-marker > div.prod-product-cta-add-to-cart.display-inline-block > button').click()

##check out button
    waitSelector('#cart-root-container-content-skip > div:nth-child(1) > div > div.Cart-PACModal.standard-pac.pac-added.pac-new-ny.no-price-fulfillment.pac-vanilla-hf > div > div > div > div > div.Cart-PACModal-Body-right-rail.Grid-col.u-size-1.u-size-1-2-m.u-size-1-2-l > div > div > div.Grid-col.u-size-1-2.pos-actions-container > div.cart-pos-main-actions.s-margin-top > div.new-ny-styling.cart-pos-proceed-to-checkout > div > button.button.ios-primary-btn-touch-fix.hide-content-max-m.checkoutBtn.button--primary')
    driver.find_element_by_css_selector('#cart-root-container-content-skip > div:nth-child(1) > div > div.Cart-PACModal.standard-pac.pac-added.pac-new-ny.no-price-fulfillment.pac-vanilla-hf > div > div > div > div > div.Cart-PACModal-Body-right-rail.Grid-col.u-size-1.u-size-1-2-m.u-size-1-2-l > div > div > div.Grid-col.u-size-1-2.pos-actions-container > div.cart-pos-main-actions.s-margin-top > div.new-ny-styling.cart-pos-proceed-to-checkout > div > button.button.ios-primary-btn-touch-fix.hide-content-max-m.checkoutBtn.button--primary').click()
    ##waitXpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]')    
    ##driver.find_element_by_xpath('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]').click()
    
    ##enter email address
    #driver.find_element_by_xpath('//*[@id="sign-in-email"]').send_keys('')
    ##enter password
    #driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[2]/div/div[1]/label/div[2]/div/input').send_keys('')
    ##sign in button
    #driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[4]/div/section/div/section/form/div[5]/button').click()
    #time.sleep(2)
    ##pickle.dump(driver.get_cookies(), open("./penis.pkl", "wb")) 

##continue button
    ##waitXpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/button')    
    ##driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/button').click()
    waitSelector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(1) > div > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div.CXO_fulfillment_continue > button')
    driver.find_element_by_css_selector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(1) > div > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div.CXO_fulfillment_continue > button').click()
##delivery
    waitSelector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div.address-grid > div.Common-AddressTile.address-col.nth-3np1.nth-2np1.address-col-alpha.address-col-beta.address-col-gamma > div > div > div.address-tile-clickable > div.checkbox-container > label > input')
    driver.find_element_by_css_selector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div.address-grid > div.Common-AddressTile.address-col.nth-3np1.nth-2np1.address-col-alpha.address-col-beta.address-col-gamma > div > div > div.address-tile-clickable > div.checkbox-container > label > input').click()
    ##waitXpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div[1]/label/input')
    ##driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div[1]/label/input').click()

##contiue button for delivery
    waitSelector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div.arrange > div.arrange-fill.u-size-1-12-m > button')
    driver.find_element_by_css_selector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(2) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div > div > div > div > div.arrange > div.arrange-fill.u-size-1-12-m > button').click()
    ##waitXpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/button')
    ##driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/button').click()
##security code
    waitSelector('#cvv-confirm')
    driver.find_element_by_css_selector('#cvv-confirm').send_keys('483')
##review your order button
    waitSelector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(3) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div:nth-child(2) > div > button')
    driver.find_element_by_css_selector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div:nth-child(3) > div.CXO_module_container > div.CXO_module_body.ResponsiveContainer > div > div > div > div.text-left.Grid > div:nth-child(2) > div > button').click()
##place your order button
    waitSelector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div > div.Grid-col.u-size-1.u-size-3-12-s.u-size-3-12-m > div > form > div > button')
    driver.find_element_by_css_selector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div > div.Grid-col.u-size-1.u-size-3-12-s.u-size-3-12-m > div > form > div > button').click()
    time.sleep(120)
    ##waitXpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button')    
    ##driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button').click()
    

