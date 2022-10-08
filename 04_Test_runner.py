import unittest
from Test_Suite_01 import LoadTest
from Test_Suite_02 import SanityTest
from Test_Suite_02 import SanityTest

 
# get all tests from SearchText and HomePageTest class
sanityTest = unittest.TestLoader().loadTestsFromTestCase(SanityTest)
loadTest = unittest.TestLoader().loadTestsFromTestCase(LoadTest)
print (sanityTest)
print(type(sanityTest))
print (loadTest)
print(type(loadTest))
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([sanityTest, loadTest])
# #
# # # run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)