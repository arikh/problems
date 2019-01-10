def is_palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[-(i+1)]:
            return False
    return True

print(is_palindrome(''))
#>>> True
print(is_palindrome('abab'))
#>>> False
print(is_palindrome('abba'))
#>>> True
