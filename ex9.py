Annual_Salary = float(input("Please enter your annual salary: "))

Total_House_Cost = 1000000
semi_annual_raise = 0.07
Current_Savings = 0
Portion_Deposit = Total_House_Cost*0.8
r= 0.04
Months_To_Save = 0
down_Payment = Total_House_Cost*0.25
Portion_Saved = 0.0

while False:
    Portion_Saved+=10
    while Current_Savings<down_Payment:
        Current_Savings += ((Annual_Salary / 12) * Portion_Saved)
        Current_Savings += Current_Savings * (r / 12)
        Months_To_Save += 1

        if 6 % Months_To_Save == 0:
            Annual_Salary = Annual_Salary + ((Annual_Salary / 2) * semi_annual_raise)

print("Best savings rate to buy £1 million house: ", Months_To_Save)

