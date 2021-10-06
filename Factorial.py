print('Enter the number for which the factorial must be found: ')
number = input()
spam = 0
total = 1
while int(spam) <= int(int(number) - 1):
    total = int(total) * int(int(number) - int(spam))
    spam = spam + 1
print('Factorial of the number '+str(int(number))+' is '+str(int(total)))
          
