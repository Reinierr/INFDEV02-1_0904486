while True:
    fahrenheit = int(input('Fahrenheit number: '))
    celsius = round((fahrenheit - 32) * 5/9, 2)
    print('Celsius: '+ str(celsius))
    kelvin = round(celsius + 273.15, 2)
    if kelvin <= 0:
        print('Kelvin is below absolute zero')
    else:
        print('Kelvin: '+ str(kelvin))
        break