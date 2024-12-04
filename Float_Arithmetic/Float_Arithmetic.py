def float_arithmetic_compression(data):
    dic = {}
    for ch in data:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    

    # encoded_data = data.replace('\n', '\\n').replace(' ', '\\s').replace('\t', '\\t')
    # # Update dictionary to include special sequences
    # if '\\n' not in dic:
    #     dic['\\n'] = 0
    # if '\\s' not in dic:
    #     dic['\\s'] = 0
    # if '\\t' not in dic:
    #     dic['\\t'] = 0
    
    probabilities = []
    for key in dic:
        probabilities.append(dic[key]/len(data))

    ranges = []
    cumulative_probability = 0
    for prob in probabilities:
        ranges.append((cumulative_probability, cumulative_probability+prob))
        cumulative_probability+=prob
    
    range_dic = dict(zip(dic,ranges))
    lower=0
    upper=1

    for ch in data:
        middle = upper - lower
        lower = lower + middle * range_dic[ch][0]
        upper = lower + middle * range_dic[ch][1]

    with open('Float_Arithmetic/compressed.txt', 'w') as file:
        probability = dic[key] / len(data)
        for key in dic:
            if key == " " or key == "\t" or key == "\n":
                file.write(f"({key}) {probability}\n")
            else:
                file.write(f"{key} {probability}\n")
        file.write(f"{(lower + upper) / 2}")
        file.write(f"{len(data)}")
    

def float_arithmetic_decompression():
     decompress = ""
     code = 0
     size = 0
     
     lower=0
     higher=1

     range_dic = {} 
     cumulative_probability = 0
     with open('Float_Arithmetic/compressed.txt', 'r') as file:
        for line in file:
            parts = line.strip(" ").split()
            if len(parts) == 1 and code == 0:
                code = float(parts[0])
            elif len(parts) == 1:
                size = int(parts[0])
            elif len(parts) == 2:
                range_dic[parts[0]] = (cumulative_probability, cumulative_probability+float(parts[1]))
                cumulative_probability+=float(parts[1])
            else:
                print("a7a")
                break


     while size!=0:
         
         code = (code-lower)/(higher-lower)
         for key in range_dic:
             if code >= range_dic[key][0] and code <= range_dic[key][1]:
                 decompress+=key
                 middle = upper - lower
                 lower = lower + middle * range_dic[key][0]
                 upper = lower + middle * range_dic[key][1]
                 break
         size-=1

     with open('Standard_Huffman/decompressed', 'w') as file:
        file.write(decompress)
        
        
     
     
    




file_data = ""
with open('Float_Arithmetic/Input.txt', 'r') as file:
    file_data = file.read()
while(True):
    print("Enter 1 if you want to compress the text in file called input.txt")
    print("Enter 2 if you want to input text to compress.")
    print("Enter 3 if you want to decompress the compressed data in file compressed_data")
    print("Enter 0 if you want to Exit")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        float_arithmetic_compression(file_data)
    elif inp==2:
        float_arithmetic_compression(input("Input Text to be compressed: "))
    elif inp==3:
        float_arithmetic_decompression()
    else:
        break