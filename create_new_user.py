import pickle

class New_User:

    def __init__(self,
                 user_full_name,
                 user_screen_name
                 ):

        self.user_UUID = None
        self.name = user_full_name
        self.screen_name = user_screen_name

    # serialize some shit - this will serialize each user as he is created, rather than serializing the whole list of users and appending to that list with each user created.

        with open('users.p', 'ab+') as u:
            pickle.dump(self, u)
