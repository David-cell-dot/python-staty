#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
#quiz 1
name=" JOHn  .  "
name=name.replace("."," ")
name=name.strip()
name=name.lower()
print(name)

#quiz 2,slice  to display  “Breed is German”
sentence_one ="The Dog Breed is German Shepherd"
print(sentence_one[8:])

#SLICE ,show only "clinton forces"
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.”
text="The lazy dog; ran so fast; it hit the wall."
text=text.split(";")
print(text)
print(len(text))

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r='["E","W","C"]'
r=r.replace("' "," ")
print(r)