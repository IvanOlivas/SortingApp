
def sort_list():
    sortIt = list();                #create list to store strings
    doc = open('Sort Me.txt');      #access the file with the string

    #read through file and store each string
    for name in doc:
        sortIt.append(name);
    doc.close();           # close file since all strings were stored in our list

    #sortIt.sort()  #sort by the length of the string
   
    sortIt.sort(key=lambda s: (len(s), s))

    return sortIt;
