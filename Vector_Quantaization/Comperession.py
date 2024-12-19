# #1. a gray scale image file
# # 2. the block size
# # 3. code book size
# from decimal import Decimal, getcontext
# [[[1,2],[3,4]],[]]
from PIL import Image
import numpy as np
import math
# getcontext().prec = 10000
def absolute_difference(a, b):
    return np.sum(np.abs(a - b))
def calculate_avg(padded_array,block_height,block_width):
    degree = (block_height,block_width)
    averages = np.zeros(degree)
    no_blocks = len(padded_array)
    for i in range(block_height):
        for j in range(block_width):
            for l in range(0,len(padded_array)):
                averages[i][j] += padded_array[l][i][j]
            averages[i][j]/=no_blocks

    # Calculate the average for each block
    # for i in range(block_height):
    #     for j in range(block_width):
    #             averages[i][j] /= no_blocks
    return averages
def divide_into_blocks(image,block_height,block_width):
    """Divides an image into non-overlapping blocks of size block_size x block_size."""
    h, w = image.shape
    blocks = []
    for i in range(0, h, block_height):
        for j in range(0, w, block_width):
            block = image[i:i+block_height, j:j+block_width]
            if block.shape == (block_height, block_width):
                blocks.append(block)
    return blocks
# def go_nearest():
    
def compression(img,new_height,new_width,block_height,block_width,codeBookSize):
    cnt= 0
    img = divide_into_blocks(img,block_height,block_width)
    avg = calculate_avg(img,block_height,block_width)
    degree = avg.shape

# Calculate first_key and second_key
    first_key = tuple(np.floor(avg).flatten()) - tuple(np.ones(degree).flatten())
    second_key = tuple(np.ceil(avg).flatten())

# Create the dictionary with hashable keys
    dic = {first_key: [], second_key: []}
    while True:
        break
image_name = '1.jpg'
img = Image.open(image_name)
img = img.convert('L')

old_width, old_height = img.size

new_height = 7
new_width = 5

addition_height = (new_height - (old_height % new_height)) % new_height
addition_width = (new_width - (old_width % new_width)) % new_width

img_array = np.array(img)

if addition_width > 0:
    last_column = img_array[:, -1:]  # Extract the last column
    padded_array = np.concatenate([img_array, np.tile(last_column, (1, addition_width))], axis=1)
else:
    padded_array = img_array

if addition_height > 0:
    last_row = padded_array[-1, :].reshape(1, -1)  # Extract the last row
    padded_array = np.concatenate([padded_array, np.tile(last_row, (addition_height, 1))], axis=0)
codeBookSize = 8
compression(padded_array,old_height+addition_height,old_width + addition_width,new_height,new_width,codeBookSize)
# padded_img = Image.fromarray(padded_array.astype(np.uint8))


# padded_img.save('compressed_image.jpg')
# from PIL import Image
# import numpy as np

# # Load the grayscale image
# image_name = '1.jpg'
# img = Image.open(image_name)
# img  = img.convert('L')  # Convert to grayscale
# img_array = np.array(img)

# # Define block size
# block_height = 8
# block_width = 8

# # Get image dimensions
# height, width = img_array.shape

# # Ensure the dimensions are divisible by the block size
# padded_height = height + (block_height - height % block_height) % block_height
# padded_width = width + (block_width - width % block_width) % block_width
# addition_width = padded_width - width
# if addition_width > 0:
#     last_column = img_array[:, -1:]  # Extract the last column
#     padded_array = np.concatenate([img_array, np.tile(last_column, (1, addition_width))], axis=1)
# else:
#     padded_array = img_array
# addition_height = padded_height - height
# if addition_height > 0:
#     last_row = padded_array[-1, :].reshape(1, -1)  # Extract the last row
#     padded_array = np.concatenate([padded_array, np.tile(last_row, (addition_height, 1))], axis=0)
# # padded_image = np.pad(
# #     img_array,
# #     ((0, padded_height - height), (0, padded_width - width)),
# #     mode='edge'
# # )
# # padded_image = Image.fromarray(padded_array.astype(np.uint8))
# # Perform vector quantization
# codebook = []
# quantized_image = padded_array.copy()

# # Process blocks manually
# for i in range(0, padded_height, block_height):
#     for j in range(0, padded_width, block_width):
#         # Extract the block
#         block = padded_array[i:i + block_height, j:j + block_width]
        
#         # Calculate the average value of the block
#         block_average = np.mean(block)
#         codebook.append(block_average)
#         # Replace the block with its average value
#         quantized_image[i:i + block_height, j:j + block_width] = block_average

# # Convert the quantized image back to a PIL image for visualization
# quantized_img = Image.fromarray(quantized_image.astype(np.uint8))

# # Save or display the image
# quantized_img.save('quantized_image.jpg')
# # quantized_img.show()
# print("Codebook:", codebook)