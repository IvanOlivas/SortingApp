def readFile():
	
	studentList = list()
	#read the file 
	readFromFile = open("SortMe.txt", "r")
	
	#append each name to studentList
	for eachName in readFromFile:
		studentList.append(eachName)
		#print(eachName)
		
	readFromFile.close()
	
	sortListNames(studentList)	
	
	
def sortListNames(studentList):
	studentList.sort()
	studentList.sort(key=len)
	
	###########################
	#for testing purposes only 
	printList(studentList)
	###########################
	
	return studentList
	
#############################	
def printList(thisList):
	for item in thisList:
		print(item)
#############################	
	
if __name__ == '__main__':
	readFile()
	
	
	
