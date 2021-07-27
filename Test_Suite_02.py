import unittest

class PythonOrgSearch1(unittest.TestCase):
    @classmethod 
    def setUp(self):
        print("@classmethod  setup from PythonOrgSearch1")

    def test_03_search_in_python_org(self):
        print("Test Case : test_03_search_in_python_org")
    
    def test_04_search_by_name(self):
        print("Test Case : test_04_search_in_python_org")

    @classmethod 
    def tear_down(self):
        print("@classmethod  teardown from PythonOrgSearch1")


if __name__ == "__main__":
    unittest.main()