from tkinter import *
from tkinter import filedialog,ttk
from Float_Arithmetic import float_arithmetic_compression, float_arithmetic_decompression
import binascii

def open_file_to_text(widget, bin_flag):
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Binary files", "*.bin"), ("All files", "*.*")])
    if file:
        if bin_flag:
            with open(file, 'rb') as file:
                content = file.read()
                hex_content = binascii.hexlify(content).decode('utf-8')
                widget.delete(1.0, END)
                widget.insert(END, hex_content)
        else:
            with open(file, 'r') as file:
                content = file.read()
                widget.delete(1.0, END)
                widget.insert(END, content)

def save_text_from_widget(widget, extension):
    file = filedialog.asksaveasfile(defaultextension=extension,
                                    filetypes=[("Text files", "*.txt"), 
                                               ("All files", "*.*")])
    if file:
        content = widget.get(1.0, "end-1c")
        file.write(content)
        file.close()

def compress_text():
    float_arithmetic_compression(compression_input.get(1.0, "end-1c"));

    with open("Float_Arithmetic/compressed.txt", 'r') as file:
         compressed_output.delete(1.0, END)
         compressed_output.insert(END, file.read())
    
    with open("Float_Arithmetic/compressed.bin", 'rb') as file:
         hex_data = binascii.hexlify(file.read()).decode('utf-8')
         bin_compressed_output.delete(1.0, END)
         bin_compressed_output.insert(END, hex_data)

def decompress_text(bin_flag):
    if bin_flag:
        hex_string = bin_decompression_input.get(1.0, "end-1c")
        binary_data_bytes = binascii.unhexlify(hex_string)
        with open("Float_Arithmetic/compressed.bin", 'wb') as file:
            file.write(binary_data_bytes)
    else:
        with open("Float_Arithmetic/compressed.txt", 'w') as file:
            file.write(decompression_input.get(1.0, "end-1c"))
    
    float_arithmetic_decompression(bin_flag)
    
    with open("Float_Arithmetic/decompressed.txt", 'r') as file:
        if bin_flag:
            bin_decompressed_output.delete(1.0, END)
            bin_decompressed_output.insert(END, file.read())
        else:
            decompressed_output.delete(1.0, END)
            decompressed_output.insert(END, file.read())

    

# Main window
window = Tk()
window.title("Float Arithmetic Compression SIM")
window.config(background="#2E2E2E")
window.attributes('-fullscreen', True)

def exit_fullscreen(event=None):
    window.quit()
window.bind("<Escape>", exit_fullscreen)

# Notebook setup
notebook = ttk.Notebook(window)

compression_tab = Frame(window, bg="#2E2E2E")
decompression_tab = Frame(window, bg="#2E2E2E")
bin_decompression_tab = Frame(window, bg="#2E2E2E")

notebook.add(compression_tab, text="Compression")
notebook.add(decompression_tab, text="Decompression")
notebook.add(bin_decompression_tab, text="Binary Decompression")
notebook.pack(expand=True, fill="both")

# Compression Tab
Label(compression_tab, text="Input Text:", bg="#2E2E2E", fg="#FFFFFF").grid(row=0, column=0,rowspan=4, padx=10, pady=5, sticky=W)
compression_input = Text(compression_tab, height=10, width=80, bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
compression_input.grid(row=0, column=1,rowspan=4, padx=10, pady=5, sticky=N+S+E+W)

Button(compression_tab, text="Load Text File", command=lambda: open_file_to_text(compression_input,False), bg="#3C3F41", fg="#FFFFFF").grid(row=5, column=0,columnspan=2, padx=10, pady=5, sticky=W+E)
Button(compression_tab, text="Compress", command=compress_text, bg="#3C3F41", fg="#FFFFFF").grid(row=6, column=0,columnspan=2, padx=10, pady=5, sticky=W+E)

Label(compression_tab, text="Compressed Data:", bg="#2E2E2E", fg="#FFFFFF").grid(row=0, column=3,rowspan=2, padx=10, pady=5, sticky=W)
compressed_output = Text(compression_tab, height=10, width=80, state="normal", bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
compressed_output.grid(row=0, column=4,rowspan=2, padx=10, pady=5, sticky=W+E)

Label(compression_tab, text="Binary Data (Hex):", bg="#2E2E2E", fg="#FFFFFF").grid(row=3, column=3,rowspan=2, padx=10, pady=5, sticky=W+E)
bin_compressed_output = Text(compression_tab, height=10, width=80, state="normal", bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
bin_compressed_output.grid(row=3, column=4,rowspan=2, padx=10, pady=5, sticky=W+E)

Button(compression_tab, text="Save Compressed File", command=lambda: save_text_from_widget(compressed_output, ".txt"), bg="#3C3F41", fg="#FFFFFF").grid(row=5, column=3,columnspan=2, padx=10, pady=5, sticky=W+E)
Button(compression_tab, text="Save Binary File", command=lambda: save_text_from_widget(bin_compressed_output, ".bin"), bg="#3C3F41", fg="#FFFFFF").grid(row=6, column=3,columnspan=2, padx=10, pady=5, sticky=W+E)

# Decompression Tab
Label(decompression_tab, text="Input Compressed Text Data:", bg="#2E2E2E", fg="#FFFFFF").pack(anchor=W, padx=10, pady=5)
decompression_input = Text(decompression_tab, height=10, width=80, bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
decompression_input.pack(padx=10, pady=5)

Button(decompression_tab, text="Load Compressed File", command=lambda: open_file_to_text(decompression_input, False), bg="#3C3F41", fg="#FFFFFF").pack(pady=5)
Button(decompression_tab, text="Decompress", command=lambda: decompress_text(False), bg="#3C3F41", fg="#FFFFFF").pack(pady=5)

Label(decompression_tab, text="Decompressed Output:", bg="#2E2E2E", fg="#FFFFFF").pack(anchor=W, padx=10, pady=5)
decompressed_output = Text(decompression_tab, height=10, width=80, state="normal", bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
decompressed_output.pack(padx=10, pady=5)

# Binary Decompression Tab
Label(bin_decompression_tab, text="Input Compressed Binary Data:", bg="#2E2E2E", fg="#FFFFFF").pack(anchor=W, padx=10, pady=5)
bin_decompression_input = Text(bin_decompression_tab, height=10, width=80, bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
bin_decompression_input.pack(padx=10, pady=5)

Button(bin_decompression_tab, text="Load Compressed Binary File", command=lambda: open_file_to_text(bin_decompression_input, True), bg="#3C3F41", fg="#FFFFFF").pack(pady=5)
Button(bin_decompression_tab, text="Decompress", command=lambda: decompress_text(True), bg="#3C3F41", fg="#FFFFFF").pack(pady=5)

Label(bin_decompression_tab, text="Decompressed Output:", bg="#2E2E2E", fg="#FFFFFF").pack(anchor=W, padx=10, pady=5)
bin_decompressed_output = Text(bin_decompression_tab, height=10, width=80, state="normal", bg="#3C3F41", fg="#FFFFFF", insertbackground='white')
bin_decompressed_output.pack(padx=10, pady=5)
window.mainloop()
