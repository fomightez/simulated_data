# simulated_data
A repository for code that generates various simulated data.

Subfolders found here concern:

* [raw nucleic acid (even genomic) or protein sequences](https://github.com/fomightez/simulated_data/tree/master/sequence_data)

* [gene expression](https://github.com/fomightez/simulated_data/tree/master/gene_expression)

* [gene lists](https://github.com/fomightez/simulated_data/tree/master/gene_lists)

* [high-throughput sequencing data from phylogenetic relationships](https://github.com/fomightez/simulated_data/tree/master/across_phylogeny)

* [general computational data](https://github.com/fomightez/simulated_data/tree/master/general)



Related efforts by others
-------------------------

- "select 5-10 Mb of neutral DNA sequences in the human genome": 
https://twitter.com/cegAmorim/status/1646158398071754755  
>"What is a good and easy way to select 5-10 Mb of neutral DNA sequences in the human genome? Would selecting random intergenic regions (say >10Kb away from genes) be enough? Has someone done something similar recently in a paper I could cite and use the same loci?"  
https://twitter.com/vsbuffalo/status/1646212322833334272   
>"I had to do this recently — I took all exonic + phastcons + UTRS, merged them, and then add 200bp of buffer on both ends (all using bedtools). You could do this and even select out random regions. I did some sensitivity analysis and comparison to the CADD tracks and seemed good."  
>"Also (and perhaps this is being too paranoid) but I  merged the refseq and ensembl tracks. They differ slightly in their percent of basepairs that annotated as coding, so I took the union."  

- long-read mock microbial community data:
https://twitter.com/pathogenomenick/status/1037346467462176769
>"Go and grab 130G of long-read mock microbial community data from PromethION and 36G from MinION over here, if you fancy:
https://github.com/LomanLab/mockcommunity … #UKGS18 - could be useful for bioinformatics pipeline validation and method development!"

https://twitter.com/Hasindu2008/status/1628569325895585793
>"Squigulator r10 branch https://github.com/hasindu2008/squigulator/tree/r10 can simulate r10.4.1 signals. Also f5c r10 branch https://github.com/hasindu2008/f5c/tree/r10 can do resquiggle and eventalign for R10.4.1.
Note: still work in progress and improvements are on the way. 
Thanks, @nanopore for providing the pore-model."
  - [Squigulator](https://github.com/hasindu2008/squigulator/tree/r10) - "a tool for simulating nanopore raw signal data"
  - Plus, "...f5c r10 branch https://github.com/hasindu2008/f5c/tree/r10 can do resquiggle and eventalign for R10.4.1"
  - https://twitter.com/Hasindu2008/status/1656470090668449793 May 2023
    >"Here is a pre-print for squigulator: a tool for simulating @nanopore raw signal data https://biorxiv.org/content/10.1101/2023.05.09.539953 Squigulator is easy to use, simple, fast, supports dna/rna and r9/r10 and  modifiable parameters, and the output can be basecalled using nanopore basecallers."

- a script that allows for using long reads make mock short read data:
[Create short paired-end reads from long reads](https://github.com/Chartiza/Microbiome/tree/main/long_reads_to_short_PE_reads)
>"To test different approaches for assembling genomes, I needed data with known microbial content. Only long reads were available, but I needed to test the algorithm on short paired-end reads. This script was written to create short reads from long reads."

- [simuG: a general-purpose genome simulator.](https://github.com/yjx1217/simuG) "A simple, flexible, and powerful tool to simulate genome sequences with pre-defined or random genomic variants." ... "simuG as a light-weighted tool for simulating the full spectrum of genomic variants (SNPs, INDELs, CNVs, inversions, and translocations)." Learned if from an answer to ['To randomly generate a list of insertions and deletions'](https://www.biostars.org/p/9599960/)

* [sim.counts: RNA-seq Count Data Simulation from Negative-Binomial distribution](https://rdrr.io/cran/ssizeRNA/man/sim.counts.html) - this R function doesn't seem to allow specifically designating regions to alter levels, but you could probably further edit the simulated data to do that for genes in the region in which you are looking to alter the level relative the baseline.


* [cypress: an R/Bioconductor package for cell-type-specific differential expression analysis power assessment ](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btae511/7735301?login=false)  - "cypress is capable of modeling and simulating various sources of variation in signal convolution and deconvolution and adopting multi-faceted statistical evaluation metrics in csDE hypothesis testing evaluation." - [SOURCE](https://x.com/razoralign/status/1825029912820129818)

Single cell:  
- [scReadSim: a single-cell RNA-seq and ATAC-seq read simulator](https://github.com/JSB-UCLA/scReadSim), which I learned of at the bottom of [scDesign3](https://github.com/SONGDONGYUAN1994/scDesign3) under 'Related Manuscripts'.
From abstract: "To fill this gap, we introduce scReadSim, a single-cell RNA-seq and ATAC-seq read simulator that allows user-specified ground truths and generates synthetic sequencing reads (in a FASTQ or BAM file) by mimicking real data." 

- scDesign3 for Single cell: https://twitter.com/jsb_ucla/status/1656690298435821568. May 2023. 
>"Our single-cell and spatial omics simulator scDesign3 is now online: https://nature.com/articles/s41587-023-01772-1
scDesign3 has two functionalities: (1) synthetic data simulation and (2) real data interpretation and modification 1/"  (The [scDesign3 Github repo](https://github.com/SONGDONGYUAN1994/scDesign3))

- [Splatter: Simulation Of Single-Cell RNA-seq](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1305-0) -  Bioconductor (R) package for simple, reproducible and well-documented simulation of single-cell RNA-seq data. Splatter provides an interface to multiple simulation methods including Splat, based on a gamma-Poisson distribution. Splat can simulate single populations of cells, populations with multiple cell types or differentiation paths.

Be sure to also see 'Related software by others I have encountered' on the page [Scripts and resources for generating simulated data for gene expression analysis](https://github.com/fomightez/simulated_data/tree/master/gene_expression) because sometimes I add to there and not here and vice versa.

Only Tangentially Related
--------------------------

https://x.com/RobAboukhalil/status/1808602458698232258     July 2024
>"When writing bioinformatics tools, I often need small datasets to test edge cases or invalid file formats, e.g. files that are truncated, unsorted, have extraneous whitespace, etc.
I started compiling examples here: https://github.com/omgenomics/bio-data-zoo, contributions are welcome!"
    [Bio Data Zoo](https://github.com/omgenomics/bio-data-zoo)  
    >"This repo contains example data in various genomics file formats. It is intended for bioinformatics tool developers to make testing software easier. It includes examples of valid file formats, edge cases, and invalid formats."
