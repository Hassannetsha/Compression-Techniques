def lz_77_Compression(data, s_buffer_size, la_buffer_size):
    la_position = 0
    s_buffer = ""
    compressed_data = list()

    while la_position < len(data):
        position = 0
        length = 0

        la_buffer = data[la_position:la_position+la_buffer_size]
        longest_match = la_buffer[0]
        index = s_buffer.rfind(longest_match)

        while index != -1 and (la_position + length) < len(data):
            length += 1
            position = len(s_buffer) - index
            longest_match = la_buffer[:length+1]
            index = s_buffer.rfind(longest_match)

        compressed_data.append( f"({position},{length},{longest_match[-1]})")

        s_buffer += data[la_position:la_position + length + 1]
        s_buffer = s_buffer[-s_buffer_size:]
        la_position += length + 1
    return compressed_data
def lz_77_Compression(data, s_buffer_size, la_buffer_size):
    la_position = 0
    s_buffer = ""
    compressed_data = list()

    while la_position < len(data):
        position = 0
        length = 0
        move_len = 0
        la_buffer = data[la_position:la_position+la_buffer_size]
        longest_match = la_buffer[0]
        index = s_buffer.rfind(longest_match)
        temp = len(s_buffer) - index
        while index != -1 and (la_position + length) < len(data):
            length += 1
            move_len = length
            if temp<position and position!=0:
                position = temp
            else:
                break
            longest_match = la_buffer[:length+1]
            index = s_buffer.rfind(longest_match)
        
        compressed_data.append( f"({position},{length},{longest_match[-1]})")

        s_buffer += data[la_position:la_position + length + 1]
        s_buffer = s_buffer[-s_buffer_size:]
        la_position += length + 1
    return compressed_data

def main():
    with open('baseD.txt', 'r') as file:
        d = file.read()

    s = 12
    la = 11
    # c = ['(5,10,NULL)','(5,1,23)']
    c = lz_77_Compression(d, s, la)

    with open('baseC.txt', 'w') as file:
        for tag in c:
            tag = tag.strip('()').split(",")

            file.write(f'<{tag[0]},{tag[1]},{"NUll" if tag[2] == "NULL" else f'"{tag[2]}"'}>\n')


main()