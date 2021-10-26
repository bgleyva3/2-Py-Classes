import sys 

file_name = input("Ingrese el archivo a abrir: ")

try:
    file_selected = open(file_name)
except OSError as e:
    print("No se encontró un archivo con el nombre", file_name)
    sys.exit()

class Counter:
    @staticmethod
    def most_repeated_words(file):

        word_Obj = {}
        array = []

        for line in file:
            line_word = line.strip().lower().replace(',','').replace('.','').split();

            for w in line_word:
                word_Obj[w] = word_Obj.get(w, 0) + 1



        for i in word_Obj:
            if len(array) == 0:
                array.append([i, word_Obj[i]])
            else:
                inserted = False
                for j in range(len(array)):
                    if word_Obj[i] > array[j][1]:
                        array.insert(j, [i, word_Obj[i]])
                        inserted = True
                        break
                if inserted == False and len(array) < 10:
                    array.append([i, word_Obj[i]])
                array = array[0:10]

        print("The most repeated words are:")

        count = 0
        for i in array:
            count = count + 1
            print(count, ') "', i[0], '" ', i[1], " veces")


Counter.most_repeated_words(file_selected)

file_selected.close();
