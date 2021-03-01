import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://demo-m2.bird.eu/')

    def test_logo(self):
        logo = self.driver. \
            find_element_by_xpath("//img[@alt='Magento Commerce']")
        #     check logo is displayed on homepage
        self.assertTrue(logo.is_displayed())
        #   click on logo to open the page
        logo.click()
        # check page title
        self.assertEqual("Home Page", self.driver.title)

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.ID, "search_mini_form"))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID, "switcher-language"))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = \
            self.driver.find_element_by_css_selector(".minicart-wrapper")
        shopping_cart_icon.click()
        # get the shopping cart status
        shopping_cart_status = \
            self.driver.find_element_by_css_selector(".minicart-wrapper .action.showcart").text
        self.assertTrue("You have no items in your shopping cart.", shopping_cart_status)
        # close the shopping cart section
        close_button = self.driver. \
            find_element_by_class_name("action-close")

    def test_my_account_link_is_displayed(self):
        # get the account link
        account_link = self.driver.find_element_by_link_text("Create an Account")
        # Check 'Create an account' is displayed in the Home Page footer
        self.assertTrue(account_link.is_displayed())


    def test_register_new_user(self):
        driver = self.driver

        # Click on Sign In to open Sign in page
        driver.find_element_by_link_text("Sign In").click()

        # get the Create an Account link
        create_account_link = driver.find_element_by_link_text("Create an Account")
        # check Create an Account link is displayed and enabled
        self.assertTrue(create_account_link.is_displayed() and
                        create_account_link.is_enabled())

        create_account_link.click()

        self.assertEqual("Create New Customer Account", driver.title)

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        news_letter_subscription = driver.find_element_by_id("is_subscribed")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id(("password-confirmation"))
        create_an_account_button = driver.find_element_by_xpath("//button[@type='submit']")

        self.assertTrue(first_name.is_displayed() and last_name.is_displayed())
        # self.assertEqual('255', first_name.get_attribute('maxlength'))
        # self.assertEqual('255', last_name.get_attribute('maxlength'))
        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and
                        email_address.is_enabled() and
                        news_letter_subscription.is_enabled() and
                        password.is_enabled() and
                        confirm_password.is_enabled() and
                        create_an_account_button.is_enabled())

        # check Sign Up for Newsletter is unchecked
        self.assertFalse(news_letter_subscription.is_selected())

        # fill out all the fields
        first_name.send_keys("Tester9")
        last_name.send_keys(("User9"))
        news_letter_subscription.click()
        email_address.send_keys("TestUser9@example.com")
        password.send_keys("Bello14@$")
        confirm_password.send_keys("Bello14@$")

    def is_element_present(self, how, what):
        '''

        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        '''
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False


        return True

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
