# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_pay_month_start = 61
extra_pay_month_end = 108
extra_payment = 1000

while principal > 0:
    if months >= extra_pay_month_start and months <= extra_pay_month_end:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    
    if principal < 0:
        total_paid += principal  # Reduce total paid by the overpaid amount
        principal = 0

    months += 1
    print(months, round(total_paid,2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', months)

#>>> bool("False")
#True
#>>> any non-empty string is considered True when converted to a boolean.
#"False" is a non-empty string, so bool("False") returns True.