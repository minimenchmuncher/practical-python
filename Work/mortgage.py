# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
period = 0

while principal > 0:
    extra = 1000 if period < 12 else 0
    principal = principal * (1 + rate / 12) - payment - extra
    total_paid = total_paid + payment + extra
    period += 1

print('Total paid', total_paid)
