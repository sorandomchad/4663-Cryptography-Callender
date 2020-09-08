# import sys
# import os
# import requests
# import pprint as pp

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None

if __name__=='__main__':
    #url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    #url = "https://www.gutenberg.org/files/2600/2600-0.txt"
    #print("Downloading book ...")
    #f = requests.get(url)
    #text = f.text

    with open("ciphertext_1.txt") as ciphertext_1:
      text_1 = ciphertext_1.read()

    with open("ciphertext_2.txt") as ciphertext_2:
      text_2 = ciphertext_2.read()

    print("ciphertext_1.txt Frequency Distribution")
    print("Calculating frequency...")
    F1 = Frequency()

    F1.count(text_1)

    F1.print()
    
    print("\n\nciphertext_2.txt Frequency Distribution")
    print("Calculating frequency...")
    F2 = Frequency()

    F2.count(text_2)

    F2.print()
