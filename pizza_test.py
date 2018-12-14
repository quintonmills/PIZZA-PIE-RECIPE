from fourthpack.pages.home.pizza_page import PizzaPage
import unittest
import pytest
@pytest.mark.usefixtures("OneTimeSetUp", "SetUp")
class orderPizzaTest(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    @pytest.fixture(autouse=True)
    def objectSetup (self, OneTimeSetUp):
        self.pizza = PizzaPage(self.driver)
    @pytest.mark.run(order=1)
    def test_pizzaRecipe(self):
        self.pizza.OrderThePizza()
