
def getDataSearch(korpus, query) :
    term = []
    inverted_list = {}
    result = []

    #Memisahkan kata menjadi term
    for doc in korpus :
        for kata in korpus[doc].split() :
            if kata not in term :
                term.append(kata.removesuffix(",").removesuffix("."))

    #Membuat kata menjadi biner
    for kata in term :
        data = []
        for doc in korpus :  
            if kata in korpus[doc] :
                data.append(1)
            else :
                data.append(0)
        inverted_list[kata] = data;     


    kalimat = query

    biner = []

    #Melakukan penjumlahan pada biner untuk mencari kata pada document yang tersedia
    for kata in kalimat.split() :
        if kata in inverted_list:
            for index in range(len(inverted_list[kata])) :
                if len(biner) > index : 
                    biner[index] = biner[index] & inverted_list[kata][index]
                else :
                    biner.append(inverted_list[kata][index])


    #Melakukan perulangan untuk mendapatkan document mana yang didapat dengan index biner  
    for index in range(len(biner)) :
        if biner[index] == 1 :
            result.append({"title" : list(korpus.keys())[index], "content" : korpus[list(korpus.keys())[index]]})

    return result        