import fourthpack.utilities.custom_logger as cl
import loggingfrom fourthpack.base.basepage import basepage
import time
class PizzaPage(BasePage):
####################Locators#################
    menu_selection = "//a[contains(text(),'Menu')]"
    pizza_selection = "//main[@class='main']//section[1]//div[2]//ul[1]"
    address_text_field = "//input[@id='locations-streetaddress']"
    zipcode_text_field = "//input[@id='locations-usa-zipcode']"
    submit_button = "//div[@class='button-set']//input[@value='Submit']"
    secondMenue_selection = "//a[@id='order-button-0-1']"
    addToCart_button = "//div[@id='product-details-0-1']//button[@type='submit'][contains(text(),'Add to cart')]"
    goToCheckout_button = "//a[contains(@href,'/order/view-cart')]"
    commit_button = "//button[contains(text(),'Check Out →')]"
    secondCommit_button = "//button[@class='button-small button']"
    firstName_field = "//input[@id='contact-firstname']"
    secondName_field = "//input[@id='contact-lastname']"
    ########################information#####################
    address = "1600 Pennsylvania Ave NW, Washington, DC"
    zipcode = "20500"
    firstname = "Donald"
    lastname = "Trump"
#-----------------------------------------------------------
    log = cl.customLogger(logging.DEBUG)
#-----------------------------------------------------------
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def AddPizzaToCart(self):
        self.elementClick(locator=self.menu_selection, locatorType="xpath")
        self.elementClick(locator=self.pizza_selection, locatorType="xpath")
        self.sendKeys(address, locator=self.address_text_field, locatorType="xpath")
        self.sendKeys(zipcode, locator=self.zipcode_text_field, locatorType="xpath")
        self.elementClick(locator=self.submit_button, locatorType="xpath")
        self.elementClick(locator=self.secondMenue_selection, locatorType="xpath")
        self.elementClick(locator=self.commit_button, locatorType="xpath")
        self.elementClick(locator=self.secondCommit_button, locatorType="xpath")
    def AddCredentials(self):
        self.sendKeys(firstname, locator=self.firstName_field, locatorType="xpath")
        self.sendKeys(lastname, locator=self.secondName_field, locatorType="xpath")
    def OrderThePizza(self):
        self.AddPizzaToCart()
        self.addCredentials()

        

