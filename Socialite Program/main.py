#Name: Samyam C. Shrestha
#Drexel ID: ss4674
#Course: CS-172-A
#Lab Section: CS-172-061

#import statements
from socialite import  Socialite

#define list variable
socialite_list =[]


print("Welcome to CS 172: Socialite Homework")


#Prompt the user for number of socialites
valid = False
while not valid:
    try:
        num_socialite = int(input("How many socialites do you want to create?\n"))
        valid = True

    except:
        print("Please enter a valid integer input.")

#Prompt the user to fill out all six attributes for each socialite
counter = 1
while num_socialite >= 1:
    print("Enter the data for Socialite " + str(counter))
    first_name = input("Enter the First Name:\n")
    last_name = input("Enter the Last Name:\n")
    user_id = input("Enter the User ID:\n")
    picture = input("Enter the URL for Picture:\n")
    website = input("Enter the URL for Website:\n")
    description = input("Enter the Website Description:\n")

    #create the object for Socialite class and populate the attributes
    obj = Socialite(first_name,last_name,picture,website,description,user_id)
    obj.setFirstName(first_name)
    obj.setLastName(last_name)
    obj.setUserID(user_id)
    obj.setPicture(picture)
    obj.setWebsite(website)
    obj.setDescription(description)
    socialite_list.append(obj)
    print(obj)


    counter += 1
    num_socialite -= 1


#Method to create the Socialite profile files
def create_files():
    for each in socialite_list:
        file_name = each.user_id+".html"



        with open(file_name,'w') as htmlFile:
            htmlFile.write(each.html())


#Method to create index.html file
def create_index_file():
    header_string ="<html>\n\t<head>\n\t\t<title>List of Socialite Profiles</title>\n\t</head>\n\t<body>\n\t\t" \
                   "<h2>List of Socialite Profiles</h2>\n\t\t"
    footer_string = "\n\t</body>\n</html>"
    write_header = True


    index_file_present = False  #Check if the index file is present or not

    try:
        #Read the index file
        with open("index.html", 'r') as mainFile:
            index_file_present = True
            file_content = mainFile.readlines()
            # x = mainFile.tell()
            # mainFile.seek(x)

            #Check for the presence of header and footer
            for line in file_content:
                if ("<html>" in line)== True:
                    write_header = False
                if ("</body>" in line) == True:
                    file_content.pop()
                    file_content.pop()
    except FileNotFoundError:
        print("Index File not Present. Creating a new Index File.")

    #write to the index file
    with open("index.html",'w') as mainFile:
        if write_header == True:
            mainFile.write(header_string)
        if index_file_present == True:
            mainFile.writelines(file_content)
        for each in socialite_list:
            str = "<p><a href=\"{0}\">{1} {2}</a></p>\n\t\t".format(each.user_id+".html",each.first_name,each.last_name)
            mainFile.write(str)
        mainFile.write(footer_string)




#Method Calls
create_files()
create_index_file()