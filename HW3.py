import string

alphabet = " "+string.ascii_lowercase 

positions = dict(zip(alphabet,list(range(0,27,1))))

message = "hi my name is caesar"

def encoding(message,key=1):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    
    encoded_string = "".join(encoding_list)
    
    return encoded_string

'''
def encoding(message):

    encoded_message = ""

    for i, char in enumerate(message):
        result = (positions[char]+1) % 27
        encoded_message += alphabet[result]
    return encoded_message
'''

encoded_message = encoding(message,key = 3)
    
decoded_message = encoding(encoded_message,-3)

print(encoded_message)

print(decoded_message)