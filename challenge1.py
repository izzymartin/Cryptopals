# Challenge 1 Convert hex to base64
from base64 import b64encode

# Converts hex to base64
def hexToBase64(hex_input):
    base64_input = b64encode(bytes.fromhex(hex_input)).decode()
    return base64_input


input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

input_base64 = hexToBase64(input_string)
assert input_base64 == expected