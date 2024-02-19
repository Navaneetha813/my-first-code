'''def evenodd(num):
    if (num % 2) == 0:
        print("is Even")
    else:
        print("is Odd")
        return num
num = int(input("Enter a number: "))
x=evenodd(num)'''

'''def posneg(num):
    if num > 0:
       print("Positive number")
    elif num == 0:
       print("Zero")
    else:
       print("Negative number")
       return num
    
num = float(input("Enter a number: "))
x=posneg(num)'''

'''def add(num1,num2):
    result=num1+num2
    return result

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
x=add(num1,num2)
print(x)'''
'''def is_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    return count == 0

def main():
    n = int(input("Enter a number: "))
    if is_prime(n):
        print("Prime")
    else:
        print("Not Prime")

if __name__ == "__main__":
    main()'''
'''
def reversefun(num):
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print('Palindrome')
    else:
        print("Not Palindrome")
num = int(input("Enter a number: "))
x=reversefun(num)
'''
'''
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
        
s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
check(s1, s2)'''
'''
def amstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum
num=int(input("enter the number:"))
x=amstrong(num)
if num == x:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")'''
'''
def smallest(a,b,c):
    smallest_num = 0
    if a < b and a < c :
        smallest_num = a
    if b < a and b < c :
        smallest_num = b
    if c < a and c < b :
        smallest_num = c
    return smallest_num
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter first number  : '))
x=smallest(a,b,c)
print(x, "is the smallest of three numbers.")'''
'''
def factfun(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
    return factorial
num = int(input("Enter a number: "))
x=factfun(num)'''

'''
def fibfun(n1,n2):
    count = 0
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1
    return (n1,n2)
n1, n2 = 0, 1
nterms = int(input("How many terms? "))
x=fibfun(n1,n2)
'''
n=int(input())
count=0
if n>1:
    for i in range(2,n):
        if(n%i==0):
            count=count+1
        if count==1:
            print("prime")
        else:
            print("no")
            


























