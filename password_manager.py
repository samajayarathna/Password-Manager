import io
#display Welcome to Password manager when program starts
print("\nWelcome to Password manager\n")

#def encryption (cleartext):
    # charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`!@#$%^&*()_-=|\"':;?/>.<, "
    # encText = " ".join([charset[(charset.find(c)+3)%95] for c in cleartext])
    # print(encText)

def add_data():
    
    #create a file called credentials.txt if it doesnt exist
    myfile = open("credentials.txt ", "a")

    with open("credentials.txt ", "a+") as myfile:
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
        myfile.writelines(encText)
        
        # add URL/Source to the file
        url = input("Enter URL/Source ")
        myfile.writelines(url)

       
    #close the file
    myfile.close()

    # display message 
    print("\nSuccessfully added your credentials\n\n")

def display_data():
    f = open("credentials.txt", "r")

    with open('credentials.txt','r') as f:
        print(f"{'User Name' :28} {'Password' : ^28} {'URL/Source' : >28}")
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
