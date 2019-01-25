# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
def shift_n_letters(letter, n):
    alphabets = list(map(chr, range(97, 123)))
    if alphabets.index(letter) + n < 26:
        return alphabets[alphabets.index(letter) + n]
    else:
        return alphabets[alphabets.index(letter) + n - 26]

def rotate(passage, n):
    # Your code here
    passage_list = passage.split()
    new_passage = []
    for word in passage_list:
        new_word = ""
        for letter in word:
            new_word += shift_n_letters(letter, n)
        new_passage.append(new_word)
    return " ".join(new_passage)


print(rotate ('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu',13))
#>>> 'sarah'
print(rotate('dave',5))
#>>>'ifaj'
print(rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???
