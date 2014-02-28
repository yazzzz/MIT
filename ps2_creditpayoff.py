#!/usr/bin/python
"""
Problem 1 6.00sc, lecture 2

annual interest rate: 18%
monthly interest rate: 18%/12 = 0.015

minimum monthly payment: 2% = .2 * 5000 = $100
interest paid = 18%/12 * 5000 = 75
principal paid = mmp - ip = 100 -75 = 25
remaining balance after m1 5000 - 25 = 4975

For each month on one year, print the minimum monthly payment, remaining balance, principle paid in the 
format shown in the test cases below. All numbers should be rounded to the nearest penny. 
Finally, print the result, which should include the total amount paid that year and the remaining 
balance. 

Retrieve user input. 
    Initialize some state variables. Remember to find the monthly interest rate from the 
annual interest rate taken in as input. 
    For each month: 
    Compute the new balance. This requires computing the minimum monthly 
payment and figuring out how much will be paid to interest and how much will be 
paid to the principal. 
    Update the outstanding balance according to how much principal was paid off. 
    Output the minimum monthly payment and the remaining balance. 
    Keep track of the total amount of paid over all the past months so far. 
 Print out the result statement with the total amount paid and the remaining balance. 


"""

# problem 1
def payMinimum():    
    userBalance = 4800
    userInterestRate = 0.2
    userMinMonthlyPaymentRate = 0.02
    month = 1
    total = 0
    for month in range (1, 13):
        minMonthlyPayment = round(userMinMonthlyPaymentRate * userBalance, 2)
        interestPaid = (userInterestRate/12) * userBalance
        principalPaid = round(minMonthlyPayment - interestPaid, 2)
        remainingBalance = userBalance - principalPaid

        userBalance = remainingBalance #new user balance
        total += minMonthlyPayment
        print "Month: ", month
        print "Minimum monthly payment:  $%.2f" % minMonthlyPayment
        print "Principle paid:  $%.2f" % principalPaid
        print "Remaining balance:  $%.2f" % remainingBalance
        print "\n"

    print "Total amount paid:  $%.2f" % total
    return

print payMinimum()

#problem 2
def payOffInOneYear():    
    userBalance = 4800
    userInterestRate = 0.18
    monthlyInterestRate = userInterestRate/12
    updatedBalance = userBalance
    monthlyPayment = 0

    while updatedBalance > 0:
        numMonths = 0
        updatedBalance = userBalance
        monthlyPayment += 10

        while numMonths < 12 and updatedBalance > 0:
            # Count this as a new month     
            numMonths += 1
            # Interest for the month
            interest = monthlyInterestRate * updatedBalance           
            # Subtract monthly payment from outstanding balance
            updatedBalance -= monthlyPayment
            # Add interest
            updatedBalance += interest


    # Round final balance to 2 decimal places
    updatedBalance = round(updatedBalance,2)
    print "Monthly payment to pay off debt in 1 year:", monthlyPayment
    print "Number of months needed:", numMonths
    print "Balance:",updatedBalance

print payOffInOneYear()

# problem3 
original_balance = 4800
interest_rate = 0.2


# Initialize state variables
balance = original_balance
low_payment = balance/12
high_payment = (balance*(1+(interest_rate/12))**12)/12

# Use bisection search until the search space is sufficiently small
while True:
    balance = original_balance
    monthly_payment = (low_payment + high_payment)/2

    # Simulate passage of time until outstanding balance is paid off
    # Each iteration represents 1 month
    for month in range(1,13):
        interest = round(balance*interest_rate/12, 2)
        balance += interest - monthly_payment
        if balance <= 0:
            break
        
    if (high_payment - low_payment < 0.005):
        # Bisection search space is small enough
        # Print result
        print "RESULT"

        # Round monthly payment up to the nearest cent
        monthly_payment = round(monthly_payment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year:", round(monthly_payment,2)

        # Recompute remaining balance and the number of months needed
        balance = original_balance
        for month in range(1,13):
            interest = round(balance*interest_rate/12, 2)
            balance += interest - monthly_payment
            if balance <= 0:
                break
        print "Number of months needed:", month
        print "Balance:", round(balance,2)
        break
    elif balance < 0:
        #Paying too much
        high_payment = monthly_payment
    else:
        #Paying too little
        low_payment = monthly_payment


