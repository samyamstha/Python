#Name: Samyam C. Shrestha
#Drexel ID: ss4674
#Course: CS-172-A
#Lab Section: CS-172-061

class Socialite:

    #set all attributes to empty string
    def __init__(self, last_name, first_name, picture, website, description, user_id):
        self.last_name = ""
        self.first_name = ""
        self.picture = ""
        self.website = ""
        self.description = ""
        self.user_id = ""

    #Returns a string with all attributes as plain text format.
    def __str__(self):

        output_string = "Socialite Created\nName: {0} {1}\nUser ID: {2}\nPicture: {3}\nWebsite: {4}\nWebsite Description: {5}" .format(self.first_name,self.last_name,self.user_id,self.picture,
                                                                                                            self.website,self.description)
        return output_string

    #Returns a string with all attributes in HTML format.
    def html(self):

        output_string = "<html>\n\t<head>\n\t\t<title>{0} {1}\'s Socialite Page</title>\n\t</head>\n\t<body>\n\t\t<img width=\"400px\" src=\"{2}\"" \
                        " alt=\"{0} {1}\'s Picture\" align=\"Right\"/>\n\t\t<h1>{3}</h1>\n\t\t<h2>{0} {1}</h2>\n\t\t<hr/>\n\t\t<p>\n\t\t\t{0} wants to share\n\t\t\t" \
                        "<a href=\"{4}\" target=\"_blank\">\n\t\t\t{5}</a>\n\t\t\t with you:<br />\n\t\t\t{4}\n\t\t</p>\n\t</body>\n</html>" \
                        .format(self.getFirstName(), self.getLastName(), self.getPicture(), self.getUserID(),
                           self.getWebsite(), self.getDescription())


        # output_string = "<html>\n\t<head>\n\t\t<title>%s %s\'s Socialite Page</title>\n\t</head>\n\t<body>\n\t\t<img width=\"400px\" src=\"%s\"" \
        #                 " alt=\"%s %s\'s Picture\" align=\"Right\"/>\n\t\t<h1>%s</h1>\n\t\t<h2>%s %s</h2>\n\t\t<hr/>\n\t\t<p>\n\t\t\t%s wants to share\n\t\t\t" \
        #                 "<a href=\"%s\" target=\"_blank\">\n\t\t\t%s</a>\n\t\t\t with you:<br />\n\t\t\t%s\n\t\t</p>\n\t</body>\n</html>" \
        #                 %(self.first_name,self.last_name,self.picture,self.first_name,self.last_name,self.user_id,self.first_name,self.last_name,
        #                   self.first_name,
        #                   self.website,self.description,self.website)
        return output_string


    #Mutator methods
    def setLastName(self,l):
        self.last_name = l
    def setFirstName(self,f):
        self.first_name = f
    def setPicture(self,p):
        self.picture = p
    def setWebsite(self,w):
        self.website = w
    def setDescription(self,d):
        self.description = d
    def setUserID(self,u):
        self.user_id = u

    #Accessor Methods
    def getLastName(self):
        return self.last_name
    def getFirstName(self):
        return  self.first_name
    def getPicture(self):
        return self.picture
    def getWebsite(self):
        return self.website
    def getDescription(self):
        return self.description
    def getUserID(self):
        return self.user_id

    






   