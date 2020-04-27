# Input Parameter: a string x
# Return Value: True if x is a palindrome, False otherwise
def palindrome(x):
    # remove punctuation -> our test cases don't have punctuation, but is still a good practice
    cleaned_string = ''
    for i in range(len(x)):
        if(i != '?' and i != ',' and i !='!' and i != '.' and i !=':' and i != ';'):
            cleaned_string += x[i]
    # reverse string w/ for loop
    reverse_string = ''
    for i in range((len(x)-1), -1, -1):
        reverse_string += x[i]
    # compare revered string to original -> true/false
    return (reverse_string == cleaned_string)


# Tests!
print(palindrome("aba"))
print(palindrome("a"))
print(palindrome("abba"))
print(palindrome("amanaplanacanalpanama"))
print(palindrome("abca"))
print(palindrome("ac"))
print(palindrome("adabbba"))
print(palindrome("amandaplanacanalpanama"))

# Expected Output
'''
True
True
True
True
False
False
False
False
'''