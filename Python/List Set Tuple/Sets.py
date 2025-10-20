#sets dont care about order
course = {'a','b','c','d','e'}
print(course)
#if you run the above multiple tines, it changes location of variables
#sets throw away duplicates
course = {'a','b','c','d','e','a'}
print(course)
#membership test? True or False
print('Math' in course)
#to find variable of a set they have in common?
course = {'a','b','c','d','e','a'}
course2 = {'f','l','c','s','v','a'}
print(course.intersection(course2))
print(course.difference(course2))
#to combine
print(sorted(course.union(course2)))
