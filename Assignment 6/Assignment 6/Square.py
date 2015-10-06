size = int(raw_input('Square: '))
square = ''
for x in range(size):
    for y in range(size):
        square = square + '*'
    square = square + '\n'      
print square