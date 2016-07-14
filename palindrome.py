import re

def is_palindrome(user_sentence):
    user_sentence = re.sub('[^a-z0-9]','', user_sentence)
    if len(user_sentence) < 1:
        return False
    if user_sentence == user_sentence[::-1]:
        return True
    else:
        return False

def main():
    user_sentence = str(input("Enter a word, phrase, or sentence(s) to test whether it's palindromic: ").lower())
    if is_palindrome(user_sentence):
        print("Your input is a palindrome!")
    else:
        print("Your input is not a palindrome!")

if __name__ == '__main__':
    main()
