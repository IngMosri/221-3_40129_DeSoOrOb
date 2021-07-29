# with is like your try .. finally block in this case
fh = open("/Users/christianmosrialatorre/Documents/OneDrive - Instituto Superior Autonomo de Occidente A.C/8 cuatrimestre/USB/ProgramacionOrientadaObjetos/Library-POO-main/books_inventory.txt", "r")
word = input("Enter the name of the book : ") 
s = " "
count = 1
while(s):
    s=fh.readline()
    l=s.split()
if word in l:
    print("book found :", count, ":",s)  
with open('books_inventory.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()
with open('books_inventory.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

print(data)
print("nuevo stock " + data[0])

# now change the 2nd line, note that you have to add a newline
data[6] = '2\n'

# and write everything back
with open('books_inventory.txt', 'w') as file:
    file.writelines( data )