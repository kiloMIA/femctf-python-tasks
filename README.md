# Challenge 1: The Vigenère Cipher for International Women's Day Wishes

## Objective

Your task is to implement two functions, encrypt_vigenere and decrypt_vigenere, which respectively encrypt and decrypt a plaintext message using the Vigenère cipher with a provided keyword. The key aspect of this cipher is polyalphabetic substitution, where each letter in the plaintext is shifted along the alphabet based on a corresponding letter in the keyword.
## Key Requirements

    Alphabetic Sensitivity: Your functions should only process alphabetic characters (both uppercase and lowercase). All non-alphabetic characters, including numbers, spaces, punctuation, and symbols, must remain unchanged in the output.
    Case Preservation: The case of each alphabetic character must be preserved. Uppercase letters remain uppercase, and lowercase letters remain lowercase after encryption or decryption.
    Keyword Repetition: The keyword is repeated or truncated to match the length of the plaintext for encryption. For decryption, the same keyword is used to reverse the encryption process.

## Guidelines for Implementation

### Encryption Function (encrypt_vigenere):

    Input: Accept two inputs - the plaintext string to be encrypted and the keyword. Both should be strings.
        plaintext: The message you wish to encrypt. It can contain alphabetic characters, numbers, spaces, punctuation, and symbols.
        keyword: The word used to encrypt the plaintext. It should ideally be an alphabetic string, as non-alphabetic characters are not processed.

    Process:
        Prepare the Alphabet: Define an alphabet string containing all uppercase letters (A-Z). This will be used to find the index of each letter for the shift operation.
        Normalize the Keyword: Ensure the keyword is of the same length as the plaintext. If it is shorter, repeat it until it matches the length of the plaintext. Only alphabetic characters in the plaintext count towards the length matching.
        Encrypt Each Letter: For each alphabetic character in the plaintext, find its corresponding letter in the keyword. Use the position of the keyword letter in the alphabet as the number of positions to shift the plaintext letter.
            If the plaintext character is not alphabetic (e.g., number, punctuation), leave it unchanged.
            Preserve the case of each letter. Use the alphabet string for case conversion if needed.
        Handle Alphabet Wraparound: Ensure that the encryption wraps around the alphabet. For example, shifting 'Z' by 1 results in 'A'.

    Output: Return the encrypted message as a string, maintaining the original case and leaving non-alphabetic characters unchanged.

### Decryption Function (decrypt_vigenere):

    Input: Accept two inputs - the ciphertext string to be decrypted and the same keyword used for encryption.
        ciphertext: The encrypted message.
        keyword: The word used to decrypt the ciphertext, identical to the one used for encryption.

    Process:
        Prepare the Alphabet: Use the same alphabet string as in the encryption process.
        Normalize the Keyword: Adjust the keyword to match the length of the ciphertext, considering only alphabetic characters.
        Decrypt Each Letter: For each alphabetic character in the ciphertext, reverse the encryption process using the keyword's corresponding letter position to shift back to the original letter.
            Non-alphabetic characters should remain unchanged.
            Preserve the case of each alphabetic character.
        Handle Alphabet Wraparound: Ensure that the decryption correctly wraps around the alphabet. For example, shifting 'A' back by 1 results in 'Z'.

    Output: Return the decrypted message as a string, with the case preserved and non-alphabetic characters left as is.

## Special Notes:

    Case Sensitivity: The functions should accurately handle both uppercase and lowercase letters, ensuring that the case of the plaintext is preserved in the ciphertext and vice versa.
    Non-Alphabetic Characters: Spaces, numbers, punctuation, and symbols must be ignored by the encryption and decryption processes but should be included in the final output in their original positions.



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

# Challenge: Hash and Unzip for the Flag

## Objective

Your task is to implement a simple hashing function based on the Division-Remainder Method and use this hash to decrypt a password-protected zip file. The plaintext "ClaraZetkin" must be hashed, and the resulting hash value will serve as the password to unlock the zip file containing the challenge flag. This task will test your ability to apply hashing concepts in a practical scenario and manipulate zip files programmatically in Python.

## Key Requirements

    Deterministic Output: Your hashing function must be deterministic, meaning the same input ("ClaraZetkin") should always produce the same hash value.
    Password Usage: The calculated hash value will be used as the password to unlock a provided zip file. The zip file contains a single text file with the challenge flag.

## Guidelines for Implementation
Hashing Function (division_remainder_hash):
    Input: The plaintext string "ClaraZetkin".
    Process:
        Convert each character of the input string to its ASCII value and sum these values.
        Choose 101 as a prime number and calculate the remainder of the sum divided by this prime number. This remainder is your hash value.
    Output: The hash value as an integer

## Unlocking the Zip File:
    Requirement: Use the hash value obtained from your hashing function as the password to unlock and extract the contents of the provided zip file.

## Testing:
- To test your code, simply write:  
```bash
python division_remainder_hash.py
```