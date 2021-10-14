def prime(num):
    remainder = []
    for i in range(2,int(int(num) - 1)):
        remainder.append(int(num) % i)
    if 0 in remainder:
        print('Entred number '+num+', is not a prime number.')
    else:
        print('Enterd number '+num+', is a prime number.')

print('Enter a number to find out whether it is prime or not : ',end='')
num = input()
prime(num)


