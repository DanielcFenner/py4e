# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file")
    quit()

lines = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lines += 1
    index = line.find("0")
    confidence = float(line[index:])
    total += confidence

average = total / lines
print("Average spam confidence:", average)
