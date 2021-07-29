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
        print("book found :", count, ":",s)  
        stock_count= int(l[2])
        stock_count = stock_count-1
        l[2] = str(stock_count)
        print("new Stock ",stock_count)
        print(("|").join(l))
    new_line = ("|").join(l)

 
    data += new_line
print("data")
print(data)
fh.close()


with open("books_inventory.txt", "w") as file:
    file.writelines( data )
