def no_dups(s):
    # Your code here
    if s == "":
        return ""
    #split the string into words
    slist = s.split(' ')
    #create new string
    new_s = ''
    #loop through list    
    for i in range(len(slist)):
        #if new string does not contain the word
        if slist[i] not in new_s:
            if i == 0:
                #join a string of the element to new string
                new_s += "".join(str(slist[i]))
            else:
                new_s += "".join(' ' + str(slist[i]))
    return new_s
   



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))