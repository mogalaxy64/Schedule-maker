def lineCounter():#This finds the total amount of lines in the doc to show the num of classes
        file = open("Schedule Example.txt")
        lines = 0
        for line in file:
                line = line.strip("\n")
                lines += 1
        return lines

def main():
	classNum = lineCounter()
	f = open("Schedule Example.txt")
	s = f.readline()
	for i in range(classNum):
		s +=f.readline()
	f.close()
	#print(s)
	#Now I need to parse the string to get all the values needed for each class
	#Can either store each class info into a single array and iterate through
	#Or can create array for each data type I need to get and iterate through those for each line



main()
