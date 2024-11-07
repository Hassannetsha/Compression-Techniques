import ast

def lz_w_Decompression(data:list):
    # data = [int(num) for num in datastring]
    i=0
    key=128
    dictionary = {}
    original_data = ""
    prev_str = ""
    while i<len(data):

        if data[i] <= 127:
            original_data+= chr(data[i])
            
            if prev_str:
                dictionary[key] = prev_str + chr(data[i])
                key+=1

            prev_str = chr(data[i])
            i+=1
            continue

        else:
            if data[i] in dictionary:
                original_data+= dictionary[data[i]]
                dictionary[key] = prev_str+dictionary[data[i]][0]
                key+=1
                prev_str = dictionary[data[i]]
                i+=1
                continue

            else:
                prev_str = prev_str+prev_str[0]
                original_data+=prev_str
                key = data[i]
                dictionary[data[i]] = prev_str
                i+=1
                continue
    
    return original_data

def main():
    with open('Lz-w/compressed_data.txt', 'r') as file:
        content = file.read().strip()

    data = ast.literal_eval(content)
    original = lz_w_Decompression(data)
    
    with open('Lz-w/decompresses_data.txt', 'w') as file:
        file.write(original)

main()
