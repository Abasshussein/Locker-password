import unittest
from credential import Credential
class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the credential class behaviours,
    the arguments help in creating test cases.

    """

    def setUp(self):

        """
        this method runs before each test case, carries the instrctions of what is to be done

        """

        self.new_password = Credential("rooney")

    def test_init(self):

        """
        used to test if the objects have been initialized properly

        """

        self.assertEqual(self.new_password.credential_detail,"rooney")



if __name__ == '__main__':
    unittest.main()
