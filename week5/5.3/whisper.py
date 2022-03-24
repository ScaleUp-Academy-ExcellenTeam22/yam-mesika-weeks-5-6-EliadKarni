"""
whisper.
By: Eliad Karni.
The code decode messages which contained in the file "logo.jpg".
Used the help of the websites:
Binary read -> https://pythonguides.com/python-read-a-binary-file/
Ignore decode errors -> https://docs.python.org/3/library/codecs.html
"""


def get_a_whisper() -> str:
    """
    The function is a generator which decode a whisper from the file "logo.jpg".
    One message each call.
    :return: a decoded word from the file "logo.jpg".
    """
    with open("logo.jpg", "br") as file_reader:
        decoded_word = ""
        for line in file_reader:
            for char in line.decode(errors="ignore"):
                if char == "!":
                    if len(decoded_word) > 4:
                        yield decoded_word
                    decoded_word = ""
                elif char.islower():
                    decoded_word += char
                else:
                    decoded_word = ""


if __name__ == "__main__":
    for word in get_a_whisper():
        print(word)
