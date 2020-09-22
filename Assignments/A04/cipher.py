""""
  This file defines the encrypt and decrypt functions to be used in the implemenatation of this cipher.
"""

import polybius as pb
import fractionate as frac
import math

class Adfgx(pb.AdfgxLookup):
    #this is gonna have the encrypt and decrypt functions

    def encrypt(self, **kwargs):
      """
        Takes a plaintext message and encrypts it.
      """

      input_file = kwargs.get('input', None)
      output_file = kwargs.get('output', None)
      self.key = kwargs.get('key1', None)
      self.key2 = kwargs.get('key2', None)
      
      with open(input_file) as f:
        message = f.read()

      message = message.lower()

      lookup = self.build_polybius_lookup(self.key)
      #pp.pprint(boy)
      print("Message:", message)
      print("Encrypting...")

      for l in message:
        if not l in self.alphabet:
          message = message.replace(l,'')  # get rid of spaces

      pre_text = []

      for letter in message:
        pre_text.append(lookup[letter])

      message = ''.join(pre_text)
      #print(message)

      # dictionary for our new matrix
      matrix = {}

      # every letter is a key that points to a list
      for k in self.key2:
          matrix[k] = []

      # add the message to the each list in a row-wise fashion
      # meaning DFFDGAFXXA gets loaded like:
      #
      #           QUARK
      #           -----
      #           DFFDG
      #           AFXXA
      i = 0
      for m in message:
          matrix[self.key2[i]].append(m)
          i += 1
          i = i % len(self.key2)

      # Alphabetize the matrix (not really necessary) if you just
      # alphabetize the key2 word and use it to access the dictionary
      # in alphabetical order instead. BUT this does stick to the
      # algorithm
      temp_matrix = sorted(matrix.items())

      #print("")

      sorted_matrix = {}

      # Rebuild the sorted matrix into a dictionary again
      # Rememnber sorted returns a list of tuples and we
      # need to make another dictionary. This is another
      # reason NOT to sort the matrix, but simply access
      # it via an alphabetized word.
      for item in temp_matrix:
          sorted_matrix[item[0]] = item[1]


      #encrypted message
      with open(output_file, 'w') as f:
        f.write(frac.print_message(matrix, self.key2))

      return None
      
    
    def decrypt(self, **kwargs):
      """
        Takes a ciphertext message and decrypts it. 
      """

      input_file = kwargs.get('input', None)
      output_file = kwargs.get('output', None)
      self.key = kwargs.get('key1', None)
      self.key2 = kwargs.get('key2', None)
      
      with open(input_file) as f:
        ciphertext = f.read()

      ciphertext = ciphertext.upper()
      
      print("Message:", ciphertext)
      print("Decrypting...")

      for l in ciphertext:
        if not l in self.adfgx:
          ciphertext = ciphertext.replace(l,'')
      
      matrix = {}

      for k in self.key2:
        matrix[k] = []

      text_length = len(ciphertext)
      key2_length = len(self.key2)
      
      rows = math.ceil(float(text_length)/float(key2_length))
      short_cols = key2_length - (text_length%key2_length)

      short_col_letters = self.key2[-short_cols:]

      ind = 0

      for k in sorted(self.key2):
        if k in short_col_letters:
          for i in range(rows-1):
            matrix[k].append(ciphertext[ind])
            ind += 1
        else:
          for i in range(rows):
            matrix[k].append(ciphertext[ind])
            ind += 1

      string = ''
      for i in range(rows):
        for k in self.key2:
          try:
            string += matrix[k][i]
          except IndexError:
            continue

      lookup = self.build_polybius_lookup(self.key)

      plaintext = ''
      for i in range(0, text_length, 2):
        for k in lookup.items():
          if string[i:i+2] == k[1]:
            plaintext += k[0]
          
      with open(output_file, 'w') as f:
        f.write(plaintext)

      return None


if __name__ == '__main__':
  C = Adfgx('matrix','radial')
  C.encrypt("spaghetti")
  #should return XF XA GD AX FF FA FA GD DF
  C.decrypt("FA FF XD FF DA GA GG FA DA DA AD FD XA DA XA FG FX")
  #should return theattackisatdawn
