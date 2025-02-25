#python salary calculator ver 2, calculates overtime as well

#version Number
print("SalCal ver 1.2")

#constant
end = False

#continues to run code until end becomes true(q is input)
while end == False:
    name = input("Enter your name, or type 'Q' to end \n")
    #end program
    if name == "Q".casefold():
        print("\nThank you for using SalCal ver 1.2.\n")
        break
    #continues program if name is entered
    else:
        rate = float(input("Enter your rate of pay: "))
        r = rate

        hourPerDay = float(input("Enter your hours worked in a day: "))
        hpd = hourPerDay

        hourPerWeek = float(input("Enter your hours worked in a week: "))
        hpw = hourPerWeek

        #Line redundant, should be removed
        '''dayPerWeek = float(input("Enter number of worked days in a week: "))
        dpw = dayPerWeek'''

        #formulas
        yearlySalary = r * hpw * 52
        monthlySalary = yearlySalary / 12
        weeklySalary = r * hpw
        dailySalary = r * hpd

        #calculate overtime rate and pay
        if hpw > 40:
            overtimeHour = hpw - 40
            overtimeRate = rate * 1.5
            overtimePay = overtimeHour * overtimeRate
            otPrompt = input("It appears you worked some overtime. Do you want your overtime information? Y or N: ")
            if otPrompt != "Y".casefold():
                print("\nOvertime information will not be displayed.\n")
            else:
                print("\n******Overtime Information******\n")
                print(f"Your overtime rate of pay is ${overtimeRate:.2f}.\n")
                print(f"Your overtime pay is ${overtimePay:.2f}.")
                print("\n******Overtime Information******\n")
   
    breakdown = input("Do you want a full breakdown of your income? Y or N: ")
    #show total income (year, month, week, day) 
    if breakdown == "Y".casefold():
        print("\n******Income Information******\n")
        print(f"Hello, {name.title()},")
        print(f"You make ${yearlySalary:.2f} in a year.\n")
        print(f"You make ${monthlySalary:.2f} in a month.\n")
        print(f"You make ${weeklySalary:.2f} in a week.\n")
        print(f"You make ${dailySalary:.2f} in a day.")
        print("\n******Income Information******\n")

    #only show yearly income    
    else:
        print("\n******Concise Version******\n")
        print(f"Hello, {name.title()},")
        print(f"You make ${yearlySalary:.2f} in a year.")
        print("\n******Concise Version******\n")
        
#OT is factored into overall yearly income, need to make separate
#maybe consider removing OT all together