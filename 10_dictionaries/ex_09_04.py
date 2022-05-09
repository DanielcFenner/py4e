name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic = dict()

# For each in line file, find lines starting with "From " and
# split the email out, add to dictionary and count it in dic
for line in handle:
    if not line.startswith("From "):
        continue

    split_line = line.split()
    email = split_line[1]
  
    dic[email] = dic.get(email, 0) + 1

# Find which key value was the biggest in dictionary
biggestValue = 0
biggestKey = ""
for key, value in dic.items():
    if value > biggestValue:
        biggestValue = value
        biggestKey = key

print(biggestKey, biggestValue)
