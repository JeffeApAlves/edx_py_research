import string
import time

alphabet = " "+string.ascii_lowercase 

positions = dict(zip(alphabet,list(range(0,27,1))))

message = "teste um dois tres quatro cinco"

def encoding(message,key=1):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    
    encoded_string = "".join(encoding_list)
    
    return encoded_string


def encoding2(message,key=1):

    encoded_string = ""

    for i, char in enumerate(message):
        result = (positions[char]+1) % 27
        encoded_string += alphabet[result]
    return encoded_string

t0 = time.time()

encoded_message = encoding(message,key = 3)
decoded_message = encoding(encoded_message,-3)

t1 = time.time()

print(t1-t0)

print(encoded_message)
print(decoded_message)