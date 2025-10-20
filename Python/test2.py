my_set = ['1,2,3,5,6,4', '1,5,6,7,2']

list1 = set(my_set.pop().split(','))
list2 = set(my_set.pop().split(','))

if sorted(list1.intersection(list2)) == {0}:
    print('false')
else: 
    result = sorted(list1.intersection(list2))
    print(result)
