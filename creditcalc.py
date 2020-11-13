import argparse
from math import ceil, floor, log


def number_of_payments(number):
    if 11 < number < 12 or number % 12 >= 11:
        number = ceil(number)
    years = int(number // 12)
    months = ceil(number % 12)
    if number == 1:
        print(f'It will take {months} month to repay this loan!')
    elif number <= 11:
        print(f'It will take {months} months to repay this loan!')
    elif number <= 12:
        print(f'It will take {years} year to repay this loan!')
    elif number <= 23:
        print(f'It will take {years} year and {months} months to repay this loan!')
    elif number % 12 == 0:
        print(f'It will take {years} years to repay this loan!')
    elif number % 12 <= 1:
        print(f'It will take {years} years and {months} month to repay this loan!')
    else:
        print(f'It will take {years} years and {months} months to repay this loan!')


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', dest='t', help='choose between annuity and differentiated loans')
parser.add_argument('-pay', '--payment', dest='pay', help='monthly payment amount', type=float)
parser.add_argument('-pcp', '--principal', dest='pcp', help='loan principal', type=float)
parser.add_argument('-prd', '--periods', dest='prd', help='number of months to repay the loan', type=int)
parser.add_argument('-itt', '--interest', dest='itt', help='loan interest rate', type=float)
args = parser.parse_args()
t = args.t
pay = args.pay
pcp = args.pcp
prd = args.prd
itt = args.itt

if t == 'annuity' or 'diff' and itt and (pay and pcp or pay and prd or pcp and prd):
    if itt >= 0 and (pay and pcp or pay and prd or pcp and prd) > 0:
        itt /= 1200
        if t == 'annuity':
            if not pay:
                pay = itt * pow((1 + itt), prd) / (pow(1 + itt, prd) - 1)
                pay *= pcp
                print(f'Your monthly payment = {ceil(pay)}!')
                print(f'Overpayment = {int(ceil(pay) * prd - pcp)}')
            elif not pcp:
                pcp = itt * pow((1 + itt), prd) / (pow((1 + itt), prd) - 1)
                pcp = pay / pcp
                print(f'Your loan principal = {floor(pcp)}!')
                print(f'Overpayment = {ceil(pay * prd - pcp)}')
            elif not prd:
                if itt == 0:
                    n = pcp / pay
                    number_of_payments(n)
                elif itt > 0:
                    n = log(pay / (pay - itt * pcp), 1 + itt)
                    number_of_payments(n)
                    print(f'Overpayment = {ceil(pay * ceil(n) - pcp)}')
        elif t == 'diff' and not pay:
            diff_sum = 0
            m = 0
            while m < prd:
                m += 1
                diff = ceil(pcp / prd + itt * (pcp - pcp * (m - 1) / prd))
                diff_sum += diff
                print(f'Month {m}: payment is {diff}')
            print(f'Overpayment = {round(diff_sum - pcp)}')
    else:
        print('Incorrect parameters')

else:
    print('''What do you want to calculate?
type "a" for annuity monthly payment amount,
type "d" for differentiated payment amount,
type "n" for number of monthly payments,
type "p" for loan principal:''')
    choice = input()

    if choice == 'a':
        print('Enter the loan principal:')
        loan_principal = float(input())
        print('Enter the number of periods:')
        periods = int(input())
        print('Enter the loan interest:')
        loan_interest = float(input())
        loan_interest /= 1200

        a = loan_interest * pow((1 + loan_interest), periods) / (pow(1 + loan_interest, periods) - 1)
        a *= loan_principal
        print(f'Your monthly payment = {ceil(a)}!')
        print(f'Overpayment = {int(ceil(a) * periods - loan_principal)}')

    elif choice == 'd':
        print('Enter the loan principal:')
        principal = float(input())
        print('Enter the number of periods:')
        periods = int(input())
        print('Enter the loan interest:')
        interest = float(input())
        interest /= 1200

        diff_sum = 0
        m = 0
        while m < periods:
            m += 1
            diff = ceil(principal / periods + interest * (principal - principal * (m - 1) / periods))
            diff_sum += diff
            print(f'Month {m}: payment is {diff}')
        print(f'Overpayment = {round(diff_sum - principal)}')

    elif choice == 'n':
        print('Enter the loan principal:')
        loan_principal = float(input())
        print('Enter the monthly payment:')
        monthly_payment = float(input())
        print('Enter the loan interest:')
        loan_interest = float(input())
        loan_interest /= 1200

        if loan_interest == 0:
            n = loan_principal / monthly_payment
            number_of_payments(n)
        elif loan_interest > 0:
            n = log(monthly_payment / (monthly_payment - loan_interest * loan_principal), 1 + loan_interest)
            number_of_payments(n)
            print(f'Overpayment = {ceil(monthly_payment * ceil(n) - loan_principal)}')
        else:
            print('Error: invalid input')

    elif choice == 'p':
        print('Enter the annuity payment:')
        monthly_payment = float(input())
        print('Enter the number of periods:')
        periods = int(input())
        print('Enter the loan interest:')
        loan_interest = float(input())
        loan_interest /= 1200

        p = loan_interest * pow((1 + loan_interest), periods) / (pow((1 + loan_interest), periods) - 1)
        p = monthly_payment / p
        print(f'Your loan principal = {floor(p)}!')
        print(f'Overpayment = {ceil(monthly_payment * ceil(periods) - p)}')

    else:
        print('Error: invalid input')
