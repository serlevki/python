import sys

filename = "somefile.txt"

while True:
    try:
        print("we are inside try")
        myfile = open(filename, mode='r')
    except Exception:
        print("we are insid exception")
        print("errror found")
        print(sys.exc_info()[1])
        filename = input("Give me right name: ")
    else:
        print("we are inside else")
        print(myfile.read())
        sys.exit()

print("---------eof------------------")