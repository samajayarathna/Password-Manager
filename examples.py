import io

# with open("credentials.txt ", "a+") as file_object:
#     file_object.seek(0)
#     data = file_object.read(100)
#     if len(data) >0 :
#         file_object.write("\n")
#         file_object.write("hello")

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


    