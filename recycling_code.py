
'''
recycling your code with functions and modules
'''


# using functions
list(range(0,5))

# parts of a function
def testfunc(myname):
    print('hello %s' % myname)
testfunc('Emily')


# variables and scope
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable

print(variable_test())

def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Week %s = %s cans' % (week, total_cans))

spaceship_building(2)

# using modules
import time
print(time.asctime())
import sys
print(sys.stdin.readline())
