#an integer is a whole number, a float is a decimal
num = 3
print(type(num))
num2 = 4.1
print(type(num2))
#shortcut for increments
num3 = 1
num3 += 3
# this means num3 = num3 + 3
print(num3)
#abosolute value and rounding
print(abs(-3))
print(round(4.21))
print(round(4.5))
#u can also round to a a number of digits after a decimal, it does not round up for 0.5
print(round(4.254, 1))
print(round(4.626, 2))
# you can also compare (== equal, != not equal, >=, <=)
num4 = 2
num5 = 4
print(num4 == num5)
print(num4 != num5)
#casting is changing from str to intm you cant "add" strings
num6 = '10'
num7 = '12'
print(num6+num7)
num6 = int(num6)
num7 = int(num7)
print(num6+num7)
