
#display Welcome to Password manager when program starts
print("\nWelcome to Password manager\n")

choice = 0

def add_data():

    #create a file called credentials.txt if it doesnt exist
    myfile =open("credentials.txt ", "a")

    # add username to the file
    userName = input("Please enter User name ")
    myfile.write("\n")
    myfile.write(userName)
    
    # add password to the file
    password = input("Enter password ")
    myfile.write(' ')
    myfile.write(password)
    
    # add URL/Source to the file
    url = input("Enter URL/Source ")
    myfile.write(' ')
    myfile.write(url) 
   

    #close the file
    myfile.close()

    # display message 
    print("\nSuccessfully added your credentials\n\n")

def display_data():
    
    #print(f"{'User Name' :10} {'Password' : ^20} {'URL/Source' : >10}")
    f =open('credentials.txt','r')

    #display data in command prompt
    line_list = f.readlines()
    items = []
    for x in line_list:
        items.append(x)
    print(items)

#display choices to the user
while choice != 'q':
    print("\nType 1 to add credentials\n")
    print("Type 2 to View credentials\n")
    print("Type 'q' to Exit ")
    #ask choice from the user
    choice = input("\nMake your choice ")
    if choice == '1':
        #call function add_data
        add_data()
    elif choice == '2':
        #call function display_data
        display_data()
    elif choice == 'q':
        break 
    else:
        print("invalid option. Please try again")

