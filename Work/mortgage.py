# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

months = 0
while principal > 0:
    months += 1
    curr_payment = (payment + extra_payment) if  extra_payment_start_month <= months <= extra_payment_end_month else payment
    principal = principal * (1+rate/12) - curr_payment

    if principal < 0:
        curr_payment += principal
        principal = 0.0

    total_paid = total_paid + curr_payment
    print(f'{months} {total_paid:.2f} {principal:.2f}')

print(f'Total paid {total_paid:.2f}')
print(f'Months {months}')
