
def sort_list():
    sortIt = list();                #create list to store strings
    doc = open("Sort_Me.txt", "r");      #access the file with the string

    #read through file and store each string
    for name in doc:
        sortIt.append(name);
    doc.close();           # close file since all strings were stored in our list
    
    sortIt.sort(reverse=True)
    sortIt.sort(key=len, reverse=True)

    return sortIt;
