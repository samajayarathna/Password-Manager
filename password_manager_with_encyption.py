
#display Welcome to Password manager when program starts
print("\nWelcome to Password manager\n")

choice = 0
charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`!@#$%^&*(+)_-=|\"':;?/>.<, "




def add_data():

    #create a file called credentials.txt if it doesnt exist
    myfile =open("credentials.txt ", "a")
    
    # get data from the user
    userName = input("Please enter User name ")
    password = input("Enter password ")
    url = input("Enter URL/Source ")
    
    encryUserName = " ".join([charset[(charset.find(c)+3)%95] for c in userName])
    encryPassword = " ".join([charset[(charset.find(c)+3)%95] for c in password])
    encryUrl = " ".join([charset[(charset.find(c)+3)%95] for c in url])
    
    #write data to the file
    myfile.write(encryUserName)
    myfile.write(encryPassword)
    myfile.write(encryUrl) 
   
    #close the file
    myfile.close()

    # display message 
    print("\nSuccessfully added your credentials\n\n")

def display_data():
    
    #f=open("credentials.txt ", "a")
    f =open('credentials.txt','r')

    #display data in command prompt
    data = f.read()
    f.close()

    decryptData = " ".join([charset[(charset.find(c)-3)%95] for c in data])
    dataList = decryptData.split()
    
    print(f"{'User Name' :10} {'Password' : ^20} {'URL/Source' : >10}")
    
    i = 0
    while i < len(dataList):
        print(f"{dataList[i] :10} {dataList[i+1] : ^20} {dataList[i+2] : >10}")
        i = i + 3

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