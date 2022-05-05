import utils
from pathlib   import Path

# Student name: WRITE YOUR NAME BELOW
# -----------------------------------------------------------------------------
name:    str = "Luis"
surname: str = "Cardenete"
assert name and surname, 'Error: Please write your name and surname.'
# -----------------------------------------------------------------------------

# E1
# -----------------------------------------------------------------------------
# 1. Fes quatre classes: Seq, DNASeq, RNASeq, Protein.
# 2. DNASeq, RNASeq i Protein han d'heretar de Seq.
# 3. Codifica els atributs i els mètodes necessaris per tal que
#   passin tots els tests que hi ha a l'arxiu 'e1_test.py'.
# 4. Executeu els tests amb l'ordre: pytest -v
# 5. A l'arxiu 'utils.py' teniu codi que us pot ajudar.
# 6. Tot el codi ha d'estar a les classes o a utils.py.
# 7. En cap cas poseu codi a la secció Main. Us donarà problemes en executar pytest.
# -----------------------------------------------------------------------------


# Classes
# -----------------------------------------------------------------------------
# WRITE YOUR CODE HERE

class Seq:
    def __init__(self, seq: str):

        self.seq: str = seq
    
    def __len__(self):
        return len(self.seq)
   
    @classmethod
    def from_fasta(cls,fasta_filename: str) :
    
        fasta_text:      str  = Path(fasta_filename).read_text()
        line_list:  list[str] = fasta_text.strip().split('\n')
        header: str       = line_list[0]
        body:   list[str] = line_list[1:]


        seq: str  = ''.join(body)
        good_sep: Seq= cls(seq)

        return good_sep

    def __str__(self) -> str:
            introduction: str = f"{self.seq}"
            return f"{introduction}"
    
   










class Protein(Seq):
    def __init__(self, seq: str):
        super().__init__(seq)
        for letter in self.seq:
            if (letter=="Ç") or (letter=="Ñ"):
                assert False
            else:
                pass
        






class RNASeq(Seq):
    def __init__(self, seq: str):
        super().__init__(seq)
        for letter in self.seq:
            try:
                letter=="T"
            except:
                pass
    def translate(self):
        trios: str= utils.AMINO.keys
        letters: str= utils.AMINO.values
        translate_seq: str =self.seq.replace(trios, letters)
        return translate_seq






class DNASeq(Seq):
    def __init__(self, seq: str):
        super().__init__(seq)
        raise
    def transcribe(self):
        transcribe_seq: str= self.seq.replace("T", "U")
        return transcribe_seq
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    #  t2: Seq = Seq.from_fasta("data_dna.fasta")
    #  t3: Seq= Seq.len(t2)
    #  print(t2 , t3)
     pass
    # Write your solution inside classes.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
 