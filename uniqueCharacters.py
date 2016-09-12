__author__ = 'Nimish'

def unique(s):

    return len(set(s)) == len(s)

#print unique("abgjhtyj")

def unique2(s):

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

print unique2("abcdef")