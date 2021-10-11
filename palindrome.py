def palindrome(word_num):
    word = list(word_num)
    reverse_word = []
    for i in range(len(word)):
        reverse_word.append(word[-(i+1)])
    if reverse_word == word:
        print('Entered input, '+str(word_num)+' is Palindrome.')
    else:
        print('Entered input, '+str(word_num)+' is not a Palindrome.')
      
print('Enter a text or number to findout whether it is palindrome or not:')
word_num = input()
palindrome(word_num)   
