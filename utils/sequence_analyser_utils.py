from typing import Tuple

"""
Written by Alice Wan
Last updated: 30/09/2025

Sequence analyser utlity functions involving:
- Nucleotide counting
- GC content calculation
- Complement and reverse complement generation
- ORF finding TODO:
"""

def nucleotide_counts(sequence: str) -> tuple:
    """counts the number of each nucleotide in a DNA or RNA sequence

    Args:
        sequence (str): sequence string of DNA or RNA

    Returns:
        tuple: counts of each nucleotide in the order of A, G, T/U, C, is_dna
    """
    A_count = sequence.count("A")
    G_count = sequence.count("G")
    T_count = sequence.count("T")
    U_count = sequence.count("U")
    C_count = sequence.count("C")

    if U_count == 0:
        return A_count, G_count, T_count, C_count, True

    return A_count, G_count, U_count, C_count, False

def gc_content(sequence: str) -> float:
    """calculates the GC content of a DNA or RNA sequence

    Args:
        sequence (str): DNA or RNA sequence string

    Returns:
        float: GC content percentage (rounded to 2 decimal places)
    """
    sequence_length = len(sequence)
    G_count = sequence.count("G")
    C_count = sequence.count("C")

    gc_content = ((G_count + C_count) / sequence_length) * 100

    return round(gc_content, 2)

def complement(sequence: str, is_dna: bool) -> Tuple[str, str]:
    """generates the complement and reverse complement of a DNA or RNA sequence

    Args:
        sequence (str): sequence string of DNA or RNA
        is_dna (bool): True if DNA, False if RNA

    Returns:
        str, str: complment and reverse complement sequences
    """
    if is_dna:
        translation_table = str.maketrans("AGTC", "TCAG")
    else:
        translation_table = str.maketrans("AGUC", "UCAG")

    complement = sequence.translate(translation_table)
    reverse_complement = complement[::-1]

    return complement, reverse_complement

#TODO: implement ORF finder
def orf_finder():
    pass

def sequence_analysis(sequence: str):
    n_counts = nucleotide_counts(sequence)
    is_dna = n_counts[-1]
    gc_content_value = gc_content(sequence)
    complement_seq, reverse_complement_seq = complement(sequence, is_dna)

    return n_counts, is_dna, gc_content_value, complement_seq, reverse_complement_seq