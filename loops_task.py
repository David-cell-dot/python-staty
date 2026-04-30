# # . Write a program that displays a numbers 1 to 50 inside a list.
numbers=list(range(1,51))
number=[]
for x in numbers:
  number.append(x)
  
print(number)



 #2. From 1 above display the ones divisible by 7 or 5 inside a list.
numbers=list(range(1,51))
number=[]
for x in numbers:
 if x%5==0 and x %7==0:
  number.append(x)

print(number)




# 3. Find sum and average of values in the range between 10 to 40.

value=[]
let=list(range(10,41))
print(let)
total=0
count=0

for i in let:
    total+=i
    count+=i

print(total)
print(total)
average=total/count
print(total)



# 4. Put in a list the first 10 odd numbers between 10 to 50.
number=list(range(10,51))
count=0
nums=[]
for n in number:
   if n%2==1:
    nums.append(n)
   if len(nums)==10:
    break

print(nums)



   
# 5. write a program that takes a number as input and prints its
# # multiplication table up to 10 using a for loop.

res=int(input('enter a number:'))
for i in range(1,11):
    print(res,"x",i, '=' "")



       


# 6. write a program that counts and prints the number of even numbers
# between 1 and 50 using a for loop
tx=list(range(1,51))
num=[]
for t in tx:
  if t%2==0:
   num.append(t)
print(num)
#7. ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# # Display the total quantity of the 3 above.
ls1 = [ ("Jay", "20"), ("Mo", "30"), ("Mya", "32") ]
total_quantity=0

for i in ls1:
    quantity=int(i[1])
    total_quantity=total_quantity + quantity

print(total_quantity)



