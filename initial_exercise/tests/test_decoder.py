import unittest
import morse.decoder as decoder

class TestDecoder(unittest.TestCase):
    def test_decode_single_letter(self):
        self.assertEqual(decoder.decode(".-"), "A")

    def test_decode_multiple_letters(self):
        self.assertEqual(decoder.decode(".... .."), "HI")

    def test_decode_with_pipe_separator(self):
        self.assertEqual(decoder.decode(".... ..|--. ..- -.-- ..."), "HI GUYS")

    def test_decode_hey_jude(self):
        morse = ".... . -.--|.--- ..- -.. .|-.. --- -. -|-- .- -.- .|.. -|-... .- -.."
        text = "HEY JUDE DONT MAKE IT BAD"
        self.assertEqual(decoder.decode(morse), text)

    def test_decode_word(self):
        self.assertEqual(decoder.decode_word(".-"), "A",
                         msg="Did you code the `decode_word` function? If not, refactor your code.")


if __name__ == "__main__":
    unittest.main()