__author__ = 'Nimish'

def rev_word(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
        i += 1

    #return words

#print rev_word(" This is   John")


    first = 0
    last = len(words)-1
    for i in range(first,last):
        words[first], words[last] = words[last], words[first]
        first +=1
        last -=1
    return " ".join(words).rstrip(' ')

print rev_word("This is     John   kill him")

s1 = "test string "
