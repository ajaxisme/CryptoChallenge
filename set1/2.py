def xor_strings(a, b):
    a = bytearray(a)
    b = bytearray(b)

    c = []

    for i in range(len(a)):
        c.append(chr(a[i] ^ b[i]))
    
    return "".join(c).encode("hex")

if __name__ == "__main__":
    a = "1c0111001f010100061a024b53535009181c".decode("hex")
    b = "686974207468652062756c6c277320657965".decode("hex")

    print xor_strings(a, b)
