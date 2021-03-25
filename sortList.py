
def sort_list():
    sortIt = list();                #create list to store strings
    doc = open("Sort Me.txt", "r");      #access the file with the string

    #read through file and store each string
    for name in doc:
        sortIt.append(name);
    doc.close();           # close file since all strings were stored in our list

    #ask user if they want to reverse the sort
    val = input("Would you like to reverse the sort? (enter 1 for yes, 2 for no):")
    
    if val == 1:   # final result in reverse
        sortIt.sort(reverse=True)
        sortIt.sort(key=len, reverse=True)
        
    elif val == 2:  #not reversed
        sortIt.sort()
        sortIt.sort(key=len)

    return sortIt;
