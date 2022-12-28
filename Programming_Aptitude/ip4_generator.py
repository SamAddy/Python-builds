import random

def ip4_generator():
    octets = [random.randint(0, 255) for _ in range(4)]
    return ".".join(str(octet) for octet in octets)


print(ip4_generator())
