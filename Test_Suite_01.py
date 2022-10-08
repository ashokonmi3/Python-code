import unittest

class LoadTest(unittest.TestCase):
    
    def setUp(self):
        print("setup from Load test")

    
    def test_01_search_in_python_org(self):
        print("Load Test Case : test_01_search_in_python_org")

    
    def test_02_search_by_name(self):
        print("Load Test Case : test_02_search_by_name")

     
    def tear_down(self):
        print("TEAR DOWN from Load test case")



if __name__ == "__main__":
    unittest.main()