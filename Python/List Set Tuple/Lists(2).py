#byilt in to sort
nums = [1,2,3,4,5]
print(min(nums))
print(max(nums))
print(sum(nums))
#how to find values, its will show index of value
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('CompSci'))
#is something in a list? Trye or False
print('CompSci' in courses)
# list of all items
for everything in courses:
    print(everything)
# you can also ask for number or index
for index, course in  enumerate(courses):
    print(index, course)
# to start as 1 instead of 0
for index, course in  enumerate(courses, start=1):
    print(index, course)
#turn list to string of comma sepperated values
course_str = ', '.join(courses)
print(course_str)
#string back to list
newlist = course_str.split()
print(newlist)
#TUPLES you cannot modify
