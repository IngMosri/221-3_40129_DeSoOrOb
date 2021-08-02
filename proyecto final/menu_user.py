#!/usr/bin/python3
import singin_user_menu
import user_login
import rent_book
class Menu_user:
    def user_main_menu():
        
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num

    def show_menu():

        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Login Menu")
            print ("2. Sign") 
            print("3 Rent Book")         
            print ("4. Exit")
            
            print ("choose one option ")
        
            opcion = Menu_user.user_main_menu()
        
            if opcion == 1:
                user_login.User_login.user_login_menu()
                print ("Login sucefully")
            elif opcion == 2:
                singin_user_menu.Signin_user.show_signin_user()
                print ("Option 2")
            elif opcion == 3:
                rent_book.Rent_book.show_user_rent_book()
                print("Option 3")
                salir = True
            elif opcion == 4:
                print("Option 4")
                salir = True
            else:
                print ("Choose the option beetween 1 and 3")
        