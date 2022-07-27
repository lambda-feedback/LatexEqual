import unittest

from evaluation_function_utils.client import MissingCredentials

try:
    from .evaluation import evaluation_function
except ImportError:
    from evaluation import evaluation_function
except MissingCredentials:
    pass


class TestEvaluationFunction(unittest.TestCase):
    """
        TestCase Class used to test the algorithm.
        ---
        Tests are used here to check that the algorithm written 
        is working as it should. 
        
        It's best practise to write these tests first to get a 
        kind of 'specification' for how your algorithm should 
        work, and you should run these tests before committing 
        your code to AWS.

        Read the docs on how to use unittest here:
        https://docs.python.org/3/library/unittest.html

        Use evaluation_function() to check your algorithm works 
        as it should.
    """

    # No tests in here, since the test environment doens't have access
    # to the credentials required to call the external symbolicEqual function
    def test_blank(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()