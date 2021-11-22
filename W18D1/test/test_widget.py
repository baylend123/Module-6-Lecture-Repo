'''
The unittest package
    To run tests with unittest:

        python -m unittest
    All tests must be in a folder called test at the top level of the project. 
    The test folder must contain a __init__.py
'''

'''
Writing unittest tests
    Inside a test file:
        import unittest.
        import the code that we are testing.
        create a class that inherits from unittest.TestCase.
'''

# import unittest
# from widget import Widget

# class TestWidget(unittest.TestCase):
#      def test_initialize_widget_with_color(self):
#         # arrange
#         color = "blue"
#         test_widget = Widget(color)
#         # act
#         result = test_widget.color
#         # assert
#         self.assertEqual(result, color)


'''
The pytest package
Create a virtual environment if you haven’t yet, and install pytest.

pipenv install pytest --python 3.9.4
Run tests at the command line by running

pytest
Make a directory called test at the top level of your project (be sure it contains a __init__.py).

Test files must be in test directory, and filenames must begin or end with test.
'''

'''
Writing pytest tests
Define test functions directly—no need for classes. Function names must begin 
with test to be treated as a unit test.

Use assert keyword, followed by the conditional you are trying to test.

You can run unittest tests with pytest, but not vice versa.
'''

from widget import Widget


def test_initialize_widget_with_color():
    # arrange
    color = "blue"
    test_widget = Widget(color)
    # act
    result = test_widget.color
    # assert
    assert result == color