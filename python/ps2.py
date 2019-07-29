import math

def polysum(n, s):
    '''
    input: int, num -> output: float
    given the number of sides n and length of side s of a regular
    polygon, returns the sum of the area and the perimeter squared
    '''
    area = (0.25*n*(s**2))/(math.tan(math.pi/n))
    perimeter = n*s
    return round(area + perimeter**2, 4)

'''
Problem 1
calculate the credit card balance after one year if a person
only pays the minimum monthly payment required each month.
given variables:
    balance: outstanding balance
    annualInterestRate: annual rate as decimal
    monthlyPaymentRate: minimum monthly payment rate as decimal
'''

def owed(balance, monthrate, interest):
    '''
    input is three floats: balance outstanding,
    monthly payment rate, and annual interest rate.

    Returns balance outstanding for next month.
    '''
    monthPaid = balance*monthrate
    return (balance-monthPaid)+(balance-monthPaid)*(interest/12)

def outstanding_after(balance, months, monthrate, interest):
    '''
    input: float, int, float, float: balance outstanding at initial time,
    months passed, monthly payment rate, yearly interest

    Returns outstanding balance after months have passed.
    Recursive: base case is only one month, determines owed() on it recursively
    '''
    if months == 1:
        return owed(balance, monthrate, interest)
    else:
        return owed(outstanding_after(balance, months-1, monthrate, interest), monthrate, interest)

months = 12 #number of months in which payment rate is the same
final_outstanding = outstanding_after(balance, months, monthlyPaymentRate, annualInterestRate)
print("Remaining balance: " + str(round(final_outstanding, 2)))


'''
Problem 2
calculate the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. The monthly payment
must be a multiple of $10
given variables:
    balance: outstanding balance
    annualInterestRate: annual rate as decimal

Had to modify Problem 1 functions so that the were using monthly payments
and not monthly payment rates:
'''

def owed2(balance, monthPaid, interest):
    '''
    input is three floats: balance outstanding,
    monthly payment, and annual interest rate.

    Returns balance outstanding for next month.
    '''
    return (balance-monthPaid)+(balance-monthPaid)*(interest/12)

def outstanding_after2(balance, months, monthPaid, interest):
    '''
    input is float, int, float, float: balance outstanding at initial time,
    months passed, monthly payment, yearly interest

    Returns outstanding balance after months have passed
    Recursive: base case is only one month, determines owed() on it recursively
    '''
    if months == 1:
        return owed2(balance, monthPaid, interest)
    else:
        return owed2(outstanding_after2(balance, months-1, monthPaid, interest), monthPaid, interest)

def idealmonthly(balance, interest, time):
    '''
    input is float float int: outstanding balance, interest,
    and months within which to pay off debt.

    Returns the minimum monthly payment required to pay off
    balance within the specified time.
    Tried to do it recursively but iteratively
    is really intuitive and short
    '''
    pay = 0
    while outstanding_after2(balance, time, pay, interest) > 0:
        pay += 10
    return pay

print('Lowest Payment: ' + str(idealmonthly(balance, annualInterestRate, months)))


'''
Problem 3

Do problem 2 but using bisection search. Give lowest payment to 2 decimal places.

Note: using outstanding_after2 and owed2 to get idealmonthly_bis()
Note: initial lower bound is 1/12 of initial balance.
      initial upper bound is 1/12 of final balance with interest and no payment.
'''

def idealmonthly_bis(balance, interest, time):
    '''
    input is float float int: outstanding balance, interest,
    and months within which to pay off debt.

    Returns the minimum monthly payment (to the cent) required to pay off
    balance within the specified time using bisection search.
    '''
    low = balance/time
    high = outstanding_after2(balance, time, 0, interest)
    pay = (high+low)/2
    while round(abs(outstanding_after2(balance, time, pay, interest)), 2) > 0.00:
        if outstanding_after2(balance, time, pay, interest) < 0:
            high = pay
        else:
            low = pay
        pay = (high+low)/2
    return round(pay, 2)

print('Lowest Payment: ' + str(idealmonthly_bis(balance, annualInterestRate, months)))
