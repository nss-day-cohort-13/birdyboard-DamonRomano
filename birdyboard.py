from create_new_user import *
from chirp import *

active_user = None

def main_menu():

    global active_user

    print   ("""
            \n\n
            WELCOME TO BIRDYBOARD, A FLAGRANT COPYRIGHT VIOLATION!

            Your real life is teh suxx0r;
            waste yourself away on social media instead!

            Main Menu:
            1. Create New User Account
            2. Select User
            3. Make New Chirp
            4. View All Chirps
            5. Exit Birdyboard

            """)

    selection = input("Please Make A Selection:")
    if selection == '1':
        print   ("""
                Create A New User Account Because \n
                You Think We Won't Know It's Still You. \n
                Creeper. \n
                Please Enter the New User's Full Name\n
                \n
                """)

        user_full_name = input(">")

        print   ("""
                Please Enter the New User's Screen Name
                \n\n
                """)

        user_screen_name = input(">")

        active_user = New_User(user_full_name, user_screen_name)

        main_menu()


    elif selection == '2':
        print   ("""
                \n\n
                Who would you like to pretend you are today?
                \n\n
                """)

        # print list of user names from users.p
        with open('users.p', 'rb') as u:
            user_list = []
            while True:

                try:
                    user_list.append(pickle.load(u))

                except EOFError:
                    break

        for number, user in enumerate(user_list, start=1):
            print   (str(number)
                    + ". "
                    + user.screen_name
                    )

        # then pick one from list
        choice_of_user = input (">")
        active_user = user_list[int(choice_of_user) - 1]
        print   ("""
                \n\n
                Welcome {}! You have no friends IRL!
                \n\n
                """.format(active_user.screen_name)
                )

        main_menu()


    elif selection == '3':
        print   ("""
            You are logged in as {}.

            Write a new chirp:
            """.format(active_user.screen_name)
            )

        chirp = input(">")


        new_chirp = Chirp(active_user.user_UUID, chirp)

        chirp_list()
        input (">")
        main_menu()


    elif selection == '4':
        print   ("""
                View All Chirps
                """)
        chirp_list()
        input (">")
        main_menu()

    elif selection == '5':
        print ("Yes!  Love yourself more than this.  Go outside; play in the rain. ")
        exit()

    else:
        print ("You want the impossible.")


def chirp_list():

    global active_user

    try:
        chirp_list = []
        with open('chirps.p', 'rb') as c:
            while True:

                try:
                    chirp_list.append(pickle.load(c))

                except EOFError:
                    break

                except FileNotFoundError:
                    chirp_list = []
                    print("FNF chirp_list")

        user_list = []
        with open('users.p', 'rb') as u:
            while True:

                try:
                    user_list.append(pickle.load(u))

                except EOFError:
                    break

        for number, chirp in enumerate(chirp_list, start=1):
            user = None
            for u in user_list:
                if u.user_UUID == chirp.user_UUID:
                    user = u
                    break

            print   (
            str(number)
            + ". "
            + user.screen_name
            + ":  "
            + chirp.text
            )
    except FileNotFoundError:
        print("No File, Fucker!")


main_menu()
