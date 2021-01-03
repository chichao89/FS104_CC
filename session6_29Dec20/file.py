filestring = str(input("Enter a text"))

def file_content(string):
    file = open("test2.txt","w")
    file.write(string)
    file.close()

file_content(filestring)