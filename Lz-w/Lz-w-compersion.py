def lz_W_Compression(Data):
    compressed_data  = []
    Dictionary = {}
    start = 128
    i = 0
    while i <  len(Data):
        letters = Data[i]
        last_place = ord(letters)
        place = ord(letters)
        while ((letters in Dictionary) or (place<128 and len(letters)>=1)):
            i+=1
            place = start
            if letters in Dictionary:
                last_place = Dictionary[letters]
            if i>=len(Data):
                break
            letters+=Data[i]
            
        compressed_data.append(last_place)
        Dictionary[letters] = place
        start+=1
    return compressed_data
            
        




# print(ord(a))
with open('Lz-w/Input.txt', 'r') as file:
    Data = file.read()


compressed_data = lz_W_Compression(Data)


with open('Lz-w/compressed_data.txt', 'w') as file:
    file.write(f'{compressed_data}')