def func(s):
    p_str_in = s
    
    if p_str_in is None:
        return None
    bits = ""
    for byteNo in range(len(p_str_in)):
        byteValue = ord(p_str_in[byteNo])
        for i in range(8):
            bit = "1" if byteValue & (1 << (7 - i)) else "0"
            bits += bit
    result = str(bits)
    return result
