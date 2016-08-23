from create_new_user import *

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
            print (str(number) + ". " + user.screen_name)


        # then pick one from list
        choice_of_user = input (">")
        active_user = user_list[int(choice_of_user) - 1]
        print ("Welcome " + active_user.screen_name + "! You have no friends IRL!")

        main_menu()




    elif selection == '3':
        print ("You are logged in as " + active_user.screen_name)

        print   (
                "\n"
                "View All Chirps" "\n" "\n"
                "1. View all private Chirps." "\n"
                "2. View all public Chirps."
                )
        input (">")

    #     if selection == '1':
    #         # goto list of users with whom this user has private Chirps
    #     elif selection == '2':
    #         # goto chronological list of all public chirps.
    #         #   Hmm...chronological by first Chirp or by most recent reply?)
    #     else print ("You don't know what you want.")

    # elif selection == '4':
    #     print ("You Can Make A New Public Chirp!")
    #     print ("No, go ahead;  We're all so interested in what you have to say.")
    #     print ("")
    #     input (">")

    elif selection == '5':
        print ("You Can Make A New Private Chirp!")
        print ("From which user do you desperately crave attention," \
                " you very lonely person?")
        print ("")
        # print (numbered userlist)
        print ("")
        input (">")

    elif selection == '5':
        print ("Yes!  Go outside; play in the rain. Love yourself more than this.")
        # exit python console

    else:
        print ("You want the impossible.")

main_menu()
