import io



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

# with open('credentials.txt','r') as f:
# 	listl=[]
# 	for line in f:
# 		print(f)
		
# with open('credentials.txt') as f:
#     for index, line in enumerate(f):
#         print("User  {}: {}".format(index, line.strip()))
#         print()

with open('credentials.txt','r') as f:
    lines = [line.strip() for line in f]
    print(lines)

    
        

# with open('credentials.txt','r') as fp:
#    line = fp.readline()
#    cnt = 1
#    for line in fp:
#        #print("User name {}: {}".format(cnt, line.strip()))
#        print("User name {}: {}".format(cnt ,line.strip()))
#        line = fp.readline()
       

