Total_House_Cost = float(input("Please enter the total cost of the house: "))
Annual_Salary = float(input("Please enter your annual salary: "))
Portion_Saved = float(input("Please enter your percentage of your salary to be saved : "))

Current_Savings = 0
Portion_Deposit = Total_House_Cost*0.8
r= 0.04
Months_To_Save = 0

while Current_Savings<Total_House_Cost:
    Current_Savings+=(Annual_Salary/12*(1-Portion_Saved))
    Current_Savings * r / 12
    Months_To_Save+=1


