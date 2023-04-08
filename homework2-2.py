import math

a_str = '3/4'
b_str = '5/6'
a = a_str.split('/')
b = b_str.split('/')
a1 = int(a[0])
a2 = int(a[1])
b1 = int(b[0])
b2 = int(b[1])
sum_numerator = int((a1 * b2 + a2 * b1)/math.gcd(a1 * b2 + a2 * b1, a2 * b2))
sum_denominator = int((a2 * b2)/math.gcd(a1 * b2 + a2 * b1, a2 * b2))
prod_numerator = int((a1 * b1)/math.gcd(a1 * b1, a2 * b2))
prod_denominator = int((a2 * b2)/math.gcd(a1 * b1, a2 * b2))
print(f'{sum_numerator}/{sum_denominator}')
print(f'{prod_numerator}/{prod_denominator}')