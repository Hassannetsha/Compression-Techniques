from PIL import Image
import numpy as np
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
    return averages
def divide_into_blocks(image,block_height,block_width):
    h, w = image.shape
    blocks = []
    for i in range(0, h, block_height):
        for j in range(0, w, block_width):
            block = image[i:i+block_height, j:j+block_width]
            if block.shape == (block_height, block_width):
                blocks.append(block)
    return blocks
def go_nearest(img,dicIndex,dicPlace):
    for block in img:
        min_diff = float('inf')
        closest_index = None
        for index,average in dicIndex.items():
            diff  = absolute_difference(block,average)
            if diff < min_diff:
                min_diff = diff
                closest_index = index
        block_tuple = tuple(map(tuple, block))

        if block_tuple not in dicPlace[closest_index]:
            # ctn += 1
            dicPlace[closest_index].add(block_tuple)

            for index in dicPlace.keys():
                if index != closest_index:
                    dicPlace[index].discard(block_tuple)

    for key in dicPlace.keys():
        dicPlace[key] = [np.array(block) for block in dicPlace[key]]

def compression(img,block_height,block_width,codeBookSize):
    # ctn= 0
    h,w = img.shape
    img = divide_into_blocks(img,block_height,block_width)
    avg = calculate_avg(img,block_height,block_width)
    degree = (block_height,block_width)
    first_key = np.floor(avg)-np.ones(degree)
    second_key = np.ceil(avg)
    dicAverage = {0:first_key,1:second_key}
    dicPlace = {0:[],1:[]}
    for block in img:
        dicPlace[0].append(block)
    dicPlace = {
        key: {tuple(map(tuple, block)) for block in value}
        for key, value in dicPlace.items()
    }
    go_nearest(img,dicAverage,dicPlace)
    for index in dicAverage.keys():
        dicAverage[index] = calculate_avg(dicPlace[index],block_height,block_width)
    while len(dicAverage)<codeBookSize:
        key = 0
        dicTemp = {}
        for val in dicAverage.values():
            dicTemp[key] = np.floor(val)-np.ones(degree)
            key+=1
            dicTemp[key] = np.ceil(val)
            key+=1
        dicAverage = dicTemp
        for i in range(len(dicPlace),key):
            dicPlace[i] = []
        dicPlace = {
            key: {tuple(map(tuple, block)) for block in value}
            for key, value in dicPlace.items()
        }
        go_nearest(img,dicAverage,dicPlace)
        for index in dicAverage.keys():
            if dicPlace[index]:
                dicAverage[index] = calculate_avg(dicPlace[index],block_height,block_width)
    # for key in dicPlace:
    #     dicPlace[key] = [np.array(val, dtype=np.int64) for val in dicPlace[key]]
    # for l in range(len(img)):
    dicTemp = {
        tuple(map(tuple, value)) : key
        for key, value in dicAverage.items()
    }
    dicAverage = dicTemp
    compressed_list = []
    lis = []
    for block in img:
        for index, val in dicPlace.items():
            if any(np.array_equal(block, existing_block) 
                    for existing_block in val):
                lis.append(index)
                break
        if  len(lis)==(w//block_width):
            compressed_list.append(lis)
            lis = []
    with open('Vector_Quantaization/compressed_data.txt', 'w') as file:
        file.write(f'{compressed_list}\n{dicAverage}')
        # file.write(f'')
    
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
# compression(padded_array,new_height,new_width,codeBookSize)
arr = np.array([
    [1, 2, 7, 9, 4, 11],
    [3, 4, 6, 6, 12, 12],
    [4, 9, 15, 14, 9, 9],
    [10, 10, 20, 18, 8, 8],
    [4, 3, 17, 16, 1, 4],
    [4, 5, 18, 18, 5, 6]
])

compression(arr,2,2,4)

# padded_img = Image.fromarray(padded_array.astype(np.uint8))