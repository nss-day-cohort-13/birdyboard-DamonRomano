import sys
import pickle
import birdyboard

    class Chirp:

    def read_chirps(chirps):

        try:
            with open('chirps.p', 'rb') as c:
                deserialized_chirps = pickle.load(c)

        except (FileNotFoundError, EOFError):
            deserialized_chirps = {}


        if "User" not in deserialized_chirps:
            deserialized_chirps["User"] = []
        deserialized_chirps["User"].append(chirps)

        with open('chirps.p', 'wb+') as m:
            pickle.dump(deserialized_chirps, m)
            print(deserialized_chirps)

if __name__ == "__main__":
  User.read_chirps(sys.argv[1])
