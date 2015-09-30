string = raw_input('Your string: ')
shift = int(raw_input('Amount to shift with: '))

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

dic={}  
for i in range(0,len(alphabet)):  
    dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

newtext='' 
for l in string:
    if l.isupper():
        l = l.lower()
        if l in dic:
            print(l)
            l=dic[l]
        newtext+=l.upper()
    else:
        if l.lower() in dic:  
            l=dic[l]
        newtext+=l
  
print 'Your new string: '+newtext