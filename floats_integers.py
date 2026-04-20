#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 

#temp = 56.8926 to 57
temp = 56.8926

print(round(temp))

#temp = 56.8926 to 56.89
temp = 56.8926
print(round(temp,2))

#temp = 56.8926 to 56.893 
print(round(temp,3))

#temp=56.8926 to 8.926 
temp=str(temp)
temp=temp[3:7]
temp=temp[0] + " ." +temp[1:4]
print(temp)
