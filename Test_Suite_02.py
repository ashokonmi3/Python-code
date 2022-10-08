import unittest

class SanityTest(unittest.TestCase):
    @classmethod 
    def setUp(self):
        print("@classmethod  setup from SanityTest")

    def test_03_search_in_sanity_test(self):
        print("SanityTest Case : test_03_search_in_python_org")
    
    def test_04_search_by_name(self):
        print("SanityTest Case : test_04_search_in_python_org")

    @classmethod 
    def tear_down(self):
        print("@classmethod  teardown from SanityTest")


if __name__ == "__main__":
    unittest.main()