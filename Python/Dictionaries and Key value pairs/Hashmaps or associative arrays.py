# name is a varibale, and after adding a semi colon you can provide a value
student = {"name": 'John', "age": 25, 'courses': ['Math', 'Compsci']}
print(student)
print(student['courses'])
print(student.get('phone'))
#add a variable to a dictionary
student['phone'] = '555 5555'
print(student.get('phone'))
#you can update values in many ways
student['name'] = 'Jane'
#or
student.update({'name': 'Bash', 'age': 26, 'phone': '555 5556'})
print(student)
#you can remove a value, and assign it to another variable
name = student.pop('name')
print(student)
print(name)
#you can loop through keys in a dictionary
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
#next, you can list the variable in a dict.
for key in student:
    print(key)
    #this will return the dict variable
for key, value in student.items():
    print(key, value)
    #this will return the dict variable, value
for value in student:
    print(value)
    #this will return the dict. variable again
for key, value in student.items():
    print(value)
    #this will return the value only