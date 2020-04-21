import unittest
from user import User
class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours,
    the arguments help in creating test cases.

    """

    def setUp(self):

        """
        this method runs before each test case, carries the instrctions of what is to be done

        """

        def  tearDown(self):

            """
            tearDown method does clean up after each test case has runself.
            """

        self.new_user = User("facebook","rooney","123jm","123jm")

    def  test_init(self):

        """
        used to test if the objects have been initialized properly

        """

        self.assertEqual(self.new_user.account_name,"facebook")
        self.assertEqual(self.new_user.username,"rooney")
        self.assertEqual(self.new_user.password,"123jm")
        self.assertEqual(self.new_user.confirm_password,"123jm")

    def  test_save_detail(self):

        """
        the test_save_detail test is used to test if the contact object is saved into details

        """

        self.new_user.save_detail()

        self.assertEqual(len(User.user_detail),1)

    def  test_save_multiple_detail(self):

        """
        a method to check if we can save multiple user details to our details array
        """

        self.new_user.save_detail()
        test_user = User("Test","user","123jm","123jm")
        test_user.save_detail()
        self.assertEqual(len(User.user_detail),3)

    # def test_delete_detail(self):
    #
    #     self.new_user.save_detail()
    #     test_user = User("Test","user")
    #     test_user.save_detail()
    #
    #     self.new_user.delete_detail()
    #     self.assertEqual(len(User.user_detail))

    def test_display_all_details(self):

        """
        is a method that returns a list of all details saved
        """

        self.assertEqual(User.display_all_details(),User.user_detail)




if __name__ == '__main__':
    unittest.main()
