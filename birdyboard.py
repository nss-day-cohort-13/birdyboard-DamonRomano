# import stuff from places
# from magic import spells

menu = {}
menu['1']="Create New User Account"
menu['2']="Select User"
menu['3']="View All Chirps"
menu['4']="Make New Public Chirp"
menu['6']="Make New Private Chirp"
menu['5']="Exit Birdyboard"


options = menu.keys()
for entry in options:
    print(entry, menu[entry])

    selection = input("Please Select:")
    if selection == '1':
      print ("Create New User Account")
    elif selection == '2':
      print ("Select User")
    elif selection == '3':
      print ("View All Chirps")
    elif selection == '4':
      print ("Make New Public Chirp")
    elif selection == '5':
      print ("Make New Private Chirp")
    elif selection == '6':
      print ("Exit Birdyboard")
    break
    else:
      print ("The thing you want doesn't exist.  You want the impossible.")




