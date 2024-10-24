def lz_77_Compression(data, s_buffer_size, la_buffer_size):
    la_position = 0
    s_buffer = ""
    compressed_data = list()

    while la_position < len(data):
        position = 0
        length = 0

        la_buffer = data[la_position:la_position+la_buffer_size]
        longest_match = la_buffer[0]
        index = s_buffer.find(longest_match)

        while index != -1 and (la_position + length) < len(data):
            length += 1
            position = index
            longest_match = la_buffer[:length]
            index = s_buffer.find(longest_match)

        compressed_data.append( f"({position},{length},{data[la_position+length]})")

        s_buffer += data[la_position:la_position + length + 1]
        s_buffer = s_buffer[-s_buffer_size:]
        la_position += length + 1


    return compressed_data

def main():
    d = "ABAABABAABBBBBBBBBBBBA"
    s = 12
    la = 11
    c = lz_77_Compression(d, s, la)
    print(c)


main()