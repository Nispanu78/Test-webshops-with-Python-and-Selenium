import unittest
from test_home_page_shop_1 import HomePageTest
from test_home_page_shop_2 import TestHomePage
from test_register_new_user_shop_2 import RegisterNewUser

# get all tests from SearchTest and HomePageTest class
test_home_page_shop_1 = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
test_home_page_shop_2 = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
test_register_new_user_shop_2 = unittest.TestLoader().loadTestsFromTestCase(RegisterNewUser)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([test_home_page_shop_1 , test_home_page_shop_2, test_register_new_user_shop_2])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
