def encode(string):
    cur = string[0]
    count = 0
    encoded = ""
    
    for c in string:
        if c == cur:
            count += 1
        else:
            encoded += cur + str(count)
            cur = c
            count = 1
            
    encoded += cur + str(count)

    return encoded


def decode(string):
    decoded = ''
    cur = string[0]
    num = string[1]

    for i in range(2, len(string)):
        if string[i] in "0123456789":
            num += string[i]
        else:
            decoded += cur * int(num)
            cur = string[i]
            num = ''
    decoded += cur * int(num)
    return decoded

line = input()

if line[0] == "E":
    print(encode(line[2:]))

else:
    print(decode(line[2:]))
