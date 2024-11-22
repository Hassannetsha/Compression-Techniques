def Standard_Huffman_comp(Probabilities):
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
        # j = 0
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
    









Data = ""
with open('Standard-Huffman/Input.txt', 'r') as file:
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
# letter = ''
# probability = False
# first_part = True
# second_part = False
# first_part_num = ""
# second_part_num = ""
# if Data.count('.'):
#     first_part = False
#     second_part = False
#     decimal = ""
# i = 0
# while i < len(Data):
#     if Data[i].lower() == "p" and not probability:
#         probability = True
#     elif Data[i]=='(':
#         i+=1
#         letter = Data[i]
#     elif not probability:
#         break
#     while(Data[i].isdigit() or Data[i]=='.'):
#         if first_part:
#             first_part_num += Data[i]
#         elif second_part:
#             second_part_num += Data[i]
#         else:
#             decimal += Data[i]
#         i+=1
#     if first_part_num != "":
#         first_part = False
#         second_part = True
#     if Data[i]=='\n':
#         if not first_part and not second_part:
#             probability = False
#             decimal = float(decimal)
#             Probabilities.append((decimal,letter))
#             letter = ''
#             decimal =  ""
#         else:
#             probability = False
#             first_part = True
#             first_part_num = int(first_part_num)
#             second_part_num = int(second_part_num)
#             Probabilities.append((first_part_num/second_part_num,letter))
#             letter = ''
#             first_part_num = ""
#             second_part_num = ""
#     i+=1
# Probabilities = sorted(Probabilities,reverse=True)
# data = ""
# i+=1
# while i< len(Data):
#     data += Data[i]
#     i+=1
dic = Standard_Huffman_comp(Probabilities)
compressed_data = []
compressed_data.append(Probabilities)
# for ch in data:
for ch in Data:
    compressed_data.append(dic[ch])
    
with open('Standard-Huffman/compressed_data.txt', 'w') as file:
    for item in compressed_data:
        file.write(f"{item}\n")
    

# print(Probabilities)
#aabcdef
#11 11 10 001 0000 01 0001








# p(H) = 1/14
# p(a) = 1/7
# p(s) = 5/28
# p(n) = 1/14
# p( ) = 3/28
# p(S) = 1/28
# p(h) = 1/14
# p(e) = 1/14
# p(r) = 1/14
# p(i) = 1/28
# p(f) = 1/28
# p(E) = 1/28
# p(l) = 1/28
# p(k) = 1/28


# Hassan Sherif Hassan Elkersh