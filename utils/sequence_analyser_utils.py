from typing import Tuple

def nucleotide_count(sequence: str, is_dna: bool) -> tuple:
    """counts the number of each nucleotide in a DNA or RNA sequence

    Args:
        sequence (str): sequence string of DNA or RNA
        is_dna (bool): True if DNA, False if RNA

    Returns:
        tuple: counts of each nucleotide in the order of A, G, T/U, C
    """
    A_count = sequence.count("A")
    G_count = sequence.count("G")
    U_count = sequence.count("U")
    T_count = sequence.count("T")
    C_count = sequence.count("C")

    if is_dna:
        return A_count, G_count, T_count, C_count

    return A_count, G_count, U_count, C_count

def gc_content(sequence: str) -> float:
    sequence_length = len(sequence)
    G_count = sequence.count("G")
    C_count = sequence.count("C")

    gc_content = ((G_count + C_count) / sequence_length) * 100

    return round(gc_content, 2)

def complementary_strand(sequence: str, is_dna: bool) -> Tuple[str, str]:
    """generates the complementary strand of a DNA or RNA sequence

    Args:
        sequence (str): sequence string of DNA or RNA
        is_dna (bool): True if DNA, False if RNA

    Returns:
        str, str: complementary strand and reverse complementary strand
    """
    if is_dna:
        translation_table = str.maketrans("AGTC", "TCAG")
    else:
        translation_table = str.maketrans("AGUC", "UCAG")

    complement = sequence.translate(translation_table)
    reverse_complement = complement[::-1]

    return complement, reverse_complement