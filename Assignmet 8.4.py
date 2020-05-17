fname = input("Enter file name: ")

#Opens the File
fh = open(fname)
line1=list()

for line in fh:
        
    for word in line.split():
    	if not word in line1:
    		line1.append(word)
line1.sort()
print(line1)



#############Working 8.5


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
line2 = list()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
    
    
       
    print(words[1])
    count+=1

print("There were", count, "lines in the file with From as the first word")

##################################################

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
line2 = list()
for line in fh:
    line=line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
       
  
    line2.append(words[1])
    print(words[1])
    count+=1
    

print("There were", count, "lines in the file with From as the first word")
