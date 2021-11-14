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

//*******Another Way***********//

reverse_list_word = []
print("Enter the word:",end =' ')
word = input()
list_word = list(word)
for i in range(1,int(len(list_word) + 1)):
    reverse_list_word.append(list_word[-i])
if list_word == reverse_list_word:
    print("Entered word {}, is Palindrome".format(word))
else:
    print("Entered word {}, is not palindrome".format(word))
