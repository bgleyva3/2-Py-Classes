
""" 
    Se abre el archivo
    Se lee linea por linea
    Se crea un arreglo de palabras
    La palabra de cada arreglo se mete a un objeto y suma 1
    Al final se recorre todo el arreglo y se saca el valor y su key más grande
"""

import sys 

file_name = input("Ingrese el archivo a abrir: ")

try:
    file = open(file_name)
except OSError as e:
    print("No se encontró un archivo con el nombre", file_name)
    sys.exit()

frequent_word = ""
frequency = 0
word_Obj = {}
count = 0;

for line in file:
    line_word = line.strip().lower().replace(',','').replace('.','').split();

    for w in line_word:
        word_Obj[w] = word_Obj.get(w, 0) + 1


#Creo un arreglo vacio 
#Reviso la longitud del array
#if len = 0, inserto el primer objeto
#else, comparo el 


for i in word_Obj:
    print(i)
    print(word_Obj[i])
    print({i: word_Obj[i]})
    print("--------------------------------")
    """ count = word_Obj[i]
    if(count > frequency):
        frequency = count;
        frequent_word = i """
    

""" print("------------------------------------")
print("Palabra más repetida: " + frequent_word)
print("Frecuencia: " + str(frequency))
print("------------------------------------") """
file.close();



