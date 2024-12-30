import random 


comp=random.randint(1,100)

if(comp%2==0):
    print("Hint:The number is even")

if(comp%2!=0):
    print("Hint:The number is odd")

if(comp==100):
    print("Hint:the number is a three digit number.")

if(comp<100 and comp>=10):
    print("Hint: The number is a two digit number.")
    dig_sum=sum((int(digit)) for digit in str(comp))
    print("Hint:The sum of digits is",dig_sum)

if(comp<10):
    print("Hint:The number is a single digit number.")

if(comp%3==0):
    print("Hint:The number is a multiple of 3.")

if(comp%5==0):
    print("Hint:The number is the multiple of 5.")

if(comp<50):
    print("Hint:The number is smaller than 50.")

if(comp<40):
    print("Hint:The number smaller than 40.")

if(comp<30):
    print("Hint:The number is smaller than 30")

if(comp<20):
    print("Hint:The number is smaller than 20.")

if(comp>50):
    print("The number is greater than 50.")

if(comp>90):
    print("Hint: The number is greater than 90.")

if(comp>80):
    print("Hint: The number is greater than 80")

if(comp>70):
    print("Hint:The number is greater than 70.")

if(comp>60):
    print("Hint:The number is greater than 60.")


n=int(input("Enter the number you guessed:"))

if(n==comp):
    print("You guessed it right.")
else:
    print("Try again!")



