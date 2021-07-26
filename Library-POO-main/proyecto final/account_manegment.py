class Acc:
    def main_admin_menu():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
class Account_manegment:
    def account_manegment_menu():
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def show_account_manegment():
     
        salir = False
        opcion = 0
        
        while not salir:
        
            print ("1. Edit book location  ")
            print ("2. Delete book ")
            print ("3. Edit book stock")
            print ("4. exit ")
            
            
            print ("choose one option ")
        
            opcion = Account_manegment.account_manegment_menu()
        
            if opcion == 1:
                print ("Option 1")
            elif opcion == 2:
                print ("Option 2")
            elif opcion == 3:
                print("Option 3")
            elif opcion == 4:
                salir = True
            else:
                print ("Choose the option beetween 1 and ")