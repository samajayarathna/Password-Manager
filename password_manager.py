
#display Welcome to Password manager when program starts
print("\nWelcome to Password manager\n")

#def encryption (cleartext):
    # charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`!@#$%^&*()_-=|\"':;?/>.<, "
    # encText = " ".join([charset[(charset.find(c)+3)%95] for c in cleartext])
    # print(encText)

def add_data():
    #create a file called credentials.txt if it doesnt exist
    myfile = open("credentials.txt ", "a")

    # add user name to the file
    userName = input("Please enter User name ")
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`!@#$%^&*()_-=|\"':;?/>.<, "
    encText = " ".join([charset[(charset.find(c)+3)%95] for c in userName])
    myfile.writelines(encText)

       
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
    print(f.read())


choice = 0
while choice != 'q':
    print("Type 1 to create encryption key\n")
    print("Type 2 to add credentials\n")
    print("Type 3 to View credentials\n")
    print("Type 'q' to Exit ")

    choice = input("\nMake your choice ")
    
    if choice == '1':
        print("Please enter your encryption key\n")
    elif choice == '2':
        add_data()
    elif choice == '3':
        display_data()
    elif choice == 'q':
        break 
    else:
        print("invalid option. Please try again")
