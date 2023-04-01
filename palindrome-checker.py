def palindrome_checker(word):
    len_word = len(word)
    len_word = len_word - 1 # Adjustment for `while loop` below

    list_word_new = []

    while len_word >= 0:
        list_word_new.append(word[len_word])
        len_word -= 1

    word_new = ''.join(list_word_new)

    if word_new == word:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

if __name__ == '__main__':
    word = input("Type any word: ")
    palindrome_checker(word)