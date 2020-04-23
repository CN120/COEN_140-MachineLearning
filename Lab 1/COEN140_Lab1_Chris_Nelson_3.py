
def charCounter(string):
    max_val = 0
    max_letter = string[0]
    charDict = dict.fromkeys(string,0)
    for letter in string:
        x = charDict[letter] = charDict[letter]+1
        if x>max_val:
            max_val = x
            max_letter = letter          
    if max_letter == ' ':
        max_letter = "'space'"
    return max_letter


print("Most frequent character:",charCounter("bees like honey"))
#will only return one character even if others share same frequency
