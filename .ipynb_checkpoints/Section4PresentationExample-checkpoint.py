#You can slice strings up to get the parts you want!
apple = 'peel fruit core'
print(apple)

fruitBegin = apple.find('fruit')
#print('\'fruit\' begins at index: ', fruitBegin)

fruitStrlength = len('fruit')
#print('\'fruit \' is ', fruitStrlength, ' characters long')
fruitEnd = fruitBegin+fruitStrlength

#appleFruit = apple[fruitBegin:fruitEnd]
#print(appleFruit)

# You can add and change things within the strings:
string1 = 'I like tea!'
print(string1)
string1 = string1.replace('like', 'really like')
print(string1)

#you can combine strings:
string1 = 'apples '
string2 = 'and oranges'

combineStrings = string1 + string2
print(combineStrings)