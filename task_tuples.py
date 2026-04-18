#quiz one
#numbers=(10,20,30,40,50)
#add 60 to the end
#replace 30 with 35


numbers=(10,20,30,40,50)
numbers=list(numbers)
numbers.append(60)
numbers[2]=35
numbers=tuple(numbers)
print(numbers)

#quiz 2
values=(15,5,30,25,10)
#arrange in ascending order
values=list(values)
values.sort()
values=tuple(values)
print(values)

#quiz3
fruits=("apple","banana","cherry","banana","mango","banana")
#count occurences of banana
#remove all occurences of banana
fruits=fruits.count("banana")
print(fruits)

#remove all occurences of banana
fruits=("apple","banana","cherry","banana","mango","banana")
fruits=list(fruits)
fruits.remove("banana")
fruits.remove("banana")
fruits.remove("banana")
fruits=tuple(fruits)
print(fruits)

#quiz 4
names=("Alice","Bob","Charlie","David")
#reverse the order of the elements using the sort method
names=list(names)
names.sort(reverse=True)
names=tuple(names)
print(names)
#quiz5
colours=("red","blue","green")
# add "yellow" at index 1
colours=list(colours)
colours.insert(1,"yellow")
colours=tuple(colours)
print(colours)
# extend with ["purple","orange"]
colours=list(colours)
colours2= ["purple","orange"]
colours.extend(colours2)
colours=tuple(colours)
print(colours)

