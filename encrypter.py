from sys import argv

def run_collision_test(T):
    collisions = 0
    mapping = {}
    unique_symbols = []
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        x = ord(char) - 65
        c = chr(T(x) % 26 + 65)
        if not (c in mapping.keys()):
            mapping[c] = []
            mapping[c].append(char.capitalize())
        else:
            mapping[c].append(char.capitalize())
        if c in unique_symbols:
            collisions += 1
        else:
            unique_symbols.append(c)
    if collisions == 1:
        print("Your encryption method produced 1 collision:\n")
    elif collisions > 1:
        print("Your encryption method produced {} collisions:\n".format(collisions))
        for index, key in enumerate(mapping.keys()):
            print(str(index + 1) + ".")
            for elem in mapping[key]:
                print(elem + " --> " + key)
            print("")
    return collisions

def encrypt(message, T):
    encrypted_message = ""
    for char in message.upper():
        if not (ord(char) >= 65 and ord(char) <= 90):
            encrypted_message += char
        else:
            x = ord(char) - 65
            encrypted_message += chr(T(x) % 26 + 65)
    return encrypted_message

## f = ax + b, where a is relatively prime to 26 (else you get collisions)
f = lambda x : 3 * x + 2
num_collisions = run_collision_test(f)
if num_collisions == 0:
    print(encrypt(argv[1], f))
