#!/usr/bin/python3


class Signin_user:
    
   
    
    def show_signin_user():

        opcion = 0
        outfile = open('sigin_user.txt','a' ) 
        
        full_name = input("What is your name? ")
        email = input("Whats your email address ")
        school_id =input("Enter your school ID ")
        user_name =input("Enter your user name")
        password =input("Enter your Password  ")
        
        
        outfile.write("Full name " + full_name + "|" )
        outfile.write("Email address " + email + "|")
        outfile.write("School is " + str(school_id) + "|")
        outfile.write("Your user name is " + user_name + "|")
        outfile.write("Your password is " + password  + "|")
        outfile.close()
        
        
        
           

            
            
            
                  

