# Lecture 15: K-mers in Genomics — Literature Summary & Proposed Outline

> **Status:** Ready for review before lecture generation
> **Scope:** From basic k-mer concepts through minimizers to the minimap2 algorithm
> **Format:** Quarto page (standard lecture format)

---

## Annotated Bibliography

### 1. Foundational K-mer Concepts & Counting

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Jellyfish** | Marcais G, Kingsford C. *Bioinformatics* 27(6):764-770, 2011 | Lock-free parallel hash table for k-mer counting using CAS hardware operations. Processes large genomes in minutes. |
| **KMC 2** | Deorowicz S, Kokot M, Grabowski S, Debudaj-Grabysz A. *Bioinformatics* 31(10):1569-1576, 2015 | Disk-based k-mer counting with LSD radix sort. ~2x faster than Jellyfish 2 on large datasets, ~12 GB RAM. |
| **KMC 3** | Kokot M, Dlugosz M, Deorowicz S. *Bioinformatics* 33(17):2759-2761, 2017 | Extended KMC with k-mer set operations (union, intersection, subtraction). |
| **K-mer data structures review** | Marchet C, Boucher C, Puglisi SJ, Medvedev P, Salson M, Chikhi R. *Genome Research* 31(1):1-12, 2021 | Comprehensive survey of k-mer-based data structures for indexing/querying large sequence collections. |

### 2. K-mer Spectrum Analysis & Genome Characterization

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **GenomeScope** | Vurture GW, Sedlazeck FJ, Nattestad M, et al. *Bioinformatics* 33(14):2202-2204, 2017 | K-mer frequency histograms to estimate genome size, heterozygosity, and repeat content without a reference. |
| **GenomeScope 2.0** | Ranallo-Benavidez TR, Jaron KS, Schatz MC. *Nature Communications* 11:1432, 2020 | Extended to polyploid genomes using Möbius inversion formula. |
| **Merqury** *(seed paper)* | Rhie A, Walenz BP, Koren S, Phillippy AM. *Genome Biology* 21:245, 2020 | Reference-free assembly QC using k-mer set operations: spectra-asm plots, QV estimation, haplotype phasing assessment via hap-mers. Built on Meryl. |

### 3. De Bruijn Graphs & Genome Assembly

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Eulerian path assembly** | Pevzner PA, Tang H, Waterman MS. *PNAS* 98(17):9748-9753, 2001 | Foundational paper: genome assembly as finding Eulerian paths in de Bruijn graphs built from k-mers. |
| **De Bruijn graph tutorial** | Compeau PEC, Pevzner PA, Tesler G. *Nature Biotechnology* 29(11):987-991, 2011 | Accessible tutorial — k-mer prefixes/suffixes as nodes, k-mers as edges, Eulerian cycles for reconstruction. Ideal pedagogical reference. |
| **SPAdes** | Bankevich A, et al. *Journal of Computational Biology* 19(5):455-477, 2012 | Practical multi-k de Bruijn graph assembler for single-cell and standard data. |

### 4. Minimizers & Related Theory

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Minimizers (original)** | Roberts M, Hayes W, Hunt BR, Mount SM, Yorke JA. *Bioinformatics* 20(18):3363-3369, 2004 | Seminal paper: select the smallest k-mer in a sliding window to subsample seeds. Reduces storage while preserving matching sensitivity. |
| **Winnowing** | Schleimer S, Wilkerson DS, Aiken A. *SIGMOD* pp.76-85, 2003 | Local document fingerprinting with provable density guarantees. Independent invention of the minimizer concept in the plagiarism-detection domain. |
| **Universal hitting sets** | Orenstein Y, et al. *PLoS Computational Biology* 13(10):e1005777, 2017 | DOCKS algorithm for universal hitting sets to improve minimizer density. Achieved density factor 1.737, disproving the conjectured lower bound of 2. |
| **Improved minimizers (Miniception)** | Zheng H, Kingsford C, Marcais G. *Bioinformatics* 36(S1):i119-i127, 2020 | Further improvements to minimizer ordering and density. |

### 5. Syncmers

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Syncmers** | Edgar RC. *PeerJ* 9:e10805, 2021 | K-mers selected by internal s-mer position (not surrounding context). Context-independent — cannot be invalidated by flanking mutations. Lower density and higher conservation than minimizers. |

### 6. Minimap2

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Minimap2** *(seed paper)* | Li H. *Bioinformatics* 34(18):3094-3100, 2018 | The definitive minimizer-based aligner. **Pipeline:** (1) Index reference minimizers in hash table → (2) Query minimizers find anchors → (3) Chain anchors via DP with gap costs → (4) Base-level alignment with two-piece affine gap + Z-drop heuristic. Handles short reads, long reads (15% error), cDNA, and contigs. 3-4x faster than BWA-MEM; 30x+ faster than long-read mappers. |

### 7. Sequence Similarity via K-mer Sketching

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Mash** *(seed paper)* | Ondov BD, Treangen TJ, Melsted P, et al. *Genome Biology* 17:132, 2016 | MinHash applied to genomic k-mer sets. "Sketch" = smallest hash values. Mash distance approximates mutation rate via Jaccard index. Clustered 54,118 RefSeq genomes in 33 CPU hours. |
| **Sourmash** | Brown CT, Irber L. *JOSS* 1(5):27, 2016 | Scaled MinHash (FracMinHash): consistent fraction of hashes regardless of dataset size. Supports containment searches for metagenomics. |

### 8. Metagenomic Classification

| Paper | Citation | Key Takeaway |
|-------|----------|--------------|
| **Kraken** | Wood DE, Salzberg SL. *Genome Biology* 15:R46, 2014 | K-mer → LCA mapping for taxonomic classification. 4.1M reads/min, 909x faster than Megablast. |
| **Kraken 2** | Wood DE, Lu J, Langmead B. *Genome Biology* 20:257, 2019 | Stores minimizers instead of full k-mers — 85% memory reduction. Bridges minimizer theory with practical metagenomics. |

---

## Proposed Lecture Outline

### Part I: K-mer Fundamentals
1. **What is a k-mer?** — Definition, sliding window, 4^k complexity, canonical k-mers, reverse complements
2. **K-mer counting** — Hash-based approaches (Jellyfish: in-memory lock-free; KMC: disk-based radix sort); practical considerations (choice of k, error k-mers vs true k-mers)
3. **K-mer spectrum** — Frequency histogram interpretation; GenomeScope: genome size, heterozygosity, repeat content; Merqury: assembly QC via spectra-asm plots

### Part II: K-mers in Assembly
4. **De Bruijn graphs** — K-mers as edges, (k-1)-mers as nodes; Eulerian paths; comparison with overlap-layout-consensus; SPAdes as practical example

### Part III: Subsampling — The Need for Speed
5. **The scaling problem** — Why full k-mer indexing doesn't scale; motivation for subsampling
6. **Minimizers** — Roberts et al. 2004: smallest k-mer in a window; density and conservation; connection to winnowing (Schleimer et al. 2003)
7. **Improving minimizers** — Universal hitting sets (Orenstein et al. 2017); random vs optimized orderings
8. **Syncmers** — Edgar 2021: context-independent selection; comparison with minimizers

### Part IV: Minimizers in Action
9. **Minimap2 deep dive** — Four stages: indexing (minimizer hash table), seeding (anchor lookup), chaining (DP with gap penalties), alignment (two-piece affine gap, Z-drop); versatility across read types
10. **Sketching for similarity** — Mash/MinHash: Jaccard distance from k-mer sketches; sourmash: scaled MinHash for containment

### Part V: Applications
11. **Metagenomic classification** — Kraken: k-mer → LCA taxonomy; Kraken 2: minimizer compression (85% memory savings)
12. **Summary and connections** — How k-mers unify counting, assembly, alignment, comparison, and classification

---

## Key Concepts to Emphasize

- **K-mer spectrum as a fingerprint** — The shape of the histogram tells you about genome properties before any assembly
- **De Bruijn graphs as the bridge** — K-mers aren't just counted; they define graph structure for assembly
- **Minimizers as the key innovation** — A simple idea (pick the smallest in a window) that enables minimap2, Kraken 2, and many other tools
- **Seed-chain-align paradigm** — The core of minimap2; how minimizers replace traditional seeding
- **Practical tradeoffs** — Choice of k, window size w, memory vs speed, sensitivity vs specificity

## Practical Considerations to Weave In

- Effect of sequencing errors on k-mer counts (error k-mers appear once)
- Canonical k-mers (lexicographically smaller of k-mer and reverse complement)
- Choice of k: too small → ambiguity; too large → sensitivity to errors
- Window size w for minimizers: smaller w → more seeds, higher sensitivity, more memory

---

## Validation Status

All citations independently verified by validator agent:
- Paper metadata (authors, years, journals): **Accurate**
- Paper content summaries: **Faithful to originals**
- Topic coverage: **Comprehensive for a single lecture**
- Conceptual flow: **Logical and pedagogically sound**
- No major gaps identified

**Total papers: 19** across 8 topic areas
