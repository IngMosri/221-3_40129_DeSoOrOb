#!/usr/bin/python3
class Search_book:
    def search_book_menu():
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')    
        return num

    def show_search_book_menu():

        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. For search book")
            print ("2.  Exit ")
            
            print ("choose one option ")
        
            opcion = Search_book.search_book_menu()
        
            if opcion == 1:
                book_search = input(" Enter the name of the book: ")
                # opening a text file
                file1 = open("books_inventory.txt", "r")
                # setting flag and index to 0
                flag = 0
                index = 0
                # Loop through the file line by line
                for line in file1:  
                    index += 1 
                    
                    # checking string is present in line or not
                    if book_search  in line:   
                        flag = 1
                    break 
                        
                # checking condition for string found or not
                if flag == 0: 
                    print('Book', book_search  , 'Not Found') 
                else: 
                    print('Book', book_search , 'Found in the Inventory')
                # closing text file    
                file1.close() 
                print("Book Seach Menu")
                
            elif opcion == 2:
                print ("Option 2")
                salir = True
            else:
                print ("Choose the option beetween 1 and 3")