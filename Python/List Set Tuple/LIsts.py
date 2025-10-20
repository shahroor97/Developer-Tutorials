#to create a list, do this
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
#to find length of a list, do this
print(len(courses))
#to access a value of a list, do this (starting from 0)
print(courses[0])
#you can also go backwards
print(courses[-1])
#to do multiple, doesnt include last index
print(courses[0:2])
#dont include anything in first or last index to start from beginning
print(courses[:3])
#if you want to add an item to the list
courses.append('Art')
print(courses)
#OR
courses.insert(2, 'Art')
print(courses)
# or u can add one variable/list to another
courses2 = ["Bio", "Chem"]
courses.extend(courses2)
print(courses)
#if you want to remove a value,
courses.remove('Art')
print(courses)
#OR, this is interesting. An empty index removes last variable
removed = courses.pop()
print(removed)
print(courses)
#it removed the variable, and by assigned a name it can list it
#let us sort lists
#reverse  list
courses.reverse()
print(courses)
#sort by alphabetical order
courses.sort()
print(courses)
#you can also reverse
courses.sort(reverse=True)
print(courses)
#you can also sort by adding it as a varibla without altering the origninal
sorted_courses = sorted(courses)
print(sorted_courses)