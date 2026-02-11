
# DNA Motif Finder

def clean_dna_sequence(seq):
    seq = seq.upper()
    cleaned = ""
    valid_bases = ["A", "T", "G", "C"]

    for base in seq:
        if base in valid_bases:
            cleaned += base

    return cleaned


def find_motif(sequence, motif):
    positions = []
    motif_length = len(motif)

    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i + motif_length] == motif:
            positions.append(i + 1)  # Biological indexing starts at 1

    return positions


# ===== Main Program =====

dna_input = input("Enter a DNA sequence: ")
motif_input = input("Enter a motif to search: ")

dna = clean_dna_sequence(dna_input)
motif = clean_dna_sequence(motif_input)

if len(dna) == 0 or len(motif) == 0:
    print("Invalid input. Please enter valid DNA bases (A, T, G, C).")
else:
    matches = find_motif(dna, motif)

    print("\nClean DNA Sequence :", dna)
    print("Motif              :", motif)

    if matches:
        print("Motif found at positions:", matches)
    else:
        print("Motif not found in the sequence.")
