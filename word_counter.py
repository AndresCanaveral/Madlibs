import csv

'''
text = input("En qué estás pensando?: ")
text = text.split()
count = len(text)

print(f'Usted me ha mostrado su pensamiento en {count} palabras.')
'''


print("En qué estás pensando?")

file = open('file.txt','r')

words = file.split()



file.close()





