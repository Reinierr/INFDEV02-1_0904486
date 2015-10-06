size = int(raw_input('Square: '))
squareH = ''
for x in range(size):
    for y in range(size):
        if(x > 0 and x < size-1 and y > 0 and y < size-1):
            squareH += ' '
        else:
            squareH += '*'
    squareH += '\n'     
print squareH