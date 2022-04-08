import unittest
import namegen

class TestNamegen(unittest.TestCase):
    
    def test_vowels(self):
        self.assertEqual(type(namegen.vowels()),type("h"))

    def test_consonants(self):
        self.assertEqual(type(namegen.consonants()),type("h"))



if __name__ == '__main__':
    unittest.main()