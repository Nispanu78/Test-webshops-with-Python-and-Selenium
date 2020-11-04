import unittest
from test_home_page_shop_1 import HomePageTest
from test_home_page_shop_2 import TestHomePage
from test_register_new_user_shop_2 import RegisterNewUser
from test_browser_navigation import NavigationTest
from test_compare_products_shop_2 import CompareProducts
from test_explicit_wait_shop_2 import (ExplicitWaitTests)
from test_explicit_waits_on_alerts_shop_2 import CompareProductsAlerts

# get all tests from SearchTest and HomePageTest class
test_home_page_shop_1 = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
test_home_page_shop_2 = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
test_register_new_user_shop_2 = unittest.TestLoader().loadTestsFromTestCase(RegisterNewUser)
test_browser_navigation = unittest.TestLoader().loadTestsFromTestCase(NavigationTest)
test_compare_products = unittest.TestLoader().loadTestsFromTestCase(CompareProducts)
test_explicit_waits = unittest.TestLoader().loadTestsFromTestCase(ExplicitWaitTests)
test_explicit_waits_alerts = unittest.TestLoader().loadTestsFromTestCase(CompareProductsAlerts)


# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([test_home_page_shop_1 , test_home_page_shop_2, test_register_new_user_shop_2,
                                  test_browser_navigation, test_compare_products,
                                  test_explicit_waits, test_explicit_waits_alerts])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
