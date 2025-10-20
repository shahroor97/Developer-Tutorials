message = "hello bash's world"

print(message[:5])
print(message[6:])

print(message.upper())
print(message.lower())

print(message.count('b'))
print(len(message))

print(message.find('bash'))
message2 = message.replace('hello', 'building')
print(message2)

greeting = 'Hi'
name = 'Buchra'
#the example below needs a space in between which is added in between the apostraphes.
message3 = greeting + ' ' + name
print(message3)
#or you can use a formated string, for example
message3 = '{}, {}. Welcome!'.format(greeting, name)
print(message3)
#OR you can use an f string
message4 = f'{greeting}, {name}, Welcome!'
#the good thing about f strings is that u can add code within the placeholder
message4 = f'{greeting}, {name.upper()}, Welcome!'
print(message4)
#if you need help on a command, do this. This is asking for help for str. or str.lower
print(help(str.lower))