class Account_manegment:
    def main_admin_menu():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
class Account_manegment:
    def account_manegment_menu():
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def show_account_manegment():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Edit user  ")
            print ("2. Delete user ")
            print ("3. search user")
            print ("4. exit ")
            
            
            print ("choose one option ")
        
            opcion = Account_manegment.account_manegment_menu()
        
            if opcion == 1:
                fh = open("sigin_user.txt", "r")
                word = input("Enter your name ") 
                new_location = input("Enter the new user name : ") 
                s = " "
                count = 1
                data = ""
                book_found = False

                while(s):
                    s=fh.readline()
                    l=s.split("|")
                    print(l)
                    
                    if word in l[0] and book_found == False:
                        print("book found :", count, ":",s)  
                        stock_count= ("Location"+ l[3])
                        stock_count = new_location
                        l[3] = new_location
                        print("new location",new_location)
                        print(("|").join(l))
                    new_line = ("|").join(l)               
                    data += new_line
                    
                print("New location Save: ")
                print(data)
                fh.close()

                with open("sigin_user.txt", "w") as file:
                    file.writelines( data )
                
                print ("Option 1")
            elif opcion == 2:
                fh = open("sigin_user.txt", "r")
                word = input("Enter the name of user : ") 
                s = " "
                count = 1
                data = ""
                book_found = False
                while(s):
                    s=fh.readline()
                    l=s.split("|")
                    print(l)
                    if word in l[0] and book_found == False:
                        print("user sucefully deleted")  

                # Write file
                with open("sigin_user.txt", 'w') as fp:
                    # iterate each line
                    for number, line in enumerate(fh):
                        if number not in [0,1,2,3,4]:
                            fp.write(line)
                print("Option 3")
            elif opcion == 3:
                user_search = input(" Enter the name of the book: ")
                # opening a text file
                file1 = open("sigin_user.txt", "r")
                # setting flag and index to 0
                flag = 0
                index = 0
                # Loop through the file line by line
                for line in file1:  
                    index += 1 
                    
                    # checking string is present in line or not
                    if user_search  in line:   
                        flag = 1
                    break 
                        
                # checking condition for string found or not
                if flag == 0: 
                    print('User', user_search , 'Not Found') 
                else: 
                    print('user', user_search , 'Found')
                # closing text file    
                file1.close() 
                print("Book Seach Menu")
                print("Option 3")
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")