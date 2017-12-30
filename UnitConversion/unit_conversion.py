#The purpose of this program is that it does some specific unit conversions.
#Created By: Samyam C. Shrestha
#Lab Section: CS-171-061

#Create dictionary of unit relations by taking inches as a base unit
unit_relations = {
    "inches"        : 1,
    "feet"          : 1 / 12,
    "yards"         : 1 / 36,
    "miles"         : 1 / 63360,
    "leagues"       : 1 / 190080,
    "centimeters"   : 2.54,
    "decimeter"     : 2.54/10,
    "meters"        : 2.54/100,
    "decameters"    : 2.54/1000,
    "hectometers"   : 2.54/10000,
    "kilometers"    : 2.54/100000

}

#Print the welcome message
print('Welcome to the init conversion wizard.')
print('This program can convert between any of the following lengths.')
print('inches\nfeet\nyards\nmiles\nleagues\ncentimeters\ndecimeters\nmeters\ndecameters\nhectometers\nkilometers')
print('Note : You must use the units exactly as spelled above .')

#Prompt the user for inputs
target_value = float(input('Enter value:'))
convert_from = input('Enter from units:')
convert_to = input('Enter to units:')


#perform calculations
#convert target_value to base unit
result = target_value / unit_relations[convert_from]
#convert value in base units to desired units
result = result * unit_relations[convert_to]

#print output
print('%f %s is %f %s' %(target_value, convert_from, result, convert_to))