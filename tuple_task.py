#create a new file tuples_task.py
#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana".
#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
#5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]

numbers = (10, 20, 30, 40, 50)
#add 60 at the end
numbers=list(numbers)
numbers.append(60)
numbers=tuple(numbers)
print(numbers)

#replace 30 with 36
numbers=list(numbers)
numbers[2]=35
Numbers=tuple(numbers)
print(numbers)

#quiz2
values = (15, 5, 30, 25, 10)
#arrange in ascending order
values=list(values)
values.sort()
values=tuple(values)
print(values)

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#count occurences of bananas
fruits=list(fruits)
fruits=fruits.count("banana")
print(fruits)

#remove bananas
fruits=list(fruits)
fruits=fruits.remove("banana")
fruits=fruits.remove("banana")
fruits=fruits.remove("banana")
print(fruits)