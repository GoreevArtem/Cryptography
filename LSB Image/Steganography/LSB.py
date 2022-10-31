# LSB.py
from PIL import Image
import numpy as np


def Encode(src, msg, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size // n

    msg += "$r6@0"
    bin_msg = ''.join([format(ord(i), "08b") for i in msg])
    req_pixels = len(bin_msg)

    if req_pixels > total_pixels:
        print("[ERROR] Need larger file size")

    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + bin_msg[index], 2)
                    index += 1

        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("[INFO] Image Encoded Successfully")


def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size // n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

    msg = ""
    for i in range(len(hidden_bits)):
        if msg[-5:] == "$r6@0":
            break
        else:
            msg += chr(int(hidden_bits[i], 2))
    if "$r6@0" in msg:
        print("[INFO] Hidden Message:", msg[:-5])
    else:
        print("[ERROR] No Hidden Message Found")


def Menu():
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        message = input()
        print("Enter Destination Image Path")
        dest = input()
        print("[INFO] Encoding...")
        Encode(src, message, dest)

    elif func == '2':
        print("Enter Source Image Path")
        src = input()
        print("[INFO] Decoding...")
        Decode(src)

    else:
        print("[ERROR] Invalid option chosen")
