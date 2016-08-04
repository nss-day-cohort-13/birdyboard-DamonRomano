# test, then logic, then menu, then files.


import pickle
# from magic import spells

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
        '3. View All Chirps' '\n'
        '4. Make New Public Chirp' '\n'
        '5. Make New Private Chirp' '\n'
        '6. Exit Birdyboard' '\n'
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
    # store in memory, then

    print   (
            "Please Enter the New User's Screen Name"
            "\n" "\n"
            )

    user_screen_name = input(">")

elif selection == '2':
    print ("Who would you like to pretend you are today?")
    # print list of user names from user_data.txt
    input (">")

elif selection == '3':
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

elif selection == '6':
    print ("Yes!  Go outside; play in the rain. Love yourself more than this.")
    # exit python console

else:
    print ("You want the impossible.")
