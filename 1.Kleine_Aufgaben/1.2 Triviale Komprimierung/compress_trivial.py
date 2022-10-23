class CompressedGene:

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # Mit Sentine1 starten
        for nucleotide in gene.upper():
            self.bit_string <<=2 # Zwei Bit nach links verschieben
            if nucleotide == "A": ## Letzte zwei Bit in 00 ändern.
                self.bit_string |= 0b00
            elif nucleotide == "C": ## Letzte zwei Bit in 01 ändern.
                self.bit_string |= 0b01
            elif nucleotide == "G": ## Letzte zwei Bit in 10 ändern.
                self.bit_string |= 0b10
            elif nucleotide == "T": ## Letzte zwei Bit in 11 ändern.
                self.bit_string |= 0b11
            else:
                raise ValueError("Ungüldiges Nukleotid: {}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""

        for i in range(0, self.bit_string.bit_length()-1, 2):
            bits: int = self.bit_string >> i & 0b11 # nur 2 relevante Bit lesen.
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # C
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # T
                gene += "T"
            else:
                raise ValueError("Ungültige Bits:{}".format(bits))
        return gene[::-1] # [::-1] Kehrt String durch Rückwärts-Slicing um

    def __str__(self) -> str:
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof
    original: str = \
    "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100

    print("Original: {} Byte".format(getsizeof(original)))

    compressed: CompressedGene = CompressedGene(original) # Komprimieren

    print("Komprimiert: {} Byte".format(getsizeof(compressed.bit_string)))

    print(compressed) # dekomprimiert

    print("Originaldaten und dekomprimierte Daten sind identisch: {}". 
      format(original == compressed.decompress()))


            