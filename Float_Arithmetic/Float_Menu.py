from Float_Arithmetic import float_arithmetic_compression, float_arithmetic_decompression

file_data = ""
with open('Float_Arithmetic/Input.txt', 'r') as file:
    file_data = file.read()
while(True):
    print("Enter 1 if you want to compress the text in file called input.txt")
    print("Enter 2 if you want to input text to compress.")
    print("Enter 3 if you want to decompress the compressed data in file compressed_data")
    print("Enter 0 if you want to Exit")
    inp = int(input("Enter your choice: "))
    if inp == 1:
        float_arithmetic_compression(file_data)
    elif inp==2:
        float_arithmetic_compression(input("Input Text to be compressed: "))
    elif inp==3:
        float_arithmetic_decompression(True)
    else:
        break