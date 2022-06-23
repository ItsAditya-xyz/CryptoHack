import base64
hexString = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytestFromHex  = bytes.fromhex(hexString)
print(base64.b64encode(bytestFromHex))
