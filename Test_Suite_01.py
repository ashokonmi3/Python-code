import unittest

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        print("setup from PythonOrgsearch")

    
    def test_01_search_in_python_org(self):
        print("Test Case : test_01_search_in_python_org")

    
    def test_02_search_by_name(self):
        print("Test Case : test_02_search_by_name")

     
    def tear_down(self):
        print("TEAR DOWN from PythonOrgsearch")



if __name__ == "__main__":
    unittest.main()