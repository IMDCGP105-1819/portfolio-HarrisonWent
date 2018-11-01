Annual_Salary = float(input("Please enter your annual salary: "))
Original_Salary = Annual_Salary
Total_House_Cost = 1000000
semi_annual_raise = 0.07
Portion_Deposit = Total_House_Cost*0.8

r = 0.04
down_Payment = Total_House_Cost*0.25

Portion_Saved = 1
Steps_In_BiSection = 0
Months_To_Save = 0
Saved = False

while Saved == False:
    Current_Savings = 0
    Annual_Salary = Original_Salary
    Months_To_Save = 0
    while Months_To_Save < 36:
        Current_Savings += ((Annual_Salary / 12) * Portion_Saved)
        Current_Savings += Current_Savings * (r / 12)
        Months_To_Save += 1
        if 6 % Months_To_Save == 0:
            Annual_Salary = Annual_Salary + ((Annual_Salary / 2) * semi_annual_raise)
    #print(Current_Savings)
    if Portion_Saved==1 + Current_Savings<down_Payment:
        print("It is not possible to save for this house!")
        break
    if Current_Savings > down_Payment+100:
        #("Saved too much at ", Portion_Saved)
        Steps_In_BiSection += 1
        Portion_Saved = Portion_Saved / 2
    elif Current_Savings < down_Payment-100:
        #print("Saved too little at ", Portion_Saved)
        Steps_In_BiSection += 1
        Portion_Saved = Portion_Saved + (Portion_Saved / 2)
    else:
        print("Best savings rate to pay for £1 million house down payment of 25%: ", Portion_Saved)
        print("Steps in bisection search: ", Steps_In_BiSection)
        Saved=True

