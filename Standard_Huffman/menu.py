from Standard_Huffman_decompression import *


while(True):
    print("Enter 1 if you want to compress the text in file called input.txt")
    print("Enter 2 if you want to decompress the compressed data in file compressed_data")
    print("Enter 0 if you want to Exit")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        Standard_Huffman_compression()
    elif inp==2:
        Standard_Huffman_decompression()
    else:
        break
    
    