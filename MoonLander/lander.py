#Created By: Samyam C. Shrestha
#Lab Section: CS-171-061


#Import Statements
import sys


#Defining and initializing variables
units_of_fuel = 0  #Units of Fuel
altitude = 50.0    #Altitude (m)
velocity = 0.0     #Initial Velocity (m/s)
number_of_seconds_passed = 0  #Number of seconds passed
THRUSTER_ACCELERATION = 0.1   #Thruster Acceleration (m/s^2)
level = 0          #level of the game
level_names = ['Moon', 'Earth','Pluto','Neptune','Uranus','Saturn','Jupiter','Mars','Venus','Mercury','Sun']  #Name of the levels

#Dictionary containing the details about the different levels
level_details  = {
    'Moon' : {
        'GRAVITY' : -1.622,
        'UNITS_OF_FUEL' : 150
    },
    'Earth' :{
        'GRAVITY' : -9.81,
        'UNITS_OF_FUEL' : 5000
    },
    'Pluto' : {
        'GRAVITY' : -0.42,
        'UNITS_OF_FUEL' : 200
    },
    'Neptune' : {
        'GRAVITY' : -14.07,
        'UNITS_OF_FUEL' : 250
    },
    'Uranus' : {
        'GRAVITY' : -10.67,
        'UNITS_OF_FUEL' : 270
    },
    'Saturn' : {
        'GRAVITY' : -11.08,
        'UNITS_OF_FUEL' : 300
    },
    'Jupiter' : {
        'GRAVITY' : -25.95,
        'UNITS_OF_FUEL' : 500
    },
    'Mars' : {
        'GRAVITY' : -3.77,
        'UNITS_OF_FUEL' : 550
    },
    'Venus' : {
        'GRAVITY' : -8.87,
        'UNITS_OF_FUEL' : 600
    },
    'Mercury' : {
        'GRAVITY' : -3.59,
        'UNITS_OF_FUEL' : 650
    },
    'Sun' : {
        'GRAVITY' : -274.13,
        'UNITS_OF_FUEL' : 700
    }

}


#Function that asks the user for the amount of fuel to use and returns the user_input
#Takes amount of remaining fuel as an argument
def ask_fuel(current_fuel):

    valid = False

    while not valid:

        try:
            #Prompt the user for amount of fuel to use
            user_input = int(input("Enter the units of fuel to use.").strip())

            if (user_input > current_fuel):
                print("Not enough fuel. Max fuel: %d" %current_fuel)

                print("Please provide a valid input!")

            elif (user_input <0 ):
                print("The amount of fuel to burn must be a valid positive number!")

                print("Please provide a valid input!")

            else:
                valid = True
                return user_input

        except:
            print("Please provide a valid integer input!")
            continue


#Function that performs the necessary calculations.
#Takes the amount of fuel entered by user and the gravity of the current level as arguments
#Returns the value for recent altitude
def perform_calculations(user_fuel,gravity):
    global units_of_fuel
    global velocity
    global altitude
    global number_of_seconds_passed

    units_of_fuel = units_of_fuel - user_fuel  #Remove fuel from the tank

    velocity = velocity +  gravity + THRUSTER_ACCELERATION * user_fuel #Update velocity

    altitude = altitude + velocity #Update altitude
    if altitude < 0.0:
        altitude = 0.0
    number_of_seconds_passed = number_of_seconds_passed + 1  #Record that a second passed

    #Print the information for the user/player
    print("After %d seconds Altitude is %0.2f meters, velocity is %0.2f m/s." %(number_of_seconds_passed,altitude ,velocity))
    print("Remaining Fuel: %d units" %units_of_fuel)

    return altitude


#Function that prints the information about the current level
#Takes name of the level, it's pull of gravity, and the amount of fuel as arguments
#Allows the user to play the game until the altitude is greater than 0 meters
def play_level(name, pull_of_gravity, fuel):
    #stating global variables
    global altitude
    global level
    global number_of_seconds_passed
    global velocity

    #printing level details
    print("Entering level %d" % (level + 1))
    print("Landing on the %s" %name)
    print("Gravity is %0.2f m/s^2" % pull_of_gravity)
    print("Initial Altitude: %d meters" %altitude)
    print("Initial Velocity: %0.2f m/s" %velocity)
    print("Burning a unit of fuel causes 0.10 m/s slowdown.")
    print("Initial Fuel Level: %d units" %fuel)
    print("GO")

    #Check for the altitude
    while altitude > 0:


        #Get the fuel to be used from the user/player
        user_fuel = ask_fuel(units_of_fuel)


        #Call function perform_calculations()
        altitude = perform_calculations(user_fuel, pull_of_gravity)
        #Check if landed safely or crashed
        if altitude <= 0:
            if velocity > -2 and velocity < 2:
                print('Landed Safely!')
                level += 1
                #Reset the values for altitude, number_of_seconds_passed, velocity
                altitude = 50
                velocity = 0.0
                number_of_seconds_passed = 0
                welcome_msg()
            else:
                print("Crashed!")
                # Reset the values for altitude, number_of_seconds_passed, velocity
                altitude = 50
                velocity = 0.0
                number_of_seconds_passed = 0
                welcome_msg()
    return


#Set a boolean variable to check if to print the welcome quote or not
print_welcome_note = True

#Function that prints the welcome message, prompts the player to whether play the game or not
def welcome_msg():

    global units_of_fuel
    global print_welcome_note
    welcome_quote = "Welcome to the Lunar Lander Game."

    if print_welcome_note != False:
        print(welcome_quote)
        print_welcome_note = False


    valid = False
    while not valid:
        user_decision = input("Do you want to play level %d? (yes/no)" %(level + 1)).strip().lower()
        if user_decision == 'no':
            print("The game wil now exit!\nThank you for playing.")


            print("You made to past %d levels." %level)
            sys.exit(0) #Exit the program
        elif user_decision == 'yes':
            valid = True
            level_name = level_names[level]
            level_gravity = level_details[level_name]['GRAVITY']
            units_of_fuel = level_details[level_name]['UNITS_OF_FUEL']

            #Call the function play_level
            play_level(level_name,level_gravity, units_of_fuel)
        else:
            print("Please give the valid response.")

    return


#Call the welcome_msg function and start the game.
welcome_msg()


