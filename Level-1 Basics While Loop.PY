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

total = 0  # this will hold the sum
num = int(input("Enter a number: "))  # first input
while num != 0:  # as long as it's NOT 0
    total += num  # add number to total
    num = int(input("Enter a number: "))  # ask again
print("Total sum:", total)

