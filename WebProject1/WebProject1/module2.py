userSize = int(input("Choose size square (Number): "))
size = userSize

inner = size - 2
print ('*' * size)
for i in range(inner):
    newinner = inner = inner - 1
    final = size - 2 - newinner
    print ('*' + newinner * '*' + final * ' ' + '*' )
print ('*' * size)