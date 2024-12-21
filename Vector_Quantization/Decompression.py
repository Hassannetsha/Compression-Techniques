import numpy as np
from PIL import Image

def decompression(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
        
    encoded_image = eval(data[0])  

    codebook = eval(data[1])
    reversed_dicAverage = {
    key: np.array([list(row) for row in value]) 
    for value, key in codebook.items()
    }
    
    reconstructed_image = []

    for block in encoded_image:
        lis = []
        for num in block:
            lis.append(reversed_dicAverage[num])
        reconstructed_image.append(lis)
    
    blockheight, blockwidth = reconstructed_image[0][0].shape
    original_image_height = len(reconstructed_image) * blockheight
    original_image_width = len(reconstructed_image[0]) * blockwidth

    full_image = np.zeros((original_image_height, original_image_width), dtype=np.uint8)

    for i, row_blocks in enumerate(reconstructed_image):
        for j, block in enumerate(row_blocks):
            start_row = i * blockheight
            start_col = j * blockwidth
            full_image[start_row:start_row + blockheight, start_col:start_col + blockwidth] = block

    img = Image.fromarray(full_image)
    img.save("decompressed_img.jpg")
