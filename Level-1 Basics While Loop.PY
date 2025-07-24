count = 1

while count <= 5:
    print("Count is:", count)
    count += 1

#Count to 10:
i=1
while i<=10:
    print(i)
    i=i+1

#Print numbers from 5 down to 1 using a while loop, then print "Blast off".
i=5
while i>0:
    print(i)
    i=i-1
print("Blast off")

#Sum Until 0
Task:
Ask the user to keep entering numbers.
Keep adding them up.
Stop when they enter 0, then print the total sum:
Solution:

total = 0 
num = int(input("Enter a number: "))  
while num != 0:  
    total += num  # add number to total
    num = int(input("Enter a number: "))  
print("Total sum:", total)

#Sassy Filter Bot
name=input("Enter your username:").lower()
while name!="admin":
    print("Invalid username.")
    name=input("Enter you username:").lower()
if name=="admin":
    print("Username accepted, welcome to the chaos")


#Enter PIN:
pin = int(input('Enter your PIN: '))
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))
if pin == 1234:
  print('PIN accepted!')

#Even Number Bouncer
Ask the user for a number.
Keep asking until they give you an even number.
Then print: "Finally! Even vibes only."

num = int(input("Enter your number: "))
while num % 2 != 0:
    print("Number is not even.")
    num = int(input("Enter your number again: "))
print("Number is Even!")







