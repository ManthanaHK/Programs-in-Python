spam = []
print('Enter number of elements:',end= ' ')
num = input()
for i in range(int(num)):
    print('Enter the {} element:'.format(i))
    element = input()
    spam.append(element)
print(spam)
