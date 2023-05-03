# Write code for algorithm 5 below
# * Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not

def isPalindrome(word):
    
    # base case
    if len(word) < 2:
        return True 
    
    else: 
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else: 
            return False


sample_word = 'radar'
print(isPalindrome(sample_word))