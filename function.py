def letter_match(strArr):
    #la palabra buscada
    my_word = strArr[0]
    #lista de las letras que conforman la palabra buscada.
    letters_of_word = [x for x in my_word] 
    #Convierte la segunda cadena de palabras separadas por coma en una lista de palabras.
    sep_list = strArr[1].split(",")          

    rank_word = []

    #Compara cuáles caracteres de la palabra que se desea buscar hacen match con el listado de palabras (separados por coma)
    # y crea un ranking entre ellas
    for word in sep_list:                           
        counter = 0                                                 
        for letter in word:
            if letter in letters_of_word:
                counter += 1
            else:
                counter += 0
        rank_word.append(counter)
    if max(rank_word) < 1:
        return -1
    else:
        highest_match_index = rank_word.index(max(rank_word))
        highest_match_word =sep_list[highest_match_index]
        dif =  len(highest_match_word) - len(letters_of_word)
        return dif


if __name__ == "__main__":
    #Probando la función 
    strArr=["worthy","worth,ess,worl,xx,eee,worthooy"]
    print(letter_match(strArr))       
    
