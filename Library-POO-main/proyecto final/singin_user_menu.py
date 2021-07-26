class Signin_user:
   
    
    def show_signin_user():
        opcion = 0
        outfile = open('sigin_user.txt','a' ) 
        
        full_name = input("What is your name? ")
        email = input("Whats your email address ")
        school_id =input("Enter your school ID ")
        
        outfile.write("Full name " + full_name + "\n" )
        outfile.write("Email address " + email + "\n")
        outfile.write("School is " + str(school_id) + "\n")
        outfile.close()
        
        
        
           

            
            
            
                  

