name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()

# For each line in the file starting with "From " find and split
# out the hour and build a dictionary with the count of each hour
for line in handle:
    if not line.startswith("From "):
        continue

    split_line = line.split()
    split_time = split_line[5].split(":")
    hour = split_time[0]
    
    dic[hour] = dic.get(hour, 0) + 1

# Build a list of key value pairs from the dictionary and sort it
dic_list = []
for k, v in dic.items():
    new_tup = (k, v)
    dic_list.append(new_tup)

dic_list.sort()

# print out each key value pair from the dictionary now they're sorted
for item in dic_list:
    print(item[0], item[1])
