#lets create a function

def hello_func():
    pass #dont want to add anything in def for now.
print(hello_func()) #this function can do nothing as of now as it is empty

#we can set a function to do something without retyping
def hello_func():
    print('Hello Function')

hello_func()# this runs the funciton

#functions help in not repeating typing (for example theres a typo for a reused object)
#DRY: dont repeat yourself
#lets try something else

def func():
    return 'Hello'

print(func())
print(func().upper()),

#lets pass arguments in a function and customise it using parameters

def hi(name):
    return '{} youre a genius'.format(name)
print(hi('Bash'.upper())) #Bash is the paramater (name) needed to print the function

#we can add multiple parameter
def by(name, age):
    return 'Hello {}, youre {} years old!'.format(name, age)
print(by('Bash', '25'))