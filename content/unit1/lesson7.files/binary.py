def int_to_bin(num):
    return bin(num)[2:]

def str_to_bin(string):
    return [bin(ord(ch))[2:].zfill(8) for ch in string]

if __name__ == "__main__":
    print(int_to_bin(123))
    print(str_to_bin("123"))