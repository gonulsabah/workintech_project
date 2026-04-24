pass  # YOUR CODE HERE
from .mapping import MORSE
from .encoder import encode

MORSE_REVERSE = {value: key for key, value in MORSE.items()}

def decode(morse_text):
    return " ".join(decode_word(morse_word) for morse_word in morse_text.split("|"))


def decode_word(morse_word):
    return "".join(MORSE_REVERSE[morse_letter] for morse_letter in morse_word.split())

if __name__ == "__main__":
    EXAMPLE = "abc"
    EXAMPLE_MORSE = encode(EXAMPLE)
    DECODED_TEXT = decode_word(EXAMPLE_MORSE)
    print(f"Encoded word '{EXAMPLE}' into '{EXAMPLE_MORSE}'")
    print(f"    and decoded back into plain text: '{DECODED_TEXT}'")

    EXAMPLE = "abc ABC"
    EXAMPLE_MORSE = encode(EXAMPLE)
    DECODED_TEXT = decode(EXAMPLE_MORSE)
    print(f"Encoded word '{EXAMPLE}' into '{EXAMPLE_MORSE}'")
    print(f"    and decoded back into plain text: '{DECODED_TEXT}'")