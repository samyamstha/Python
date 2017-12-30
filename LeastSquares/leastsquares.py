#Created By: Samyam C. Shrestha
#Lab Section: CS-171-061
import csv
import math
import sys


#Welcome message and prompt the user for inputs
print('Welcome to the Linear Regression Generator.')

input_flag = True
header = [] #Contain the headers of the given data
x_values = []
y_values = []
slope_num = 0.0
slope_dem = 0.0
estimated_values = []
errors = []
regression_standard_error = 0.0

while (input_flag):
    #Check for the errors
    try:
        file_name = input("Enter a File Name Containing Data:")
        with open(file_name, 'r') as csvfile:

            print('Reading file.....')
            file_reader = csv.reader(csvfile)


            first_row_check = 0
            for row in file_reader:
                #Avoid the first row
                if first_row_check == 0:
                    first_row_check += 1
                    header.append(row[0])
                    header.append(row[1])
                    continue
                #Check for bad value in the file
                (type(int(row[0])))


                #Populate x_values and y_values lists. Also, convert the values from string to int and float
                x_values.append(int(row[0]))
                y_values.append(float(row[1]))

                print(row)
            #Printing list of x values
            print("X-values : ",x_values)
            print("Y-values : ",y_values )

            #Calculate the average of the x-values and y-values
            avg_x_values = sum(x_values) / len(x_values)
            avg_y_values = sum(y_values) / len(y_values)
            print(avg_x_values,',',avg_y_values)

            #Calculate slope_num and slope_dem
            for i in range(len(x_values)):
                slope_num += ((x_values[i] - avg_x_values) * (y_values[i] - avg_y_values))
                slope_dem += (x_values[i] - avg_x_values) ** 2

            slope = slope_num / slope_dem

            #Calculate the b-intercept
            b_intercept = avg_y_values - (slope * avg_x_values)
            #Determine the sign to be displayed for b_intercept while printing
            if b_intercept >= 0:
                sign = '+'
            else:
                sign = ''

            #Calculate the estimated value and populate the estimated_values list
            for j in range(len(x_values)):
                estimated_values.append((slope * x_values[j]) + b_intercept)

            #Calculate the error and populate the errors list
            for k in range(len(x_values)):
                errors.append(abs(y_values[k] - estimated_values[k]))

            #Calculate average error for known values
            avg_error = sum(errors) / len(errors)

            #Calculate mean square error and regression standard error
            total = 0.0
            for l in range(len(x_values)):
                total += ((y_values[l] - estimated_values[l]) ** 2)

            mean_square_error = (1 / (len(x_values) - 2)) * total
            regression_standard_error = math.sqrt(mean_square_error)
            # print(total)
            # print("Regression Standard Error: ", regression_standard_error)
            # print("MSE: ", mean_square_error)
            print("Errors: ", errors)
            # print("Estimated values: ", estimated_values)
            # print("m_dem: ", slope_dem)
            # print("m_num: ", slope_num)
            # print("slope: ",slope)
            # print("b-intercept: ", b_intercept)

        #Set the loop condition to false
        input_flag = False

    except FileNotFoundError as e:
        print("Error: File not found!")

    except ValueError as e:
        print('Error: A value in the file could not be read!')
        #Clear the lists
        x_values.clear()
        y_values.clear()
        header.clear()

print("The Linear Regression Line is y ="+str(slope)+'*x'+sign+str(b_intercept)+"." )
print("Average Error for Known Values was +/- ", avg_error,".")
print("Regression Standard Error for Known Values was ", regression_standard_error,".")
print("System ready to make predictions.")
print("To quit, type \'exit\' as the year.")

#Prompt user for the input of x-value
while(True):
    user_input = input("Enter " + header[0]+":")

    if user_input.lower() == 'exit':
        print("Thank You! The program has stopped.")
        sys.exit(0)

    #Check for invalid input
    try:
        type(int(user_input))
    except:
        print("Input could not be understood. Please try again.")
        continue

    prediction = slope * int(user_input) + b_intercept

    print("Prediction when " + header[0] + " =", user_input, "is", header[1], "=", prediction,".")



