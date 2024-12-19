# from PIL import Image
# import numpy as np
# import json

# # Function to compress the image and save the codebook
# def compress_image(image_name, block_height, block_width, codebook_name, compressed_image_name):
#     # Load the grayscale image
#     img = Image.open(image_name)
#     img = img.convert('L')  # Convert to grayscale
#     img_array = np.array(img)

#     # Get image dimensions
#     height, width = img_array.shape

#     # Ensure the dimensions are divisible by the block size
#     padded_height = height + (block_height - height % block_height) % block_height
#     padded_width = width + (block_width - width % block_width) % block_width

#     # Padding the image manually with the last column and row
#     addition_width = padded_width - width
#     if addition_width > 0:
#         last_column = img_array[:, -1:]  # Extract the last column
#         padded_array = np.concatenate([img_array, np.tile(last_column, (1, addition_width))], axis=1)
#     else:
#         padded_array = img_array

#     addition_height = padded_height - height
#     if addition_height > 0:
#         last_row = padded_array[-1:, :]  # Extract the last row
#         padded_array = np.concatenate([padded_array, np.tile(last_row, (addition_height, 1))], axis=0)

#     # Initialize the codebook
#     codebook = []
#     quantized_array = padded_array.copy()

#     # Process blocks manually
#     for i in range(0, padded_height, block_height):
#         for j in range(0, padded_width, block_width):
#             # Extract the block
#             block = padded_array[i:i + block_height, j:j + block_width]
            
#             # Calculate the average value of the block
#             block_average = np.mean(block)
            
#             # Add the average value to the codebook
#             codebook.append(block_average)
            
#             # Replace the block with its average value
#             quantized_array[i:i + block_height, j:j + block_width] = block_average

#     # Save the quantized image
#     quantized_img = Image.fromarray(quantized_array.astype(np.uint8))
#     quantized_img.save(compressed_image_name)

#     # Save the codebook and dimensions to a file
#     data_to_save = {
#         "codebook": codebook,
#         "height": height,
#         "width": width,
#         "block_height": block_height,
#         "block_width": block_width
#     }
#     with open('Vector_Quantaization/compressed_data.txt', 'w') as file:
#         file.write(str(data_to_save))

#     print(f"Compression completed. Codebook saved to {codebook_name}, Quantized image saved to {compressed_image_name}.")

# # Function to decompress the image using the codebook
# def decompress_image( decompressed_image_name):
#     # Load the codebook and dimensions
#     with open('Vector_Quantaization/compressed_data.txt', 'r') as file:
#         data = file.read()
#     data = eval(data)
#     codebook = data["codebook"]
#     height = data["height"]
#     width = data["width"]
#     block_height = data["block_height"]
#     block_width = data["block_width"]

#     # Reconstruct the padded dimensions
#     padded_height = height + (block_height - height % block_height) % block_height
#     padded_width = width + (block_width - width % block_width) % block_width

#     # Reconstruct the image
#     reconstructed_array = np.zeros((padded_height, padded_width), dtype=np.uint8)
#     idx = 0
#     for i in range(0, padded_height, block_height):
#         for j in range(0, padded_width, block_width):
#             # Fill the block with the corresponding average value
#             reconstructed_array[i:i + block_height, j:j + block_width] = codebook[idx]
#             idx += 1

#     # Crop the image to the original dimensions
#     reconstructed_array = reconstructed_array[:height, :width]

#     # Save the decompressed image
#     decompressed_img = Image.fromarray(reconstructed_array)
#     decompressed_img.save(decompressed_image_name)
#     print(f"Decompression completed. Decompressed image saved to {decompressed_image_name}.")

# # Example Usage
# image_name = '1.jpg'
# block_height = 2
# block_width = 2
# codebook_name = 'codebook.json'
# compressed_image_name = 'quantized_image.jpg'
# decompressed_image_name = 'decompressed_image.jpg'

# # Compress the image
# compress_image(image_name, block_height, block_width, codebook_name, compressed_image_name)

# # Decompress the image
# decompress_image(decompressed_image_name)
