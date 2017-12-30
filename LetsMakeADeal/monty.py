#Created By: Samyam C. Shrestha
#Lab Section: CS-171-061

import sys
import random

#random.seed(10)

#Function that sets up doors
def setupDoors():

    #Create the list
    random_list = ["G","G","C"]
    #print('Current List_Setup:',random_list )

    random.shuffle(random_list)

    #print('Random doors: ',random_list)
    return random_list


#Function that determines the door for Player's choice
def playerDoor():
    selected_door = random.randint(1,3)
    #print('playerDoor: ',selected_door)
    return selected_door


#Function that selects the door for Monty's choice.
# And takes list of the doors and player's choice index for that list of the doors as arguments
def montyDoor(Doors, Player):

    #print('Player Selection Index: ', Player)
    # for door in Doors:
    #     print("Loop: ",door )
    #     print('Door Index: ',Doors.index(door))
    #     if (Doors.index(door) != Player) or (door != "C"):
    #
    #
    #         print('Monty:',door)
    #         print("index:",Doors.index(door) + 1  )
    #         return Doors.index(door)+1
    # #remove the door selected by the player
    # Doors.pop(Player)
    # print(Doors)
    # if 'C' in Doors:
    #     Doors.remove('C')
    #     print(Doors)
    # return Doors
    if Doors[Player] == 'C':
        #print('Monty\'s Index: ',Doors.index('G'))
        return Doors.index('G')
    index_of_C = Doors.index('C')
    for index in range(0,3):
        if index != Player and index != index_of_C:
            #print('Monty\'s Index: ', index)
            return index


#Function that plays one game of Let's Make a Deal.
def playRound():

    #Get the setup for doors
    list_of_doors = setupDoors()

    #Get the player choice for the door
    player_choice_door = playerDoor() - 1

    #print(list_of_doors, player_choice_door)
    #Get the door that Monty selects
    monty_door = montyDoor(list_of_doors, player_choice_door)

    if list_of_doors[player_choice_door] == 'C':
        #print('Return 0')
        return 0
    else:
        #print('Return 1')

        return 1


print("Welcome to Monty Hall Analysis")
print("Enter ’exit' to quit.")
while(True):
    user_input = input("How many tests should we run?").strip()
    if user_input.lower() == 'exit':
        print("The program will exit now. Thank You.")
        sys.exit(0)

    counter_for_stay = 0
    counter_for_switch = 0
    try:
        user_input = int(user_input)
        counter = 1

        while counter <= user_input:
            result = playRound()



            # Check for stay won and switch won and then add them to the respective counter variables
            if result == 0:
                counter_for_stay += 1

            elif result == 1:
                counter_for_switch += 1

            counter += 1




        # list_of_doors = setupDoors()
        # player_selected_door = playerDoor() - 1
        # print(list_of_doors, player_selected_door)
        # montyDoor(list_of_doors, player_selected_door)


    except:
        print("Bad Input Test.")
        print("Please enter a number.")
        continue

    #Calculate and display the Stay won and Switch Won percentages
    stay_percentage = (counter_for_stay / user_input) * 100
    switch_percentage = (counter_for_switch / user_input) * 100
    print("Results:")
    print("Stay Won %.1f%% of the time." % stay_percentage)
    print("Switch Won %.1f%% of the time." % switch_percentage)






