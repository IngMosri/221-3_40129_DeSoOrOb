#!/usr/bin/python3
import add_book_menu
import inventory_management
class Inventory_menu:
    def inventory_management():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def show_inventory_menu():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Add new book ")
            print ("2. inventory management")
            print ("3. show inventory")
            print ("4. exit ")
            
            print ("choose one option ")

            opcion = Inventory_menu.inventory_management()
        
            if opcion == 1:
                add_book_menu.Add_book_menu.show_add_book()
                print ("Option 1")
            elif opcion == 2:
                inventory_management.Inventory_manegment.show_inventory_manegment()
                
                print ("Option 2")
            elif opcion == 3:
                fh = open("books_inventory.txt", "r")
                s = " "
                count = 1
                data = ""
                book_found = False
                while(s):
                    s=fh.readline()
                    l=s.split("|")
                    print(l)
                print("Inventory menu")
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")
        