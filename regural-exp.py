import re

input_filename = "../dumpfile.txt"
output_filename = "../resultfile.txt"

input_f = open(input_filename, mode = 'r', encoding='Latin-1')
output_f = open(output_filename, mode = 'w', encoding='Latin-1')

mytext = input_f.read()

look_for = r"[\w._-]+@[\w._-]+\.[\w.]+" #regular expressions for finding email address

results = re.findall(look_for, mytext)

for item in results:
    print(item)
    output_f.write(item + "\n")

print("Total: " + str(len(results)))

input_f.close()
output_f.close()