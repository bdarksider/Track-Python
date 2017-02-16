def to_rna(dna):
    translate = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
    rna = "".join(translate.get(i, "") for i in dna)
    return rna if len(rna) == len(dna) else ""