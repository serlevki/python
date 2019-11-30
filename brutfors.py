inputfile = "../names.txt"
outputfiles = "../out.txt"

password_to_lokk_for = "qwerty"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfiles, mode='a', encoding='latin_1')

for num, line in enumerate(myfile1, 1):
    if password_to_lokk_for in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile2.write("Found password: " + line)

myfile1.close()
myfile2.close()