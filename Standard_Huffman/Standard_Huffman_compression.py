def mapping_characters(Probabilities):
    dic = {}
    Total_Probabilities = [Probabilities]
    while len(Total_Probabilities[len(Total_Probabilities)-1])>2:
        prob = []
        i = 0
        while i < len(Total_Probabilities[len(Total_Probabilities)-1])-2:
            prob.append(Total_Probabilities[len(Total_Probabilities)-1][i])
            i+=1
        
        sum = Total_Probabilities[len(Total_Probabilities)-1][i][0]
        letters = Total_Probabilities[len(Total_Probabilities)-1][i][1]
        i+=1
        sum += Total_Probabilities[len(Total_Probabilities)-1][i][0]
        letters += Total_Probabilities[len(Total_Probabilities)-1][i][1]
        prob.append((sum,letters))
        prob = sorted(prob,reverse=True)
        Total_Probabilities.append(prob)
    i = len(Total_Probabilities)-1
    dic = {
            Total_Probabilities[i][0][1]:"0",
            Total_Probabilities[i][1][1]:"1",
           }
    i -= 1
    while i>=0:
        last = len(Total_Probabilities[i])-1
        char = Total_Probabilities[i][last][1]
        if char not in dic:
            for key in dic.keys():
                if(key.find(char) and len(key)>=2):
                    old_key = key
                    old_bin = dic[key]
                    del dic[key]
                    new_key = old_key.replace(char,"")
                    new_bin = old_bin+"0"
                    dic[new_key] = new_bin
                    dic[char] = old_bin+"1"
                    i-=1
                    break
        else:
            last-=1
    return dic
    


def Standard_Huffman_compression():
    Data = ""
    with open('Standard_Huffman/Input.txt', 'r') as file:
        Data = file.read()
    Probabilities = []
    dic = {}
    for ch in Data:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    for key in dic:
        Probabilities.append((dic[key]/len(Data),key))
    Probabilities = sorted(Probabilities,reverse=True)
    dic = mapping_characters(Probabilities)
    compressed_data = []
    compressed_data.append(Probabilities)
    for ch in Data:
        compressed_data.append(dic[ch])
        
    with open('Standard_Huffman/compressed_data.txt', 'w') as file:
        for item in compressed_data:
            file.write(f"{item}\n")
        