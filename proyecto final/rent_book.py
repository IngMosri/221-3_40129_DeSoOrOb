#!/usr/bin/python3
import ticket_book
class Rent_book:
    def rent_book_menu():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def show_user_rent_book():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Rent book ")
            print ("2. Check Fines")
            print ("3. exit ")
            
            
            print ("choose one option ")
        
            opcion = Rent_book.rent_book_menu()
        
            if opcion == 1:
                ticket_book.Ticket_book.ticket_book_info()
                print ("Comeback soon ")
            elif opcion == 2:
                user_search = input(" Enter the user name ")
                # opening a text file
                fh = open("fines.txt", "r")
                s = " "
                count = 1
                data = ""
                book_found = False
                while(s):
                    s=fh.readline()
                    l=s.split("|")
                    print(l)
                    print ("Fines Menu")
            elif opcion == 3:
                print("Option 3")
                salir = True
            else:
                print ("Choose the option beetween 1 and ")