# Challenge 1: The Vigenère Cipher for International Women's Day Wishes

## Objective

Your task is to implement two functions, encrypt_vigenere and decrypt_vigenere, which respectively encrypt and decrypt a plaintext message using the Vigenère cipher with a provided keyword. The key aspect of this cipher is polyalphabetic substitution, where each letter in the plaintext is shifted along the alphabet based on a corresponding letter in the keyword.
## Key Requirements

    Alphabetic Sensitivity: Your functions should only process alphabetic characters (both uppercase and lowercase). All non-alphabetic characters, including numbers, spaces, punctuation, and symbols, must remain unchanged in the output.
    Case Preservation: The case of each alphabetic character must be preserved. Uppercase letters remain uppercase, and lowercase letters remain lowercase after encryption or decryption.
    Keyword Repetition: The keyword is repeated or truncated to match the length of the plaintext for encryption. For decryption, the same keyword is used to reverse the encryption process.

## Guidelines for Implementation

    Encryption Function (encrypt_vigenere):
        Input: plaintext (string), keyword (string).
        Process: Encrypt only the alphabetic characters of the plaintext using the Vigenère cipher, leaving numbers and symbols unchanged.
        Output: The encrypted message as a string.

    Decryption Function (decrypt_vigenere):
        Input: ciphertext (string), keyword (string).
        Process: Decrypt only the alphabetic characters of the ciphertext using the Vigenère cipher, leaving numbers and symbols unchanged.
        Output: The decrypted message (original plaintext) as a string.

## Special Considerations

    When encountering non-alphabetic characters in the plaintext or ciphertext, your functions should include these characters in the output without any modification.
    The encryption and decryption processes should seamlessly handle texts of any length, ensuring that the keyword is appropriately repeated or truncated to align with the length of the alphabetic characters in the text.
    Pay careful attention to the indexing and shifting mechanisms employed in the Vigenère cipher, especially the wrapping of alphabet characters (e.g., shifting 'Z' forward should loop back around to 'A')

Example 1:
- Input: text = "Happy Women's Day!", keyword = "Flowers"
- Output: "Mldlc Ngrpb'o Hrq!"

Example 2:
- Input: text = "Celebrate women's achievements!", keyword = "March"
- Output: "Oecgidakg damvp'z mcyklhedgufs!"

Example 3:
- Input: text = "1234567890 !@#$%^&*()", keyword = "Digits"
- Output: text = "1234567890 !@#$%^&*()"

## Getting Started
- Use this command to clone this repository to start working
```bash
git clone https://github.com/kiloMIA/femctf-python-tasks.git
```

## Testing: 
- To test your code, simply write:  
```bash
python test_vigenere.py
```
