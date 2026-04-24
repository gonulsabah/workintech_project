import unittest
from morse.encoder import encode, encode_word

class TestEncoder(unittest.TestCase):
    def test_encode_simple_letter(self):
        self.assertEqual(encode("a"), ".-")
    
    def test_case_insensitivity(self):
        self.assertEqual(encode("b"), "-...")
        self.assertEqual(encode("b"), encode("B"))
    
    def test_space_between_letters(self):
        self.assertEqual(encode("hi"), ".... ..")

    def test_pipe_between_words(self):
        self.assertEqual(encode("hi all"), ".... ..|.- .-.. .-..")
    
    def test_remove_punctuation(self):
        self.assertEqual(encode("hello, world"), ".... . .-.. .-.. ---|.-- --- .-. .-.. -..")
    
    def test_encode_hey_jude(self):
        text = "Hey Jude, don't make it bad"
        morse = ".... . -.--|.--- ..- -.. .|-.. --- -. -|-- .- -.- .|.. -|-... .- -.."
        self.assertEqual(encode(text), morse)
        
if __name__ == "__main__":
    unittest.main()