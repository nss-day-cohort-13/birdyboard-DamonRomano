from create_new_user import *
from chirp import *

active_user = None

def main_menu():

    global active_user

    print   (
            '\n'
            'WELCOME TO BIRDYBOARD, A FLAGRANT COPYRIGHT VIOLATION!'
            '\n' '\n'
            'Your real life is teh suxx0r;' '\n'
            'waste yourself away on social media instead!'
            '\n' '\n'
            'Main Menu:'
            '\n' '\n'
            '1. Create New User Account' '\n'
            '2. Select User' '\n'
            '3. Make New Chirp' '\n'
            '4. View All Chirps' '\n'
            '5. Exit Birdyboard' '\n'
            '\n'
            )

    selection = input("Please Make A Selection:")
    if selection == '1':
        print   (
                "Create A New User Account Because " \
                "You Think We Won't Know It's Still You." "\n"
                "Creeper." '\n'
                "Please Enter the New User's Full Name"
                "\n" "\n"
                )

        user_full_name = input(">")

        print   (
                "Please Enter the New User's Screen Name"
                "\n" "\n"
                )

        user_screen_name = input(">")

        active_user = New_User(user_full_name, user_screen_name)

        main_menu()


    elif selection == '2':
        print ("Who would you like to pretend you are today?")

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
        print ("Welcome " + active_user.screen_name + "! You have no friends IRL!")

        main_menu()


    elif selection == '3':
        print   (
                "\n" "\n"
                "You are logged in as "
                + active_user.screen_name
                "\n" "\n"
                "Write A New Chirp"
                "\n" "\n"
                )

                
    elif selection == '4':
        print   (
                "\n"
                "View All Chirps"
                "\n"
                )
        with open('chirps.p', 'rb') as c:
            chirp_list = []
            while True:

                try:
                    chirp_list.append(pickle.load(c))

                except EOFError:
                    break

        for number, chirp in enumerate(chirp_list, start=1):
            print   (
                    str(number)
                    + ". "
                    + user.screen_name
                    + chirp.text
                    )


    elif selection == '5':
        print ("Yes!  Love yourself more than this.  Go outside; play in the rain. ")
        # exit python console

    else:
        print ("You want the impossible.")

main_menu()
