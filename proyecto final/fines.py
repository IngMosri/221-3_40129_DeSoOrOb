user_search = input(" Enter the user name ")
# opening a text file
fh = open("fines.txt", "r")
s = " "
count = 1
data = ""
book_found = False
while(s):
    s=fh.readline()
    l=s.split("|")
    print(l)