#how loops work
nums = [1,2,3,4,5]
for num in nums:
    print(num)
#this create a loop from 1-5 (start of list to last)

for num in nums:
    if num == 3:
        print('Found') #replaces 3 with found
        break #stop
    print(num)

for num in nums:
    if num == 3:
        print('Found') #replaces 3 with found
        continue #keeps going
    print(num)

#lets try appplying a string to each variable in the list:
for num in nums:
    for letter in 'abc':
        print(num, letter)
#lets run a loop 10 times (Starting from 1, and finishing up to (not including) 11)
for i in range(1, 11):
    print(i)
#while
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
#infinte loop
while True:
    if x == 5:
        break
    print(x)
    x += 1