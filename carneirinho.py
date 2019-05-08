carneirinho = 0
sono = input('Já dormi?').lower()
while sono != 'sim':
        carneirinho += 1
        print(carneirinho)
        sono = input('Já dormi?')
print('Dormiu. FIM!')