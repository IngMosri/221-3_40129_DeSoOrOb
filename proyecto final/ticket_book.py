#!/usr/bin/python3
import datetime
class Ticket_book:

    def ticket_book_info():
    
        fh = open("books_inventory.txt", "r")
        word = input("Enter the name of the book you want to rent : ") 
        s = " "
        count = 1
        data = ""
        book_found = False
        while(s):
            s=fh.readline()
            l=s.split("|")
            if word in l[0] and book_found == False:
                print("Book Found:")  
                stock_count= int(l[3])
                stock_count = stock_count-1
                l[3] = str(stock_count)
            new_line = ("|").join(l)

        
            data += new_line
        print("Biblioteca Publica el Estado de JALISCO Juan Jose Arreola" + "\n" )
        print("book successfully rented"  + "\n" )
        print("return the book 5 days after the date to avoid fines." + "\n" )
        now = datetime.datetime.now()
        print("Current date and time: "  + "\n" )
        print(str(now))

        fh.close()


        with open("books_inventory.txt", "w") as file:
            file.writelines( data )