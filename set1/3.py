def single_byte_xor(a, c):
    a = bytearray(a)

    b = []

    for i in range(len(a)):
        b.append(chr(ord(c) ^ a[i]))

    return ''.join(b)

if __name__ == "__main__":
    c = 'x'
    a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode("hex")
    print single_byte_xor(a, c)
