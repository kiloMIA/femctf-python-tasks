import unittest
from vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_decrypt_cycle(self):
        test_cases = [
        {"plaintext": "Happy Women's Day!", "keyword": "Flowers"},  
        {"plaintext": "Celebrate women's achievements!", "keyword": "March"},  
        {"plaintext": "Here's to strong women: may we know them, may we be them, may we raise them.", "keyword": "Strength"},  
        {"plaintext": "1234567890 !@#$%^&*()", "keyword": "Digits"},  
        {"plaintext": "Consistency is the key to success.", "keyword": "Persistence"},  
        {"plaintext": "abcdefghijklmnopqrstuvwxyz", "keyword": "Alphabet"},  
        {"plaintext": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "keyword": "Alphabet"},  
        {"plaintext": "Sphinx of black quartz, judge my vow.", "keyword": "Pangram"},  
        {"plaintext": "!@#$%^&*()_+{}:<>?[];',./", "keyword": "Symbols"},  
        {"plaintext": "Still love her", "keyword":"honeymints"},
        {"plaintext": "The quick brown fox jumps over the lazy dog.", "keyword": "PangramKeyword"},  
        {"plaintext": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "keyword": "LoremIpsum"}
    ]

        for case in test_cases:
            encrypted_text = encrypt_vigenere(case["plaintext"], case["keyword"])
            decrypted_text = decrypt_vigenere(encrypted_text, case["keyword"])

            self.assertEqual(decrypted_text, case["plaintext"], f"Decryption failed for keyword '{case['keyword']}' - expected '{case['plaintext']}', got '{decrypted_text}'")

if __name__ == "__main__":
    unittest.main()
