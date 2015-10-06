size = int(raw_input('Triangle: '))
triangle = ''
for x in range(size):
    for y in range(x+1):
        triangle = triangle + '*'
    triangle = triangle + '\n'
print triangle