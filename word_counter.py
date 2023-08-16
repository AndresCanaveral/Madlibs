import csv

'''
text = input("En qué estás pensando?: ")
text = text.split()
count = len(text)

print(f'Usted me ha mostrado su pensamiento en {count} palabras.')
'''


print("En qué estás pensando?")

file = open('file.txt','r')

count_w = {}
words = file.split()

for word in words:
  count = count_w.get(word,0)
  count += 1
  count_w[word] = count

file.close()





