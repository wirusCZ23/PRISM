import sys

file = open(sys.argv[1])
fileLines = file.readlines()
file.close()

newFile = open(sys.argv[1]+"_adj", "w+")
k = int(sys.argv[3])
update = int(sys.argv[2])

for i in range(len(fileLines)):
		if i > k:
				lineParts = fileLines[i].strip().split("\t")
				newTimeStamp = int(lineParts[0])+update
				newLine = str(newTimeStamp) + "\t" + "\t".join(lineParts[1:len(lineParts)]) + "\n"
				newFile.write(newLine)
		else:
				newFile.write(fileLines[i])
