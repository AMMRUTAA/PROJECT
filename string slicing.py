#fiboacci series
#a = 0
#b = 1
#n = int(input("Enter a number here: "))

#if n == 1:
 #   print(1)
#else:
 #   print(a)
  #  print(b)
   # for i in range(2, n):
    #    c = a + b
     #   a = b
      #  b = c
       # print(c)
# if number is prime or not
#num=int (input("enter a number here:"))
#if num<=1:
 #   print ("it is not a prime number ")
#else :
 #   for i in range (2,num):
  #      if num% i== 0:
   #         print ("number is not a prime number")
    #    else:
#
 #           print ("it is a prime number")

# check for palindrome
num = int(input("Enter a number here: "))
temp = num
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10


if rev == temp:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    #area calculator