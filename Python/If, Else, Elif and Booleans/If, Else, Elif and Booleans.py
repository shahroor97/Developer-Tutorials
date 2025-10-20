language = 'METROBOOMIN'
#one = is setting a value, two == is checking equality
if language == 'python':
    print('Language is Python')
else:
    print('NOT')
#heres how to use ELIF
if language == 'python':
    print('pldpdlpdlld')
elif language == 'Java':
    print('YEP')
elif language == 'METROBOOMIN':
    print('METROO')
else:
    print('NOT')

#lets try something else with "and" and "or"

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('NO ENTRY')

if user == "Admin" or logged_in:
    print('YOURE IN')
else:
    print('YOURE OUT')
# we can also use "not": it switched false to true.
if not logged_in:
    print('Please login')
else:
    print('ENTER')

#now lets check if two objects are the same in "memory" by using == or is

a= [1,2,3]
b= [1,2,3]
print(id(a)) #they have different ID's
print(id(b))
print(a is b) #a and b are no equal from memory due to different ID
print(a==b) #but they are equal

#lets check whats true and false (None false, so is 0, and so is a empty list, tuple, or str)

condition = False or None or 0 or () or [] or {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# now we can try the same thing but add an or with a soemthing that switches it to true
condition = False or None or 0 or () or [] or {} or 1
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')