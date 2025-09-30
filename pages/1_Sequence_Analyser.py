import streamlit as st
from utils.sequence_analyser_utils import sequence_analysis

# Written by Alice Wan
# Last updated on 30/09/2025

st.title("🧬 DNA/RNA Sequence Analyser")

st.info("You may either insert in your own single DNA/RNA sequence or upload a file in FASTA format for single or multiple sequences")
input_mode = st.radio(
    "You may either insert in your own single DNA/RNA sequence or upload a file in FASTA format for single or multiple sequences:",
    ("Insert DNA/RNA sequence", "Upload FASTA file")
)

if input_mode == "Insert DNA/RNA sequence":
    sequence = st.text_area(
        "Enter your DNA/RNA sequence here"
    )

    st.write(f"You wrote {len(sequence)} characters.")

    if sequence.strip():
        st.write(sequence)
        n_counts, is_dna, gc_content_value, complement_seq, reverse_complement_seq = sequence_analysis(sequence)
        st.write("### Analysis Results:")
    else:
        st.info("👉 Please enter a DNA or RNA sequence to see the analysis.")
elif input_mode == "Upload FASTA file":
    uploaded_file = st.file_uploader("Upload a FASTA file", type=["fasta", "fa", "txt"], accept_multiple_files=False)