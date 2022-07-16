from sys import argv

def inverse_mod_n(val, modulus):
    mod_map = {}     
    dividend = modulus
    divisor = val
    quotient = int(dividend / divisor)
    remainder = dividend % divisor
    mod_map[remainder] = -quotient * divisor
    if remainder == 1:
        return int((divisor - (divisor - 1) * mod_map[remainder]) / val) % modulus
    while remainder != 1:
        dividend = divisor
        divisor = remainder
        quotient, remainder = int(dividend / divisor), dividend % divisor
        mod_map[remainder] = (mod_map[dividend] if dividend in mod_map.keys() else dividend) - mod_map[divisor] * quotient
    if dividend in mod_map.keys():
        return int((mod_map[dividend] - mod_map[divisor] * quotient) / val) % modulus 
    else:
        return int((dividend - mod_map[divisor] * quotient) / val) % modulus

def decrypt_affine(message, word_list, threshold = 3):
    factors = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for factor in factors:
        for k in range(0, 26):
            string = ""
            for char in message.upper():
                if not (ord(char) >= 65 and ord(char) <= 90):
                    string += char
                else:
                    x = ord(char) - 65
                    string += chr((inverse_mod_n(factor, 26) * (x - k)) % 26 + 65)
            common_words_found = 0
            for word in string.split(" "):
                if word in word_list:
                    common_words_found += 1 
                if common_words_found >= threshold:
                    print(string)
                    break

f = open("./data/common_words.txt", "r")
words = map(lambda x : x.upper(), f.read().split("\n"))
decrypt_affine(argv[1], list(words))
