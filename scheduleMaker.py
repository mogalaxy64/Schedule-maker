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
	print(s)


main()
