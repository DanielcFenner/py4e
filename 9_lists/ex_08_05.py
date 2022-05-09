fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

# Find every line starting with "From " and print the email
# Add to count of lines
for line in fh:
    if not line.startswith("From "):
        continue
    split_line = line.split()
    print(split_line[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")
