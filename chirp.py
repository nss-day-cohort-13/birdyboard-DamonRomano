import pickle
import uuid

class Chirp:

    def __init__(self,
                 user_UUID,
                 text
                 ):

        self.chirp_UUID = uuid.uuid4().int
        self.user_UUID = active_user.screen_name
        self.text = text

    # serialize some shit - this will serialize each user as he is created, rather than serializing the whole list of users and appending to that list with each user created.

        with open('chirps.p', 'ab+') as c:
            pickle.dump(self, c)
