from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login():

    def test(self):
        baseUrl = "https://www.papajohns.com"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        menu = driver.find_element_by_xpath("//a[contains(text(),'Menu')]")
        menu.click()
        driver.implicitly_wait(3)
        pizza = driver.find_element_by_xpath("//main[@class='main']//section[1]//div[2]//ul[1]")
        pizza.click()
        address = driver.find_element_by_xpath("//input[@id='locations-streetaddress']")
        address.send_keys("1600 Pennsylvania Ave NW, Washington, DC")
        zipcode = driver.find_element_by_xpath("//input[@id='locations-usa-zipcode']")
        zipcode.send_keys("20500")
        submit = driver.find_element_by_xpath("//div[@class='button-set']//input[@value='Submit']")
        
        submit.click()
        reorder = driver.find_element_by_xpath("//a[@id='order-button-0-1']")
        reorder.click()
        addtocart = driver.find_element_by_xpath("//div[@id='product-details-0-1']//button[@type='submit'][contains(text(),'Add to cart')]")
        addtocart.click()
        gotocheckout = driver.find_element_by_xpath("//a[contains(@href,'/order/view-cart')]")
        gotocheckout.click()
        checkOut = driver.find_element_by_xpath("//button[contains(text(),'Check Out →')]")
        checkOut.click()
        nothankyou = driver.find_element_by_xpath("//button[@class='button-small button']")
        nothankyou.click()
        firstname = driver.find_element_by_xpath("//input[@id='contact-firstname']")
        firstname.send_keys("Donald")
        lastname = driver.find_element_by_xpath("//input[@id='contact-lastname']")
        firstname.send_keys("Trump")
        driver.implicitly_wait(5)
ff= login()
ff.test()