# Getting Started
- Use this command to clone this repository to start working
```bash
git clone https://github.com/kiloMIA/femctf-python-tasks.git
```
# Challenge 1: Decrypting Caesar Cipher without a Known Shift
## Objective

Your task is to decrypt a ciphertext that has been encrypted using the Caesar cipher with an unknown shift amount. The challenge is to write a Python program capable of determining the correct shift amount and decrypting the ciphertext to reveal the original message. The decrypted message will contain a flag formatted as flag{your_decrypted_message_here}.
## Key Requirements

    Shift Detection: Your program must implement a method to accurately determine the shift amount used in the encryption process.
    Alphabetic Sensitivity: Ensure your decryption process affects only alphabetic characters (both uppercase and lowercase) as well as the special characters { and }, meaning that alphabet looks like this:
    "abcdefghijklmnopqrstuvwxyz}{"
    
    All other characters should remain unchanged.
    Case Preservation: The case of each alphabetic character must be preserved in the decrypted message.

## Guidelines for Implementation
### Shift Detection and Decryption:
    The Caesar cipher is a substitution cipher that shifts characters in the plaintext a certain number of steps down or up the alphabet. In decryption, the process is reversed by shifting the characters back by the same number of steps used for encryption.

To decrypt a message encrypted with the Caesar cipher:

    Determine the Shift: First, you must identify the number of positions each character has been shifted. Without knowing the shift amount, you can:
        Use frequency analysis, based on the assumption that certain letters appear more frequently in the plaintext.
        Brute force through all possible shifts (1 through 27, including { and }) and analyze the readability of the output.
    Shift Characters Back: Once the shift amount is known, each character in the ciphertext is shifted back by this amount in the modified alphabet, including handling special characters { and }.
    
    Input:
        ciphertext: Ybjufbqjycbq{ Mca!ub’i Tqo, cfywyhbq{{og }bcmb qi Ybjuhfbqjycbgq{ Mcf}ybw Mcaub’i Tqo, yi su{uhrfqjutg qfckbt jxu mcf{t ulufo ouqf cb ntiohmqop{wnuizkpg.
    Process:
    Detect Shift Amount: Develop a strategy to determine the shift amount used to encrypt the message. Consider using frequency analysis or brute-forcing through all possible shifts (1 through 27, including the special characters { and }).
    Decrypt the Ciphertext: After identifying the shift amount, decrypt the ciphertext by shifting each alphabetic character and the special characters {, } back by the determined amount.
        Preserve the case of each letter.
        Non-alphabetic characters (except for { and }) remain unchanged.
        Ensure correct handling of the alphabet and special character wraparound.

Output: The decrypted message, preserving the case and including non-alphabetic characters and special characters {, } in their original positions.


## Testing: 
- To test your code, simply write:  
```bash
python caesar.py
```

# Challenge 2: Hash and Unzip for the Flag

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
## Testing:
- To test your code, simply write:  
```bash
python division_remainder_hash.py
```
