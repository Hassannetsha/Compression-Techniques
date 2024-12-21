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
def go_nearest(img,dicIndex,dicPlace,ctn):
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
            ctn += 1
            dicPlace[closest_index].add(block_tuple)

            for index in dicPlace.keys():
                if index != closest_index:
                    dicPlace[index].discard(block_tuple)

    for key in dicPlace.keys():
        dicPlace[key] = [np.array(block) for block in dicPlace[key]]
    return ctn

def compression(img,block_height,block_width,codeBookSize):
    old_width, old_height = img.size
    addition_height = (block_height - (old_height % block_height)) % block_height
    addition_width = (block_width - (old_width % block_width)) % block_width

    img = np.array(img)

    if addition_width > 0:
        last_column = img[:, -1:]  # Extract the last column
        padded_array = np.concatenate([img, np.tile(last_column, (1, addition_width))], axis=1)
    else:
        padded_array = img

    if addition_height > 0:
        last_row = padded_array[-1, :].reshape(1, -1)  # Extract the last row
        padded_array = np.concatenate([padded_array, np.tile(last_row, (addition_height, 1))], axis=0)
    img = padded_array
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
    ctn = 0
    ctn = go_nearest(img,dicAverage,dicPlace,ctn)
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
        ctn = go_nearest(img,dicAverage,dicPlace,ctn)
        for index in dicAverage.keys():
            if dicPlace[index]:
                dicAverage[index] = calculate_avg(dicPlace[index],block_height,block_width)
    min_ctn = 100
    while ctn>=min_ctn:
        dicPlace = {
            key: {tuple(map(tuple, block)) for block in value}
            for key, value in dicPlace.items()
        }
        prev_ctn = ctn
        ctn = 0
        ctn = go_nearest(img,dicAverage,dicPlace,ctn)
        min_ctn = min(min_ctn,ctn)
        if prev_ctn<ctn:
            break
        for index in dicAverage.keys():
            if dicPlace[index]:
                dicAverage[index] = calculate_avg(dicPlace[index],block_height,block_width)
    dicTemp = {
        tuple(map(tuple, value)) : key
        for key, value in dicAverage.items()
    }
    dicAverage = dicTemp
    compressed_list = []
    lis = []
    dicPlace_sets = {index: {tuple(map(tuple, val)) for val in dicPlace[index]} for index in dicPlace}
    for block in img:
        for index, val_set in dicPlace_sets.items():
            block_tuple = tuple(map(tuple, block))  # Convert the block to a tuple
            if block_tuple in val_set:  # Check for membership in the set
                lis.append(index)
                break
        if len(lis) == (w // block_width):
            compressed_list.append(lis)
            lis = []
    with open('Vector_Quantization/compressed_data.txt', 'w') as file:
        file.write(f'{compressed_list}\n{dicAverage}')
    



# compression(img,new_height,new_width,codeBookSize)
# arr = np.array([
#     [1, 2, 7, 9, 4, 11],
#     [3, 4, 6, 6, 12, 12],
#     [4, 9, 15, 14, 9, 9],
#     [10, 10, 20, 18, 8, 8],
#     [4, 3, 17, 16, 1, 4],
#     [4, 5, 18, 18, 5, 6]
# ])

# compression(arr,2,2,4)