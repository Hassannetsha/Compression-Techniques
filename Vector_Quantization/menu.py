from Decompression import decompression
from Compression import compression
from PIL import Image


while(True):
    print("Enter 1 if you want to compress an image")
    print("Enter 2 if you want to decompress the image")
    print("Enter 0 if you want to Exit")
    inp = int(input("Enter your choice: "))
    
    # new_height = 7
    # new_width = 5
    # codeBookSize = 8
    if inp == 1:
        image_name = input("Enter the image path: ")
        new_height = int(input("Enter the block height: "))
        new_width = int(input("Enter the block width: "))
        codeBookSize = int(input("Enter the codeBook size: "))
        img = Image.open(image_name)
        img = img.convert('L')
        compression(img,new_height,new_width,codeBookSize)
    elif inp==2:
        decompression("Vector_Quantization/compressed_data.txt")
    else:
        break
    
    