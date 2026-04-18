trainees=["John",[2,["James","Mary"]]]
#display 2 from the list

print(trainees[1][0])

#output james from the list
print(trainees[1][1][0])

# Using a method add 56 at the end of the list
trainees=["John",[2,["James","Mary"]]]

trainees.append(56)
print(trainees)

#using a method add the name mike between james and mary
trainees[1][1].insert(1,"Mike")
print(trainees)

#change the value of 2 to 8
trainees[1][0]=8
print(trainees)

#remove john and mary from the list
trainees=['John', [8, ['James', 'Mike', 'Mary']], [56]]
#remove john#[[8, ['James', 'Mike', 'Mary']], [56]]
trainees.pop(0)

#remove mary
trainees[0][1].pop()
print(trainees)

#lenth
print(len(trainees))
