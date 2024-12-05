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
        probabilities.append(Decimal(dic[key]) / Decimal(len(data)))

    ranges = []
    cumulative_probability = Decimal(0)
    for prob in probabilities:
        ranges.append((cumulative_probability, cumulative_probability+prob))
        cumulative_probability+=prob
    
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


    with open('Float_Arithmetic/compressed.txt', 'w') as file:
        for key in dic:
            probability = Decimal(dic[key]) / Decimal(len(data))
            file.write(f"{key} {probability}\n")
        file.write(f"{(upper +lower)/2}\n")
        file.write(f"{len(data)}")
    

def float_arithmetic_decompression():
     decompress = ""
     code = Decimal(0)
     size = 0
     
     lower = Decimal(0)
     upper = Decimal(1)

     range_dic = {} 
     cumulative_probability = Decimal(0)
     with open('Float_Arithmetic/compressed.txt', 'r') as file:
        for line in file:
            parts = line.strip(" ").split()
            if len(parts) == 1 and code == Decimal(0):
                code = Decimal(parts[0])
            elif len(parts) == 1:
                size = int(parts[0])
            elif len(parts) == 2:
                if parts[0] == "\\s":
                    key = " "
                elif parts[0] == "\\n":
                    key = "\n"
                elif parts[0] == "\\t":
                    key = "\t"
                else:
                    key = parts[0]

                range_dic[key] = (cumulative_probability, cumulative_probability + Decimal(parts[1]))
                cumulative_probability += Decimal(parts[1])
            else:
                print("Error Parsing Data")
                return
    
     OGcode = code
     while size!=0:
         
         code = (OGcode-lower)/(upper-lower)
         for key, (range_low, range_high) in range_dic.items():
            if range_low <= code < range_high: 
                 decompress += key
                 range_width = upper - lower
                 upper = lower + range_width * range_high
                 lower = lower + range_width * range_low
                 break
         size-=1

     with open('Float_Arithmetic/decompressed.txt', 'w') as file:
        file.write(decompress)