days_of_week=("sun" ,"mon","tue","wed","thur","fri","sat",)
print(type(days_of_week))
print(days_of_week[1])
print(days_of_week[2:4])

#DISPLAY SAT
#display mon-thur

print(days_of_week[6])
print(days_of_week[4:])

#CONVERT tuple to list
days_of_week=list(days_of_week)
print(type(days_of_week))
#modify
days_of_week="TUESDAY"
#convert back to tuple
days_of_week=tuple(days_of_week)
print(days_of_week)

#sun to sunday
#add jan to the tuple

days_of_week=("sun" ,"mon","tue","wed","thur","fri","sat",)
#convert to list
days_of_week=list(days_of_week)
print(days_of_week)#['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
#modify
days_of_week=['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
days_of_week[0]="sunday"

print(days_of_week)

#convert to tuple
days_of_week=tuple(days_of_week)
print(days_of_week)
#add jan to tuple
days_of_week=['sunday', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
days_of_week.append("jan")
days_of_week=tuple(days_of_week)
print(days_of_week)


