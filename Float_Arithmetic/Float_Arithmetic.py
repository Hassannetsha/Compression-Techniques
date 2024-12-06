import pickle
from decimal import Decimal, getcontext

getcontext().prec = 50

def float_arithmetic_compression(data):
    dic = {}
    for ch in data:
        if ch == " ":
            key = "\\s"
        elif ch == "\n":
            key = "\\n"
        elif ch == "\t":
            key = "\\t"
        else:
            key = ch

        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    
    probabilities = []
    for key in dic:
        prob = Decimal((dic[key]) / len(data))
        probabilities.append((prob,key))

    ranges = []
    cumulative_probability = Decimal(0)
    for prob in probabilities:
        ranges.append((cumulative_probability, cumulative_probability+prob[0]))
        cumulative_probability+=prob[0]
    
    range_dic = dict(zip(dic,ranges))
    lower = Decimal(0)
    upper = Decimal(1)

    for ch in data:
        if ch == " ":
            key = "\\s"
        elif ch == "\n":
            key = "\\n"
        elif ch == "\t":
            key = "\\t"
        else:
            key = ch

        middle = upper - lower
        upper = lower + middle * range_dic[key][1]
        lower = lower + middle * range_dic[key][0]

    # Writes To A .txt File
    with open('Float_Arithmetic/compressed.txt', 'w') as file:
        
        file.write(f"{probabilities}\n")
        file.write(f"{(upper +lower)/2}\n")
        file.write(f"{len(data)}")

    # Writes To A .bin File
    with open('Float_Arithmetic/compressed.bin', 'wb') as file:
        pickle.dump((probabilities, (upper + lower) / 2, len(data)), file)
    

def float_arithmetic_decompression(bin_flag):
     decompress = ""
     code = Decimal(0)
     size = 0
     
     lower = Decimal(0)
     upper = Decimal(1)

     probabilities=[]
     range_dic = {} 
     cumulative_probability = Decimal(0)

    #  decide whether to decompress from a .bin or a .txt file
     if bin_flag:
        with open('Float_Arithmetic/compressed.bin', 'rb') as file:
             probabilities, code, size = pickle.load(file)
     else:
        with open('Float_Arithmetic/compressed.txt', 'r') as file:
            for i, line in enumerate(file):
                stripped_line = line.strip()
                if i == 0:
                    probabilities = eval(line.strip())
                elif i==1:
                    code = Decimal(stripped_line)
                else:
                    size = int(stripped_line)

    
     for prob,key in probabilities:
         range_dic[key] = (cumulative_probability, cumulative_probability + Decimal(prob))
         cumulative_probability += Decimal(prob)
     
     OGcode = code
     while size!=0:
         
         code = (OGcode-lower)/(upper-lower)
         for key, (range_low, range_high) in range_dic.items():
            if range_low <= code < range_high: 
                 if key == "\\s":
                    decompress += " "
                 elif key == "\\n":
                    decompress += "\n"
                 elif key == "\\t":
                    decompress += "\t"
                 else:
                    decompress += key

                 range_width = upper - lower
                 upper = lower + range_width * range_high
                 lower = lower + range_width * range_low
                 break
         size-=1

     with open('Float_Arithmetic/decompressed.txt', 'w') as file:
        file.write(decompress)