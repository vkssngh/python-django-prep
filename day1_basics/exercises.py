def reverse_string(s):
    """Return the reverse of the input string s."""
    return s[::-1]

#count vowels
def count_vowels(s):
    
    vowel="aeiouAEIOU"
    return sum(1 for char in s if char in vowel)

#quize solution 
def is_palindrome(s):
    """Check if the input string s is a palindrome."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    reversed_cleaned = ''.join(reversed(cleaned))
    return cleaned == reversed_cleaned

print(is_palindrome("book"))  # Output: False
print(is_palindrome("madam"))  # Output: True

def reverse_string(s):
    """Return the reverse of the input string s."""
    output = ''
    for char in s:
        output = char + output
    return output
    
print(reverse_string("hello"))  # Output: "olleh"
