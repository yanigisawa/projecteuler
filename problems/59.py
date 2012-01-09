#!/usr/bin/python

import itertools

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

def getCipherText():
    text = []
    with open("../datafiles/cipher1.txt") as f:
        for line in f:
            chars = line.split(',')
            text.extend(chars)
    return text

def getDecryptedText(key, cipherText):
    keyIndex = 0
    decryptedText = []
    for c in cipherText:
        decryptedText.append(ord(key[keyIndex]) ^ int(c))
        keyIndex += 1
        if keyIndex > 2:
            keyIndex = 0

    return ''.join([chr(c) for c in decryptedText])

def tryAllPossibleKeys():
    keys = list(itertools.permutations(lowercase, 3))
    count = 15
    cipherText = getCipherText()
    d = getDecryptedText(keys[0], cipherText)
    with open("../datafiles/prob59_decryptedText.txt", 'w') as f:
        for k in keys:
            s = getDecryptedText(k, cipherText)
            s = ("[%s] - %s\r\n" % (k, s))
            if s.find('@') + s.find('+') + s.find('{') + s.find('}') == -4:
                f.write(s)
            count -= 1
            #if count == 0:
            #    break

def prob59():
# the key is 'god'; found with the above method and visually
# inspecting the resulting output file
    s = getDecryptedText('god', getCipherText())
    total = 0
    for c in s:
        total += ord(c)

    print("Answer: %s" % total)



prob59()
