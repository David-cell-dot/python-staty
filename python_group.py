# #GROUP 11
# #Q1
# #A school administration system is tracking unpaid fees. Build a program that checks student payment status and flags those with outstanding balances.

# student_payment=int(input("enter the amount paid:"))
# total_payment_fees=int(input("enter total_payment_fees:"))
# if student_payment>=total_payment_fees:
#  print("cleared fees")
# else:
#  print("outstanding balance")
# #Q2
# #A traffic system is monitoring speeding vehicles. Create a program that evaluates speed readings and determines whether a driver should be fined.

# #speed=distance/time
# speed=int(input("enter the speed:"))
# high_speed_limit1=120
# low_speed_limit=40
# if speed>=40 and speed>=120:
#  print('high speed, driver should be fined')
# elif speed>=40 and speed<=120:
#  print("normal speed")
# else:
#  print("very low speed")

# #Q3
# #A website login system is being improved. Create a program that checks login credentials and determines
# #  whether a user should be granted full access, limited access, or denied entry.

# password=input("enter your password:")
# email=input("enter your email:")
# correct_password="admin234"
# correct_email="admin@gmail.com"

# if password!=correct_password and email!=correct_email:
#  print("denied entry")
# elif password==correct_password and email!=correct_email:
#  print("limited access")
# else:
#  print("granted full access")


# #Q1
# #A bank wants to improve its ATM service.
# #  Create a program that stores a customer’s name and account balance,
# #  then allows them to request a withdrawal.
# #  If the amount requested is greater than the available balance, 
# # the transaction should fail. If successful, 
# # deduct the amount together with a transaction fee of KES 30 and display the new balance.


# account_balance=int(input("enter the account_balance:"))
# account_balance=10000
# transaction=30
# customer_name=input("enter your name:")
# request_amount=int(input("enter the request amount:"))


# if request_amount >=account_balance:
#  print( f" Hello {customer_name}Transactional failed insuffient funds to withdraw{request_amount} your balance{account_balance}")
# else: 
#  account_balance= account_balance-(request_amount + transaction) 
#  print( f" Hello{customer_name}{request_amount}withdrawal the amount successfully,New balance{account_balance}" )






# #Q2
# #A trainer entered marks for five subjects and needs help analyzing student performance.
# #  Create a program that stores the marks in a list, 
# # calculates the average, awards grade A for averages of 70 and above, 
# # grade B for averages of 50 to 69, and grade C for anything below 50.
# #  If any subject score is below 40, 
# # display a message showing the student must retake that subject.
# student_marks=int(input("enter the student_marks:"))
# marks= [ 20,30,40,50,60]
# average=sum(marks)/len(marks)
# res=""
# if student_marks>=70 and student_marks<=100:
#  res="grade A"
# elif student_marks>=50 and student_marks<=69:
#   res="grade B"
# elif student_marks>=40 and student_marks<=49:
#  res="grade C"
# else:
#  res =" the student must retake"

# print(res)
# #Q3
# #A supermarket manager needs help checking stock levels.
# #  Create a program that stores product names and quantities in a dictionary, 
# # identifies items that are completely out of stock, 
# # and also shows products with quantities below five units that need urgent restocking.

# stocks={
#  'omo':100,
#  'sugar':45,
#  'flour':67,
#  'tea leaves':80,
#  'milk':8,
#  'bread':3,
#  'salt':0
 
# }
# #stock that are completely out

# #use if
# if stocks[-1]<=0:
#  resus="stocks['salt']"
# elif stocks>0 and stocks<=5:
#  resus="Need urgent restocking"
# else:
#  resus="enough stocking"


# print(resus)




# #Q4
# #A company wants to secure employee accounts.
# #  Create a login system that stores a username and password, 
# # allows only three attempts, locks the account after three failed attempts,
# #  and welcomes the user when the correct credentials are entered
# user_name=input("enter the username:")
# password=input("enter password:")
# company_name=input("enter comapny name:")
# correct_password="Secret@123"
# correct_user_name="Danish"
# min_attempts=0
# max_attempts=3


# if max_attempts>3 and user_name!=correct_user_name and password!=correct_password:
#  message=f"Hello {user_name} your account{password} has been locked the account ,because{max_attempts} is more than required"
# elif min_attempts>0 and max_attempts<=3:
#  message=f" Hello{user_name} you have one remaining attempts,enter the correct{password}"
# else:
#  message=f"Hello{user_name}welcomes to {company_name},we offer diverse services"

#  print(message)


 #GROUP 2
#Q1
#An electricity company charges customers based on usage.
#  Create a billing system where the first 100 units are charged at KES 15 each,
#  while any additional units are charged at KES 20 each. If the final bill exceeds KES 5000,
#  add 5% tax before displaying the total.

bill_units=int(input("enter the bill_units:"))
extra_unit=int(input("enter extra unit"))
bill_costs=int(input("enter the extra bill cost:"))



if bill_units<100:
 per_unit_charges=100/15*bill_units
 pen="you have been charged { per_unit_charges} for the service"
elif bill_units>100:
 extra_unit="bill_units-extra_unit" +  "per_unit_charges"
 pen="extra_unit"

# else:
#  bill_costs>bill_costs,
# bill_costs="5000" + "{5000*0.05}"


# pen="bill_costs "


print(pen)



#Q2
#A hospital needs a smart queue system. 
# Create a program that stores patient name and age.
#  Patients above 60 years and children below 5 years should receive priority service, 
# while all others join the normal queue.

patient_name=input("enter the patient name:")
patient_age=int(input("enter the patient age:{age in years}"))

if patient_age<=60 and patient_age>=5:
 print("join normal queue ")
else:
 print("receive priority service")


#Q3
#An online store wants an automated checkout system. 
# Create a program that stores purchased items in a list and calculates the total cost.
#  If the amount is above KES 3000, apply a 10% discount. 
#  the total is below KES 1000, add a delivery fee.
#items=[["MAIZE","KSH.400"],["SUGAR","KSH700"],["UNGA","KSH.900"],["SOAP","KSH.1500"]]
#print(items[0][1][1][1][2][1][2][1])

#
#Q4
#A website wants users to create stronger passwords.
#  Build a password checker that verifies password length, 
# checks whether it contains numbers and special characters,
#  then classifies it as Weak, Medium, or Strong.


password=input("enter password")
characters_0="weak"
characters_1="medium"
characters_digits="strong"
weak="length<=6 and no special characters/digits"
medium="length 6-10, '@' "
strong="length>=10 '@',12"
if len(password)<=6 and characters_0:
 print("weak")
elif len(password)>=6 and len(password)<=10 and characters_1:
 print("medium")
else:
 print("strong")


 #GROUP 3
#Q1
#A driver is preparing for a road trip.
#  Create a program that stores the amount of fuel available and the distance to travel. 
# If one litre covers 12 km,
#  determine whether the fuel is enough for the journey or 
# if the driver should refill first.


amount_of_fuel=int(input("enter the amount of fuel:{in litres}"))
distance=int(input("enter the distance:{ km}"))
amount_of_fuel=1
distance=12
if distance<=12 and amount_of_fuel<=1:
 print("fuel is enough ")
else:
 print("driver should refil first")

#Q2
#A company wants to automate payroll.
# Build a program that stores an employee’s basic salary,
#  adds allowances, then deducts tax. 
# Employees earning above KES 80,000 should pay 30% tax while the rest pay 20%.
#  Display the final net salary.

basic_salary=int(input("enter the basic salary:"))
allowances=int(input("enter the allowances:"))
Deduction_tax=int(input("enter deductions Tax:{gross_salary*0.3}"))

gross_salary=80000

net_salary=int(input("gross_salary -Deduction_tax"))
if gross_salary>=8000 and Deduction_tax<=0.3:
 print( " good net salary")
else:
 print( "normal net salary")



#Q3
#A weather station records daily temperatures.
#  Create a system that warns people when temperatures are above 35 degrees,
#  warns of cold weather when below 15 degrees,
#  and shows normal conditions otherwise.

temp=float(input("enter temp:"))
if temp>35:
 print("too hot")
elif temp>=15 and temp<=35:
 print("normal conditions")
else:
 print("cold temperature")
#Q4
#A courier company wants package tracking.
#  Create a system that checks whether a package is delayed, delivered, or still in transit. 
# Delayed packages should notify customers, delivered packages should display a thank-you message, 
# and packages in transit should show estimated arrival.

package_tracking=input("enter the package_track:")
delayed_package="notify customers"
delivered_package="thank you"
still_in_transit_package="will arrive at[time_in _hrs()]"
if delayed_package:
 print('notify customers')
elif still_in_transit_package:
 print("will arrive at {at--am/pm}")
else:
 print("thank you")


 #GROUP 4
#Q1
#A school wants to stop students with pending balances from sitting exams.
#  Create a program that checks a student’s fee balance.
#  If the balance is greater than zero, deny access to the exam card.
#  Otherwise allow printing.

student_fee_balance=int(input("enter student fee balance:"))
student_name=input("enter student name:")
if student_fee_balance>0:
 res=f"Hi{student_name}deny access to exam card , your balance is{account_balance}"
else:
 res=f"Hi{student_name} allow printing exam card"

print(res)
#Q2
#A parking company wants to automate entry control.
#  Build a program that stores the total parking spaces and occupied spaces, 
# then calculates available slots. If the lot is full, deny new entry.

total_packing_space=int(input("enter the total packing  spaces:"))
occupied_space=int(input("enter the slots for available space:"))
available_spaces=total_packing_space-occupied_space


if available_spaces>0:
 available_spaces-=1
 value=f"entry allowed {available_spaces} available spaces"
else:
  value=f"entry denied{available_spaces} available spaces"

print(value)


#Q3
#A mobile network provider wants to warn customers when internet bundles are low.
#  Build a program that checks remaining data in MB. If below 100MB, warn the user. 
# If zero, block browsing.
data_bundles=int(input("enter  bundles in MB:"))

data=float("enter remaining data")
if data==0:
 res="stop browsing"


 


#Q4



#A retail shop wants to identify wholesale customers.
#  Create a system that checks how many items a customer has bought.
#  If items are more than five, reward points should be given.


items=int(input("enter number of items purchased:"))
wholesale_tresh=5

if items>5:
 reward_points=items/wholesale_tresh
 val=f"You have bought{items} items you have earned{reward_points}reward points"
else:
 rem=wholesale_tresh-items
 val=f"you have bought{items}items add{rem}more to earn points"
 
 





#GROUP 5
#Q1
#A bank is reviewing loan applications.
#  Create a program that checks salary and age.
#  Applicants below 21 years should be rejected,
#  while those above 21 with salaries above KES 50,000 should be approved.

salary=float(input("enter your salary:"))
age=int(input("enter your age: {age in years}"))
if age>21 and salary>50000:
 print("approve loan")
elif age>21 and salary<50000:
 print("review the loan")
else:
 print("decline loan approval")
#Q2
#A smartphone company wants a battery safety alert.
#  Build a program that checks battery percentage. 
# If below 20%, warn the user to charge. If below 5%, activate emergency mode.

battery_percentage=int(input("enter the battery percentage:"))
if battery_percentage<5:
 print("activate emergency mode")
elif battery_percentage<20:
 print("charge the battery")
else:
 print("enough power battery")
#Q3
#A school wants to monitor attendance.
#  Create a system that stores attended classes and total classes, 
# calculates attendance percentage, and warns students whose attendance is below 75%.
class_attendance=int(input("enter the percentage of class attended:"))
if class_attendance>90 and class_attendance<=100:
 print("excellent student")
elif class_attendance>=75 and class_attendance<=90:
 print("Good,need to improvement")
else:
 print("to pull up their socks")
#Q4
#A courier company wants to improve communication.
#  Build a system that compares expected delivery date with the current day 
# and alerts customers if the package is delayed.

expected_delivery_date=input("enter date:")
current_day=input("enter delivery date:{year/month/day} ")

if current_day<= expected_delivery_date:
 print("normal delivery day ")
else:
 print("alert customers")





#GROUP 6
#Q1
#Q3
#An online course platform wants to issue certificates automatically.
#  Create a system that compares completed lessons with total lessons
#  and awards a certificate once all lessons are complete.

completed_lesson=int(input("enter lesson done:"))
total_lesson=int(input("enter total lessons:"))

if completed_lesson<total_lesson:
 print("No Award of certificates")
else:
 print("Award the Certificate")
#Q4
#A cybersecurity company wants suspicious logins detected.
#  Build a program that stores a normal login country and compares it with the current login country.
#  If different, request extra verification.

normal_login_country=input("enter normal login:")
current_login_country=input("enter current login:")
current_login_country="admin1234"
normal_login_country="Secret566"
if normal_login_country==current_login_country:
 print("Access granted")
else:
 print("Request extra verification")



#GROUP 7
#Q1
#A payroll company needs to calculate employee taxes using different salary bands. 
# Create a system that applies different tax rates depending on salary level and displays final pay.

net_salary=int(input("enter your salary:"))
if net_salary>=500000 and net_salary<=1000000:
 print("35% tax applied")
elif net_salary>=400000 and net_salary<=499999:
 print("30% tax applied")
elif net_salary>=300000 and net_salary<=399999:
 print("27% tax applied")
elif net_salary>=200000 and net_salary<=299999:
 print("25% tax applied")
elif net_salary>=100000 and net_salary<=199999:
 print("22% tax applied")

elif net_salary>=90000 and net_salary<=99999:
 print("20% tax applied")
elif net_salary>=80000 and net_salary<=89999:
 print("18% tax applied")
elif net_salary>=70000 and net_salary<=79999:
 print("16% tax applied")
elif net_salary>=60000 and net_salary<=69999:
 print("12% tax applied")
elif net_salary>=50000 and net_salary<=59999:
 print("10% tax applied")
else:
 print(" no taxation applied")
 
 
#Q2
#A university hostel manager wants to know whether rooms are available.
#  Create a program that checks room count and rejects new applicants when no rooms remain.
available_rooms=int(input("enter the available roooms:"))

applicants=int(input("enter the number of applicants:"))
new_applicants=int(input("enter new applicant:"))

if available_rooms>applicants:
 print("allow  entry of new applicants")
else:
 print("Reject new applicants")
#Q3
#An investor watches stock prices daily. 
# Build a program that sends alerts whenever 
# a stock price drops below a chosen buying target.
stock_price=int(input("enter the  daily stock price:"))
buying_target=int(input("enter the daily buying price:"))
selling_target=int(input("enter the daily selling price:"))

if buying_target<stock_price and buying_target>selling_target:
 print("restock the")
else:
 print("enough stock")


##A ride-hailing company wants to manage customer expectations. 
# If no drivers are available nearby, inform the customer to retry later.
customer_expectation=int(input("enter number of visitors:"))
drivers=int(input("enter number od drivers available:"))
if customer_expectation>drivers:
 print(" more customers entry")
else:
 print(" customers to try later")



# GROUP 8
#Q1
##Q2
#A cinema only allows adults into some movies.
#  Build a system that checks age and denies entry to anyone below 18 years.
age=int(input("enter the age:"))
if age>=18:
 print("Allow entry to the movies")
else:
 print('deny entry')

#Q3
#A library wants automatic fines.
#  Create a program that charges KES 20 per late day after seven allowed days.
charges=int(input("enter the cost of charges:{KSH.}"))
Allowed_days=input("enter number of days allowed")
if Allowed_days<7 and charges<20:
 print("No charges")
else:
 print("charge per late day:{ksh.20/day}")


#Q4
#A social media platform verifies popular users. 
# Build a program that grants verification once followers exceed 10,000
popular_users=int("enter number of pop users:")
if popular_users>10000:
 print(" Grant verification")
else:
 print("No grants verification")

 #GROUP 9
#Q1
#A fuel station wants to reward customers based on how much fuel they buy.
#  Create a system that checks the number of litres purchased and
#  applies a reward message only when the purchase exceeds a certain threshold.
litres_purchased=float(input("enter litres purchased:"))
litres=50
message=input("enter the reward message")
message=" award voucher of ksh 500 on  50+ litres "
if litres_purchased>=50:
 print("award voucher of ksh 500 on  50+ litres")
else:
 print("no reward message")
##Q2
#An internet provider is monitoring user experience.
#  Build a program that evaluates network speed readings
#  and classifies them into poor, good, 
# or excellent performance based on the value entered.

net_work_speeding=input("enter the network speed:")
speed=200_1000
if net_work_speeding<200:
 print("Poor")
elif net_work_speeding>=200 and net_work_speeding<=1000:
 print("GOOD")
else:
 print("Excellent")
#Q3
#A restaurant needs a simple bill splitter.
#  Create a system that takes a total bill amount and number of people,
#  then determines how much each person should pay,
#  including a check for invalid inputs.




#Q4
#A company is reviewing job applicants.
#  Create a program that checks if an applicant meets minimum requirements such 
# as experience and qualifications before shortlisting them.

applicants=input("")



#GROUP 10
#Q1
#An airline is pricing tickets differently for children and adults.
#  Build a program that determines ticket cost based on age 
# and applies a discount where applicable.
#Q2
#A warehouse is tracking stock levels.
#  Create a system that monitors inventory and alerts when stock falls below a required minimum level for restocking.
#3
#A mobile money service has daily transaction limits.
#  Build a program that checks if a transaction exceeds the allowed limit 
# and rejects or approves it accordingly.
#Q4
#A laptop seller wants to verify warranty validity. 
# Create a system that checks purchase year against the current year and determines whether warranty is still active
warranty_validity_years=3

purchase_year=int(input("enter purchase year:"))
current_year=int(input("enter current year:"))
warranty_validity_years=int(input("enter warranty years:"))


if warranty_validity_years<=3 and current_year>=purchase_year:
 print("warranty validity is active")
else:
 print("warrant is inactive")



 



#GROUP 12
#Q1
#An electricity token system is running low on units.
#  Build a program that checks remaining token balance
#  and warns users when they are close to exhaustion.
#Q2
#A library system is managing membership cards.
#  Create a program that checks whether a membership card is expired 
# and prevents borrowing if it is not valid.
#Q3
#A hospital appointment system is managing bookings.
#  Build a program that checks doctor availability 
# and either confirms an appointment or suggests an alternative date.
