import unittest
import sys
# Method                 Checks that
# assertEqual(a, b)      a == b
# assertNotEqual(a, b)   a != b
# assertTrue(x)          bool(x) is True
# assertFalse(x)         bool(x) is False
# assertIs(a, b)         a is b
# assertIsNot(a, b)      a is not b
# assertIsNone(x)        x is None
# assertIsNotNone(x)     x is not None
# assertIn(a, b)         a in b
# assertNotIn(a, b)      a not in b
# assertIsInstance(a, b) isinstance(a, b)
# assertNotIsInstance(a, b) not isinstance(a, b)
# ========================================
# class SimpleTest(unittest.TestCase):
#    def test1(self):
#       self.assertEqual(4 + 5,9)
#    def test2(self):
#       self.assertNotEqual(5 * 2,10)
#    def test3(self):
#       self.assertTrue(4 + 5 == 9,"The result is False")
#    def test4(self):
#       self.assertTrue(4 + 5 == 10,"assertion fails")
#    def test5(self):
#       self.assertIn(3,[1,2,3])
#    def test6(self):
#       self.assertNotIn(3, range(5))
#    def test7(self):
#       self.assertEqual('10',10)
#    def test8(self):
#       self.assertEqual(10, 10)
#
# if __name__ == '__main__':
#    unittest.main()
# =========================
import math
import re

# class SimpleTest(unittest.TestCase):
#    def test1(self):
#       self.assertAlmostEqual(22.0/7,3.14)
#    def test2(self):
#       self.assertNotAlmostEqual(10.0/3,3)
#    def test3(self):
#       self.assertGreater(math.pi,3)
#    def test4(self):
#       self.assertNotRegex("Tutorials Point (I) Private Limited","Point")
# #
# if __name__ == '__main__':   unittest.main()

# ======================
# class SimpleTest(unittest.TestCase):
#    def test1(self):
#       self.assertListEqual([2,3,4], [1,2,3,4,5])
#    def test2(self):
#       self.assertTupleEqual((1*2,2*2,3*2), (2,4,6))
#    def test3(self):
#       self.assertDictEqual({1:11,2:22},{3:33,2:22,1:11})
#
# if __name__ == '__main__':
#    unittest.main()
   # =================
# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()

# Command line
# python -m unittest 03_Demo_unittest.py
# python -m unittest -v  03_Demo_unittest.py
# -v Verbose
# When executed without arguments Test Discovery is started:
# python -m unittest
# =======================
# class Widget():
#     def __init__(self,name):
#         self.name= name
#         self.dim=(50,50)
#     def size(self):
#         return self.dim
#     def resize(self,d1,d2):
#         self.dim=(d1,d2)
# #
# class DefaultWidgetSizeTestCase(unittest.TestCase):
#     def test_default_widget_size(self):
#         widget = Widget('The widget')
#         self.assertEqual(widget.size(), (50, 50))
# #
# if __name__ == '__main__':
#     unittest.main()
# python -m unittest -v 03_Demo_unittest.py

# ============================
# Setup and tear down method
# class Widget():
#     def __init__(self,name):
#         self.name= name
#         self.dim=(50,50)
#     def size(self):
#         return self.dim
#     def resize(self,d1,d2):
#         self.dim=(d1,d2)

# class WidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         print("setUP: Test setup")
#         self.widget = Widget('The widget')
#
#     def tearDown(self):
#         print("Teardown:Test completed")
#
#     def test_default_widget_size(self):
#         print("Test case : test_default_widget_size")
#         self.assertEqual(self.widget.size(), (50,50),
#                          'incorrect default size')
#
#     def test_widget_resize(self):
#         print("Test Case: test_widget_resize")
#         self.widget.resize(100,150)
#         self.assertEqual(self.widget.size(), (100,150),
#                          'wrong size after resize')
#
# if __name__ == '__main__':
#     unittest.main()
# python -m unittest -v 03_Demo_unittest.py

# =====================
# class Widget():
#     def __init__(self,name):
#         self.name= name
#         self.dim=(50,50)
#     def size(self):
#         return self.dim
#     def resize(self,d1,d2):
#         self.dim=(d1,d2)
#
# class WidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         self.widget = Widget('The widget')
#
#     def test_default_widget_size(self):
#         self.assertEqual(self.widget.size(), (50,50),
#                          'incorrect default size')
#
#     def test_widget_resize(self):
#         self.widget.resize(100,150)
#         self.assertEqual(self.widget.size(), (100,150),
#                          'wrong size after resize')
#
#     def test_widget_name(self):
#         self.assertEqual(self.widget.name, "The widget",
#                          'wrong size after resize')
#
#     def tearDown(self):
#         print("Teardown:Test completed")
# #
# #
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(WidgetTestCase('test_default_widget_size'))
#     suite.addTest(WidgetTestCase('test_widget_resize'))
#     return suite
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())
# python -m unittest -v 03_Demo_unittest.py

# =========================
# Skipping the test cases
# def external_resource_available():
#     return False
#
# class MyTestCase(unittest.TestCase):
#     @unittest.skip("demonstrating skipping")
#     def test_nothing(self):
#         self.fail("shouldn't happen")
#
#     @unittest.skipIf(sys.version_info.major < 2 ,
#                      "not supported in this library version")
#     def test_format(self):
#         # Tests that work for only a certain version of the library.
#         pass
#
#     @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
#     def test_windows_support(self):
#         print("windows specific testing code")
# #
# #
#     def test_maybe_skipped(self):
#         if not external_resource_available():
#             self.skipTest("external resource not available")
#         # test code that depends on the external resource
#         else:
#            self.assertEqual(1, 0, "broken")
#
# if __name__ == '__main__':
#     unittest.main()
# # python -m  unittest -v unittest_example.py
# ================================
# Classes can be skipped just like methods:
# # #
# @unittest.skip("showing class skipping")
# class MySkippedTestCase(unittest.TestCase):
#     def test_not_run(self):
#         pass
# if __name__ == '__main__':
#     unittest.main()
# ====================
# Expected failures use the expectedFailure() decorator.
#
# class ExpectedFailureTestCase(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_fail(self):
#         self.assertEqual(2, 1, "broken")
# if __name__ == '__main__':
#     unittest.main()

#===========================
# #
# class ExpectedFailureTestCase(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_fail(self):
#         self.assertEqual(1, 1, "broken") #u
# if __name__ == '__main__':
#     unittest.main()
# ================
# class ExpectedFailureTestCase(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_fail(self):
#         self.assertEqual(2, 1, "broken") # x
# if __name__ == '__main__':
#     unittest.main()

# ========================
# unittest allows you to distinguish them inside the body of a test method using
# the subTest() context manager.

# class NumbersTest(unittest.TestCase):
#
#     def test_even(self):
#         """
#         Test that numbers between 0 and 5 are all even.
#         """
#         for i in range(0, 6):
#             # with self.subTest(i=i):
#             print(i)
#             self.assertEqual(i % 2, 0)
# if __name__ == '__main__':
#     unittest.main()
# =================
#
# class NumbersTest(unittest.TestCase):
#
#     def test_even(self):
#         """
#         Test that numbers between 0 and 5 are all even.
#         """
#         for i in range(0, 6):
#             with self.subTest(i=i):
#                 print(i)
#                 self.assertEqual(i % 2, 0)
# # #
# # # # Without using a subtest, execution would stop after the first failure,
# # # and the error would be less easy to diagnose because the value of i wouldn’t be displayed:
# if __name__ == '__main__':
#     unittest.main()

# ======================
# class Example(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("setUpClass")
#
#     def setUp(self):
#         print("setUp")
#
#     def test1(self):
#         print("test1")
#
#     def test2(self):
#         print("test2")
#
#     def tearDown(self):
#         print("tearDown")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("tearDownClass")
#
# if __name__ == '__main__':
#     unittest.main()
# ======================

# =================
# Exception test
import unittest

def div(a,b):
   return a/b
class raiseTest(unittest.TestCase):
   def testraise(self):
      self.assertRaises(ZeroDivisionError, div, 1,0)

if __name__ == '__main__':
   unittest.main()

