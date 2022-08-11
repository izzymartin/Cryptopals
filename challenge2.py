# Challenge 2 Fixed XOR
#   https://www.cryptopals.com/sets/1/challenges/2
from operator import xor
from base64 import b64encode

# Set input strings
input_string = "1c0111001f010100061a024b53535009181c"
xor_input = "686974207468652062756c6c277320657965"
expected = "746865206b696420646f6e277420706c6179"

# Convert inputs to bytes to work with
decoded_input = bytes.fromhex(input_string)
decoded_xor = bytes.fromhex(xor_input)
output = ""
# XOR bytes, convert to hex, strip off 0x from hex format, then append to output
for index, bit in enumerate(decoded_input):
    output += str(hex(bit ^ decoded_xor[index])[2:])

assert output == expected