filename = input("Enter name of the txt file you wish to read (must be in active directory): ")

with open(filename+".txt",'r') as f:
    lines = f.readlines()
length = len(lines[0])
longline = []
longline.append(lines[0].strip())
curline = lines[0].strip()
count = 0
while True:
    count = 0
    for line in lines:
        if len(line.strip()) > len(curline):
            curline = line.strip()
            longline.clear()
            longline.append(line.strip())
            break
        elif len(line.strip()) == len(curline) and curline != line.strip():
            longline.append(line.strip())
        count += 1
    if count == len(lines):
        break
print("The longest line is/are: ")
for line in longline:
    print(line)