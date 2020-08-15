import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

#create an empty dataset using a dict
dataset = {}
#split words into an array of strings
words = words.split()

#random start word helper function
def random_start():
    #pick a random word from string of words
    r = random.choice(words)
    #base case
    #if word[0] is equal to " or a uppercase letter
    if r[0] == '"' or r[0] == r[0].upper():
        #return word
        return r
    else:
        return random_start()

# TODO: analyze which words can follow other words
# Your code here

#loop through the array
for i in range(0,len(words)):
    #if word is not in dict
    if words[i] not in dataset:
        #add the next word as a list to the dict using word as key
        if i != len(words) - 1:
            dataset[words[i]] = [words[i + 1]]
        else:
            dataset[words[i]] = []
    else:
        #append next word into list that is value of key of word
        dataset[words[i]].append(words[i + 1]) 

# TODO: construct 5 random sentences
# Your code here

#random sentance function
def random_sentence():

    #grab a random start word
    rand_word = random_start()
    blacklist = ['.','?','!']
    end_word = False
    

    #use a while loop using random word last digit equaling puctuation or punctuation followed by "
    while end_word is not True:
        if rand_word[len(rand_word) - 1] == '"':
            if rand_word[len(rand_word) -2] in blacklist:
                end_word = True
            elif rand_word[len(rand_word) -1] in blacklist:
                end_word = True
        
        #print random word
        print(rand_word, end=" ")
        #search the dict using random word and grab the list stored in its value
        word_list = dataset[rand_word]
        rand_word = random.choice(word_list)
        # grab a random word from list and set it to random word
    
for i in range(0, 6):
    random_sentence()
    print('\n')