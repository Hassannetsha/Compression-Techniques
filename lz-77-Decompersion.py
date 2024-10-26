def lz_77_Decompression(data:list):
    i = 0;
    original_data = ""
    while i<len(data):
        position = data[i];
        ctn = 0
        goBack = 0
        length = 0
        symbol = ""
        for ch in range(len(position)):
            num_buffer = ""
            if ctn==0 and position[ch].isdigit():
                num_buffer += position[ch]
                j = 1
                while ch+j<len(position) and position[ch+j].isdigit():
                    num_buffer += position[ch+j]
                    j+=1
                goBack = int(num_buffer)
                ctn+=1
            elif ctn==1 and position[ch].isdigit():
                num_buffer += position[ch]
                j = 1
                while ch+j<len(position) and position[ch+j].isdigit():
                    num_buffer += position[ch+j]
                    j+=1
                length = int(num_buffer)
                ctn+=1
            elif ctn==2 and (position[ch].isalpha()or position[ch].isspace() or position[ch] in ".!?/\\|@#$%^&*\()-_"):
                if((position[ch]=='N' or position[ch]=='n')and (position[ch+1]!='>' and position[ch+1]!=' ' and position[ch+1]!='\"')):
                    symbol = ""
                else:
                    symbol = position[ch]
                break
            elif ctn == 2 and position[ch] == '\\' and ch + 1 < len(position):
                if position[ch + 1] == 'n':
                    symbol = '\n'
                else:
                    symbol = position[ch] + position[ch + 1]
                break
        goBack = len(original_data) - goBack
        for ch in range(0,length):
            original_data+= original_data[goBack]
            goBack+=1
        original_data+=symbol
        i+=1
    return original_data

def main():
    with open('compressed.txt', 'r') as file:
        lines = file.readlines()
    
    lines = [lin.strip() for lin in lines]
    data = lz_77_Decompression(lines)
    
    with open('Normal.txt', 'w') as file:
        file.write(data)

main()
