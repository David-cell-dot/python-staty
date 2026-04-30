# fruits=["mango","pawpaw","bananas"]
# for i in fruits:
#     print(i)

#     cars=["toyota","harrier","isuzu"]
#     schools=["gsc","ksm","lkj","popo"]
#     for x in cars:
#         for y in schools:
#             print({x},{y})





# list1=list(range(1,100,5))
# for x in list1:
#   print(list1)

# #diplay even number btn 10 and 100
# numbers=list(range(10,101))
# even_numbers=[]

# for i in numbers:
#    if i%2==0:
#       even_numbers.append(i)

      
# print(even_numbers)



# # diplay number divisible by 3  and 7 fro 1 to 100
# numbers=list(range(1,101))
# nums=[]
# for x in numbers:
#    if x%3==0 and x%7==0:
#       nums.append(i)

# print(nums)

# diplay number divisible 7 and 9 from 1 to 100

# numbers=list(range(1,101))
# numb=[]
# for i in numbers:
#    if i%7==0 and i%9==0:
#       numb.append(i)

# print(numb)


#pin
tries=3
attempts=list(range(1,4))
for i in attempts:
    pin=input("enter pin:")
    correct_pin="1234"
    if pin==correct_pin:
        print("welcome")
        break
    else:
        remaining_tries=tries-i
        if remaining_tries>0:
            print(f"incorrect pin try again  { remaining_tries} tries remaining")
        else:
            print("account blocked")
          
  