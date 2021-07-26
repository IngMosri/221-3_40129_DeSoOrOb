
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
                print ("Option 1")
            elif opcion == 2:
                print ("Option 2")
                salir = True
            else:
                print ("Choose the option beetween 1 and 3")
        