import re

name = input("File Name:")
try:
    handle = open(name)
except:
    print("invalid file")

sum = 0

# Go through each line and find the numbers, then add them to the sum
for line in handle:
    numbers = re.findall('[0-9]+', line)
    for element in numbers:
        sum += int(element)
        
print(sum)