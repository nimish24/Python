__author__ = 'Nimish'

def Anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)


print Anagram("clint eastwood","old west action")

def Anagram2(s1,s2): #keep a count of frequency of occurance of letters
    #First time, add counts for one string
    #Second, subtract counts for second string.
    #If the count reaches 0, it's an Anagram
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

print Anagram2("clint eastwood","old west action")



