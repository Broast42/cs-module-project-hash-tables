# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# text = open("ciphertext.txt")
# text = text.read()

# whitelist = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# new_word = ''.join(filter(whitelist.__contains__, text))
# f = [c for c in new_word]
#dict to keep acctual frequency usefreq as key and letter as value
letter_freq = {
    11.53: "E",
    9.75: "T",
    8.46: "A",
    8.08: "O",
    7.71: "H",
    6.73: "N",
    6.29: "R",
    5.84: "I",
    5.56: "S",
    4.74: "D",
    3.92: "L",
    3.08: "W",
    2.59: "U",
    2.48: "G",
    2.42: "F",
    2.19: "B",
    2.18: "M",
    2.02: "Y",
    1.58: "C",
    1.08: "P",
    0.84: "K",
    0.59: "V",
    0.17: "Q",
    0.07: "J",
    0.06: "X",
    0.03: "Z",
} 

def decrypt(text):
    #import the text
    crypted = open(text)
    crypted = crypted.read()
    #list of letter from A - Z to loop through letters
    atoz = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #clean up text leaving only letters
    whitelist = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cleaned_crypted = ''.join(filter(whitelist.__contains__, crypted))
    #split the text at every letter
    crypted_letters = [c for c in cleaned_crypted]
    #dict to pass letters into as keys with letter count as values
    letter_count = {}
    #deciphered dict
    deciphered = {}
    #decipherd string
    deciphered_text = ''

    #loop through letters
    for i in crypted_letters:   
        #if letter is not in dict
        if i not in letter_count:
            #add letter to dict as key with value of 1
            letter_count[i] = 1     
        else:                
            #increment value at key of letter
            letter_count[i] += 1
    
    #change dicts values to percentage
    #for letter in list of letters
    for i in atoz:
        #dicts at letter is equal to value devided by len of all letters
        letter_count[i] = round((letter_count[i]/len(cleaned_crypted)) * 100, 2)

    #order letter count
    #letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    #loop throuh letters dict
    for i in atoz:
        #if letter is not in deciphered dict
        if i not in deciphered:
            #deciphered[letter] = feq[dict[letter]]
            deciphered[i] = letter_freq[letter_count[i]]
    


    #loop through text
    for i in crypted:
        #if i in decipered dict
        if i in deciphered: 
            #deciphered string += deciphered[i]
            deciphered_text += deciphered[i]
        else:
            #deciphered string += i
            deciphered_text += i

    #return deciphered string
    return deciphered_text

print(decrypt("ciphertext.txt"))