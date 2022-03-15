"""
whisper.
By: Eliad Karni.

The feature decode messages which contained in the file "logo.jpg".

Used the help of the websites:
Binary read -> https://pythonguides.com/python-read-a-binary-file/
Ignore decode errors -> https://docs.python.org/3/library/codecs.html
"""


def get_a_whisper() -> str:
    """
    The function is a iterate generator which decode a whisper from the file "logo.jpg".
    1 message each time.
    :return: a decoded word from the file "logo.jpg".
    """
    with open('logo.jpg', 'br') as file_reader:
        decoded_word = ''
        char = file_reader.read(1)
        while char:
            char = char.decode(errors='ignore')
            if char is '!':
                if len(decoded_word) > 4:
                    yield decoded_word
                decoded_word = ''
            elif char.islower():
                decoded_word += char
            else:
                decoded_word = ''
            char = file_reader.read(1)


for word in get_a_whisper():
    print(word)
