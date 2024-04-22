class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.compress(gene)

    def compress(self, gene: str) -> None:
        self.bit_string : int = 1 # start with sentinel
        for nucleotide in gene.upper(): 
            self.bit_string <<= 2 # shift left (multiply by) 2 bits
            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide {}".format(nucleotide))
            
    def decompress(self) -> str:
        gene: str = ""
        for i in range (0, self.bit_string.bit_length() -1, 2): # - 1 to exclude sentinel
            bits : int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
        
        return gene[::-1]
    
    def __str__(self) -> str:
        return self.decompress()


import sys
sys.set_int_max_str_digits(10000)  # Increase the limit to 10000 digits  
from sys import getsizeof

if __name__ == "__main__":
    original: str =  "TAGG"  #"TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print(f'The original string has size {getsizeof(original)}')

    compressed: CompressedGene = CompressedGene(original)

    print(f'The compressed string has size {getsizeof(compressed.bit_string)}')
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))

