from Standard_Huffman_compression import *
import pickle

def Standard_Huffman_decompression():
    Probabilities = []
    compressed_Data = []
    # with open('Standard_Huffman/compressed_data.txt', 'r') as file:
    #     for i, line in enumerate(file):
    #         if i == 0:
    #             Probabilities = eval(line.strip())
    #         else:
    #             stripped_line = line.strip()
    #             if stripped_line:
    #                 compressed_Data.append(stripped_line)
    with open('Standard_Huffman/compressed_data.bin', 'rb') as file:
        # Deserialize the compressed data using pickle
        compressed_data = pickle.load(file)

    # Extract probabilities and compressed data
    Probabilities = compressed_data[0]
    compressed_Data = compressed_data[1:]
    dic = mapping_characters(Probabilities)
    Data = ""
    for item in compressed_Data:
        for keys,Items in dic.items():
            if Items == item:
                Data+=keys
    with open('Standard_Huffman/decompressed_data.txt', 'w') as file:
        file.write(Data)



