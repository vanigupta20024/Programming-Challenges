# The Noob method (This is not preferable in case of security)

# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import base64

# input will be given in hex
string_in_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# to convert from hex to bytes
byte_string = bytes.fromhex(string_in_hex)

# encode bytes to base64 bytes
base64_string = base64.b64encode(byte_string)

# returning the base64 string
print(base64_string.decode())
