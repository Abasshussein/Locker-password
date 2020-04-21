class User:
    """

    Class that will generate new instances of users

    """

    user_detail = []

    def save_detail(self):

        """
        the method saves detail objects into the empty user_detail array
        """
        User.user_detail.append(self)


    def __init__(self,account_name,username,password,confirm_password):

        """
        the __init__method helps us define properties for our objectsself.

        """

        self.account_name = account_name
        self.username = username
        self.password =password
        self.confirm_password = confirm_password


        """
        arguments for our __init__method will include the following.

        """

    @classmethod
    def display_all_details(cls):

        return cls.user_detail

    @classmethod
    def find_by_username(cls,username):

        for user in cls.user_detail:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,username):

        for user in cls.user_detail:
            if user.username == username:
                    return True
