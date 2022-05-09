fname = input("Enter file name: ")

# check if files exists, if not then quit
try:
    fh = open(fname)
except:
    print("invalid file")
    quit()

lst = list()

# for each line in the file, append the words of the line to the list
# if it's not already in the list
for line in fh:
    split_boys = line.split()
    for element in split_boys:
        if not element in lst:
            lst.append(element)

lst.sort()
print(lst)
