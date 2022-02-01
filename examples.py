
#display Welcome to Password manager when program starts
print("\nWelcome to Password manager\n")

choice = 0

def add_data():
    #create a file called credentials.txt if it doesnt exist
    myfile =open("credentials.txt ", "a")
    userName = input("Please enter User name ")
    myfile.write("\n")
    myfile.write(userName)
    # add password to the file
    password = input("Enter password ")
    myfile.write(password)
    # add URL/Source to the file
    url = input("Enter URL/Source ")
    myfile.write(url) 
    #close the file
    myfile.close()
    # display message 
    print("\nSuccessfully added your credentials\n\n")

def display_data():
    f =open('credentials.txt','r')
    Lines = f.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("User {}: {}".format(count, line.strip()))
        
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

