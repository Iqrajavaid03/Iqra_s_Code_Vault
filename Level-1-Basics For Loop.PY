#1 printing colors
colors=["red","green","blue"]
for color in colors:
    print(color,end=" ")

#2 Print numbers from 1 to 10.
for i in range(10):
    print(i+1)

#3 Print the word “Hello World” 5 times.
word="Hello World"
for i in range(5):
    print(word)

#4 Print characters of the word "Python" one by one.
for i in "Python":
    print(i)

#5 Print all even numbers from 1 to 20.
for i in range(2, 21, 2):
    print(i)

#6 Print numbers from 10 to 1 in reverse order.
for i in range(10, 0, -1):
    print(i)

#7 Given a list of fruits, print each fruit on a new line.
fruits=["Apple","Berry","Banana","Kiwi"]
for fruit in fruits:
    print(fruit)

 #8 For Loop with Else:
for i in range (5):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")           

#9 Searching with break + else:
nums = [2, 4, 6, 8, 10]
for num in nums:
    if num == 5:
        print("Found 5!")
        break
else:
    print("5 is not in the list.")

#10 With break:
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop completed!")

#11 Prime Number Check:
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime.")
        break
else:
    print(f"{num} is prime.")

#12 Search for a vowel
vowel=["a","e","i","o","u"]
alph=input("Enter alphabet to check: ").lower()
for i in vowel:
    if alph == i:
        print("This alphabet is vowel")
        break
else:
    print("This is not vowel")

#13 Duplicate detector using for-else:
nums = input("Enter five numbers separated by space: ").split()

for num in nums:
    if nums.count(num) > 1:
        print("Ew... Duplicate found!")
        break
else:
    print("All of these are unique. You're one of a kind ")








