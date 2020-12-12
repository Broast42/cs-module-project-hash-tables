# Your code here

#remove unwanted char helper function 
def remove_char(word):
    whitelist = set("abcdefghijklmnopqrstuvwxyz' ")
    new_word = ''.join(filter(whitelist.__contains__, word))
    return new_word

#main function    
def word_histo(file):
    # open and read the file
    text = open(file)
    s = text.read()

    cache = {}
    longest = 0

    #set all char to lowercase
    s = s.lower()
    #split the string on whitespaces
    words = s.split()
    #loop through the new split array
    for i in words:
        #if the removed_char word is in cache
        word = remove_char(i)
        if word in cache:
            #add a hash to value of that key
            cache[word] += "#"
        else:
            #if word is not an empty string
            if word != '':
                # add the removed char word as index with a # that is a string
                if len(word) > longest:
                    longest = len(word)
                cache[word] = "#"
    #return the cache
    # for i in sorted(cache, key= lambda i: len(cache[i]), reverse=True):
    #     print(f'{i}  {cache[i]}')
    for i in sorted(cache, key= lambda i: (-len(cache[i]), i)):
        space = (longest - len(i)) +2
        spacing = " " * space
        print(f'{i}{spacing}{cache[i]}')

word_histo("robin.txt")
