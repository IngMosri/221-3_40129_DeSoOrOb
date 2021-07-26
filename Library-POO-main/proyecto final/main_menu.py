import menu_user
import admin_menu
class Main_Menu:
    def menu_library():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
     
    salir = False
    opcion = 0
     
    while not salir:
     
        print ("1. Admin Menu")
        print ("2. User menu")
        print ("3. Salir")
         
        print ("choose one option ")
     
        opcion = menu_library()
     
        if opcion == 1:
            admin_menu.Admin_menu.show_admin_menu()
            print ("Option 1")
        elif opcion == 2:
           
            menu_user.Menu_user.show_menu()    
            print ("Option 2")
        elif opcion == 3:
            salir = True
        else:
            print ("Choose the option beetween 1 and 3")
     
    print ("End")