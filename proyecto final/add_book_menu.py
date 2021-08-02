#!/usr/bin/python3
class Add_book_menu:
       
    def show_add_book():
        opcion = 0
        outfile = open('books_inventory.txt','a' ) 
        
        book_name = input("Name of the book? ")
        id_code = input("type the ID code of the book ")
        location  =input("Enter the location ")
        stock  =input("Enter the stocks  ")
        
        
        outfile.write("Name of the book " + book_name+ "|" )
        outfile.write("ID code is " + str(id_code ) + "|")
        outfile.write(location + "|" )
        outfile.write(str(stock + "\n"))
        outfile.close()   