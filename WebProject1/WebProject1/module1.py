userName = input("Uw naam: ")
print("Welkom " + userName)

size = 10
inner = size - 2
staticinner = size - 2
print ('*' * size)
for i in range(inner):
    newinner = inner = inner - 1
    final = staticinner - newinner
    print ('*' + newinner * '*' + final * ' ' + '*' )
print ('*' * size)