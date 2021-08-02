#!/usr/bin/python3
import add_book_menu
import inventory_menu
import account_manegment
import search_book_menu
class Admin_menu:
    def main_admin_menu():
        
        complete = False
        user = {"username1" : "12345", "username2" : "67890" }
        
        while not complete:
            username = input("Username: ")
            password = input("Password: ")
            if username == user and password == password:
                continue
            elif username not in user:
                print("This is not a valid username, input username again!")
                continue
            elif password != user[username]:
                print(f"Password is not valid for {username}. ")
                continue
            elif password == user[username]:
                print(f"Welcome {username} ")
                print(f"Thank you for logging on. ")
                complete = True
        
        print ("login sucefully")
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def show_admin_menu():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. inventory Control ")
            print ("2. Account manegment")
            print ("3. book search")
            print ("4. exit ")
            
            
            print ("choose one option ")
        
            opcion = Admin_menu.main_admin_menu()
        
            if opcion == 1:
                inventory_menu.Inventory_menu.show_inventory_menu()
                print ("Option 1")
            elif opcion == 2:
                print ("Option 2")
                account_manegment.Account_manegment.show_account_manegment()
            elif opcion == 3:
                search_book_menu.Search_book.show_search_book_menu()
                print("Option 3")
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")