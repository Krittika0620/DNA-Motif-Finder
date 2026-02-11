# 🧬 DNA Motif Finder

A simple Python tool that searches for a specific DNA motif (short sequence pattern) within a longer DNA sequence.

This project demonstrates basic sequence analysis and pattern matching, which are fundamental tasks in bioinformatics.

---

## 🚀 Features

* Accepts user input for a DNA sequence
* Accepts a motif (short DNA pattern) to search
* Cleans input by removing invalid characters
* Reports all positions where the motif occurs
* Uses biological position numbering (starts from 1)

---

## 🧪 Biological Background

A **motif** is a short, recurring DNA sequence that may have biological significance, such as:

* Promoter regions
* Transcription factor binding sites
* Regulatory elements

Finding motifs in sequences is a common task in genomics and molecular biology research.

---

## 💻 How to Run

1. Make sure Python 3 is installed
2. Download or clone this repository
3. Run the script:

```bash
python motif_finder.py
```

4. Enter a DNA sequence when prompted
5. Enter a motif to search for

### Example

**Input**

```
Enter a DNA sequence: ATGCGATATCGATATCG
Enter a motif to search: ATATC
```

**Output**

```
Clean DNA Sequence : ATGCGATATCGATATCG
Motif              : ATATC
Motif found at positions: [6, 12]
```

---
