import struct
from hid_code import azerty_hid_codes

input_string = input("Input string: ")

for wanted_char in list(input_string):
    modif, key = azerty_hid_codes[wanted_char]
    raw = struct.pack("BBBBL", modif, 0x00, key, 0x00, 0x00000000)
    with open("/dev/hidg0", "wb") as f:
        f.write(raw) # press key
        f.write(struct.pack("Q", 0)) # release key
