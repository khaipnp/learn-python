# Course 1: Comment line
print("------------Course 1: Comment line------------")
print("Hello Word")

# Course 2: Variable
print("------------Course 2: Variable------------")
_a2 = 19 #Init variable a with 19
_b2 = 5
_c2 = _a2 + _b2 * _b2
print(_c2)

# Course 3: Variable (Number)
print("------------Course 3: Variable (Number)------------")
# Integer
_a3 = 4
# Float
_b3 = 1.96123532959195018614326353412351
# Decimal
## Get all (*) library decimal
from decimal import *
getcontext().prec = 30
_c3 = Decimal(10)/Decimal(3)
# Fraction
## Get all (*) library fraction
from fractions import *
_d3 = Fraction(6,9)
# Complex
_e3 = complex(2,5)

# Course 4: String
print("------------Course 4: String------------")
_strA = 'I am %s%s years old and I have %s wife' %(2, 8, 1)
print(_strA)