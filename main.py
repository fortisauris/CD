"""
Experimental program to study posibilieties of Causable Deniability
problem in Cryptography.
"""

def add_byte(data: bytes, b: int) -> bytes:
    data = bytearray(data)
    data.append(b)
    print(data)
    return bytes(data)

if __name__ == "__main__":
    msg = bytes("lekvar", encoding = "ascii")
    pwd = bytes("blbost", encoding = "ascii")
    print(msg)

    result = list()
    for i in range(0,len(msg)):
        print(msg[i], pwd[i])
        zasifrovane_pismeno = msg[i] ^ pwd[i]
        result.append(zasifrovane_pismeno)

    print(result)
    ba = bytearray(result)
    print(ba)
    print(bytes(ba))

    result = list()
    for i in range(0,len(msg)):
        print(ba[i], pwd[i])
        odsifrovane_pismeno = ba[i] ^ pwd[i]
        result.append(odsifrovane_pismeno)

    print(result)
