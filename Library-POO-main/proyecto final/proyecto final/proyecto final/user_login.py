#!/usr/bin/python3
class User_login:
    def user_login_main_menu():
            
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the followingggg option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         

    
    def user_login_menu():       
        fh = open("/Users/christianmosrialatorre/Documents/OneDrive - Instituto Superior Autonomo de Occidente A.C/8 cuatrimestre/USB/ProgramacionOrientadaObjetos/Library-POO-main/sigin_user.txt", "r")
        user_name = input("Enter the your name : ") 
        password = input("Enter the your password : ") 
        s = " "
        count = 1
        while(s):
            s=fh.readline()
            l=s.split()
        if user_name in l:
            print("Usuario found:", count, ":",s) 
        elif password in l:
            print("password correcto:", count, ":") 

        
        
                
                
            
                
        
        
                    
    