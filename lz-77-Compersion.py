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
def lz_77_adjusted_Compression(data, s_buffer_size, la_buffer_size):
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
        s_temp = ""
        while index != -1 and (la_position + length) < len(data):
            length += 1
            if temp <= position or position==0:
                position = temp
            else:
                break
            if index != -1:
                s_temp = longest_match
                move_len = length
            longest_match = la_buffer[:length+1]
            index = s_buffer.rfind(longest_match)
            temp = len(s_buffer) - index
        s_temp = s_temp[0:move_len] + longest_match[0:len(longest_match)-move_len]
        while s_temp == longest_match and len(s_temp)!=1 and len(longest_match)<la_buffer_size and (la_position + length) < len(data):
            longest_match = la_buffer[:length+1]
            length += 1
            s_temp = s_temp[0:move_len] + longest_match[0:len(longest_match)-move_len]
        length = len(longest_match) - 1
        compressed_data.append( f"({position},{length},{longest_match[-1]})")

        s_buffer += data[la_position:la_position + length+1]
        s_buffer = s_buffer[-s_buffer_size:]
        la_position += length + 1
    return compressed_data

def main():
    with open('Normal.txt', 'r') as file:
        d = file.read()

    s = 12
    la = 11
    # c = ['(5,10,NULL)','(5,1,23)']
    c = lz_77_Compression(d, s, la)

    with open('compressed.txt', 'w') as file:
        for tag in c:
            tag = tag.strip('()').split(",")

            file.write(f'<{tag[0]},{tag[1]},{"NUll" if tag[2] == "" else f'"{tag[2]}"'}>\n')


main()