def word_count(s):
    # Your code here
    #dict to store words and number of times it appears
    words = {}
    #set all letters to lower case
    s = s.lower()
    #remove unwanted characters from string
    letters = set("abcdefghijklmnopqrstuvwxyz' ")
    s = ''.join(filter(letters.__contains__, s))
    #split the string into a list of words.
    new_list = s.split(' ')
    #loop through list of words
    for i in new_list:
        #if word is a key in dict
        if i in words: 
            #increse the dicts value by 1
            words[i] += 1
        else:
            #if i is not an empty string
            if i != '':
                #create a key using the word and initialize with value of 1
                words[i] = 1
    
    #return the dict
    return words
    




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))