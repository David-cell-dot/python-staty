my_dic={
    "name":"David wafula",
    "age":23,
    "gender":"male",
    "city":"nairobi"
    
}
print(my_dic)
print(type(my_dic))

#accessing values using keys
print(my_dic["age"])
print(my_dic["city"])

#update and add properties
my_dic["age"]=60
print(my_dic)

#add properties
my_dic["OCCUPATION"]="TEACHER"
print(my_dic)

#dictionary methods
#pop
my_dic.pop("gender")
print(my_dic)

#pop item-removes last added
my_dic.popitem()
print(my_dic)
