import io




        
# with open('credentials.txt','r') as fp:
#    line = fp.readline()
#    cnt = 1
#    for line in fp:
#        #print("User name {}: {}".format(cnt, line.strip()))
#        print("User name {}: {}".format(cnt ,line.strip()))
#        line = fp.readline()
       
import io


#display Welcome to Password manager when program starts
print("\nWelcome to Password manager\n")


def add_data():
    
    #create a file called credentials.txt if it doesnt exist

    myfile =open("credentials.txt ", "a")
    userName = input("Please enter User name ")
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`!@#$%^&*()_-=|\"':;?/>.<, "
    encText = " ".join([charset[(charset.find(c)+3)%95] for c in userName])

    myfile.seek(0)
    data = myfile.read(100)
    if len(data) >0 :
        myfile.write("\n")
        myfile.write(encText)

    # add password to the file
    password = input("Enter password ")
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`!@#$%^&*()_-=|\"':;?/>.<, "
    encText = " ".join([charset[(charset.find(c)+3)%95] for c in password])
    myfile.write(encText)
        
    # add URL/Source to the file
    url = input("Enter URL/Source ")
    myfile.write(url)

       
    #close the file
    myfile.close()

    # display message 
    print("\nSuccessfully added your credentials\n\n")

def display_data():
    
    print(f"{'User Name' :28} {'Password' : ^28} {'URL/Source' : >28}")
    f =open('credentials.txt','r')
    lines = [line.strip() for line in f]
    print(lines)
        
    #print(f"{num1 : <28} {num2 : ^28} {num3 : >28}")

choice = 0
while choice != 'q':
    print("\nType 1 to add credentials\n")
    print("Type 2 to View credentials\n")
    print("Type 'q' to Exit ")

    choice = input("\nMake your choice ")
    
    
    if choice == '1':
        add_data()
    elif choice == '2':
        display_data()
    elif choice == 'q':
        break 
    else:
        print("invalid option. Please try again")

