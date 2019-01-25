# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    alphabets = list(map(chr, range(97, 123)))
    if letter == "z":
        return alphabets[0]
    else:
        for position, alphabet in enumerate(alphabets):
            if alphabet == letter:
                return alphabets[position + 1]


print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a
