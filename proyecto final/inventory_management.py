class Inventory_manegment:
    def main_inventory_manegment_menu():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def show_inventory_manegment():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Edit book location")
            print ("2. Edit book stock")
            print ("3. Delete book ")
            print ("4. exit ")
            
            
            print ("choose one option ")
        
            opcion = Inventory_manegment.main_inventory_manegment_menu()
        
            if opcion == 1:
                
                fh = open("books_inventory.txt", "r")
                word = input("Enter the name of the book : ") 
                new_location = input("Enter the new location : ") 
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
                        stock_count= ("Location"+ l[2])
                        stock_count = new_location
                        l[2] = new_location
                        print("new location",new_location)
                        print(("|").join(l))
                    new_line = ("|").join(l)               
                    data += new_line
                    
                print("New location Save: ")
                print(data)
                fh.close()


                with open("books_inventory.txt", "w") as file:
                    file.writelines( data )
                
                print ("Option 1")
            elif opcion == 2:
                fh = open("books_inventory.txt", "r")
                word = input("Enter the name of the book : ") 
                new_location = input("Enter the new location : ") 
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
                fh.close()


                with open("books_inventory.txt", "w") as file:
                    file.writelines( data )
                
                print ("Option 2")
            elif opcion == 3:
                fh = open("books_inventory.txt", "r")
                word = input("Enter the name of the book : ") 
                s = " "
                count = 1
                data = ""
                book_found = False
                while(s):
                    s=fh.readline()
                    l=s.split("|")
                    print(l)
                    if word in l[0] and book_found == False:
                        print("Book sucefully deleted")  

                # Write file
                with open("books_inventory.txt", 'w') as fp:
                    # iterate each line
                    for number, line in enumerate(fh):
                        # delete line 5 and 8. or pass any Nth line you want to remove
                        # note list index starts from 0
                        if number not in [0,1,2,3]:
                            fp.write(line)
                print("Option 3")
            elif opcion == 4:
                salir = True
                
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")