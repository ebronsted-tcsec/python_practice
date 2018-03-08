for x in range(0, 5):
    print('hello')
print(list(range(10, 20)))
for x in range(0, 5):
    print('hello %s' % x)
x = 0
while x < 5:
    x = x + 1
    print(x)
step = 0
tired = True
badweather = False
while step < 10000:
    print(step)
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step = step + 1
x = 45
y = 80
while x < 50 and y < 100:
        x = x + 1
        y = y + 1
        print(x, y)
for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
x = 1
while x < 14:
    print(x)
    x = x + 2
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
for i in ingredients:
    print(i)
for