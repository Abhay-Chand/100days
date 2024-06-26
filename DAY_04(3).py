#While Loop
#syntax
'''while [boolean expression]:
    statement1
    statement2
    ...
    statementN'''

# Question:
#using break:
'''num = 0

while num < 5:
    num += 1   # num += 1 is same as num = num + 1
    print('num = ', num)
    if num == 3: # condition before exiting a loop
        break
'''
#using continue
'''num = 0

while num < 5:
  num += 1   # num += 1 is same as num = num + 1
  if num > 3: # condition before exiting a loop
    continue
  print('num = ', num)
'''
#using else:
'''num = 0

while num < 3:
  num += 1   # num += 1 is same as num = num + 1
  print('num = ', num)
else:
    print('else block executed')
'''
#QUESTION:
'''number as input from the user and calculates the average, as long as the user enters a positive number. Here, the repetitive block (the body of the loop) asks the user to input a number, adds it cumulatively and keeps the count if it is non-negative.'''

num=0
count=0
sum=0

while num>=0:
    num = int(input('enter any number .. -1 to exit: '))
    if num >= 0:
        count = count + 1 # this counts number of inputs
        sum = sum + num # this adds input number cumulatively.
avg = sum/count
print('Total numbers: ', count, ', Average: ', avg)