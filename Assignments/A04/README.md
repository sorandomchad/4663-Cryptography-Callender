## Assignment 4 - ADFGX Implementation
### Chad Callender
### Description:

### ADFGX Cipher
 
The ADFGX cipher was a field cipher used by the German Army during World War I. It is closely related to the ADFGVX cipher. ADFGX is a fractionating transposition cipher which combined a modified Polybius square with a single columnar transposition. The cipher is named after the five possible letters used in the ciphertext: A, D, F, G and X. These letters were chosen deliberately because they sound very different from each other when transmitted via morse code. The intention was to reduce the possibility of operator error. The cipher uses two keywords to encrypt and decrypt messages.

This assignment entails implementing the ADFGX cipher, creating `encrypt` and `decrypt` functions. The implementation of this cipher also requires defining functions that create the Polybius square, fractionate the resulting matrix, matching plaintext to ciphertext. Finally, the program should be able to handle input files, ignoring characters that are not letters of the alphabet and it should be created in such a way that it can be run using command line parameters.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [adfgx.py](./adfgx.py)       | This is the main file where the code runs. |
|   2   | [cipher.py](./cipher.py) | The `encrypt` and `decrypt` functions are defined here. |
|   3   | [fractionate.py](./fractionate.py) | This file takes the second keyword and fractionates the message from the first polybius square. |
|   4   | [polybius.py](./polybius.py)   | This file takes the first keyword and builds the polybius "matrix" and assigns each plaintext letter to its corresponding pair of letters from A, D, F, G, X. |

### Instructions

Invoke the progam from the command line using keyword arguments like this
```
                        1                   2           3                4
python adfgx.py input=input_file_name key1=keyword1 key2=keyword2 op=[encrypt,decrypt] 
```
where

1. The file to be encrypted or decrypted
2. keyword to build ADFGX matrix (polybius square)
3. keyword used with transposition matrix and fractionating the message
4. whether to "encrypt" or "decrypt" the message.
