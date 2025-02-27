# tip_calculator.py
# A simple tip calculator to compute tip amount and total bill

def tip_calculator():

    #Welcome
    print("Welcome to the Tip Calculator")

    try:
        #Ask for Input
        bill_amount = float(input("Please enter your bill amount: $"))
        tip_percentage = float(input("Please enter the percentage you would like to tip (e.g. 10, 15, 20, 25)" ))

        #Validate
        if bill_amount < 0:
            print("Invalid Input. Must be a Positive number")
            return

        if tip_percentage < 0:
            print("Invalid Input. Must be a Positive number")
            return
        
        #Calculator 
        tip_amount = bill_amount * (tip_percentage / 100)
        total_bill = bill_amount + tip_amount

        #Summarize the results 
        print(f"\n Bill Amount: ${bill_amount:.2f}")
        print(f"\n Tip Amount: ${tip_amount:.2f}")
        print(f"\n Total Bill(With Tip): ${total_bill:.2f}")

        #Thanks
        print("Thank you for using the Tip Calculator")

    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ =="__main__":
    tip_calculator()
