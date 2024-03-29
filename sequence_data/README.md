
# Generate Sequence data


Software by others I have encountered
-------------------------------------

- Simple Python functions

  - For making the simple `def generate_DNA(N)` function in  [Decoding translation in the cloud and at NCBI:Exercise for Upstate Summer Career Awareness Day](https://github.com/fomightez/uscad16/blob/644bcb71bacd0f34f3f3f80a0cc07b26bd6998bd/Decoding%20translation%20in%20the%20cloud%20and%20at%20NCBI.ipynb) I borrowed from [Illustrating Python via Bioinformatics Examples (Bioinf-py)](http://hplgit.github.io/bioinf-py/doc/web/index.html)

  - http://jacksimpson.co/how-to-create-random-dna-sequences-with-python/


- Advanced Python-based software

  - NullSeq https://www.ncbi.nlm.nih.gov/pubmed/27835644  https://github.com/amarallab/NullSeq  
    >" Using the principle of maximum entropy, we developed a method that generates unbiased random sequences with pre-specified amino acid and GC content, which we have developed into a python package. "


  - Randomseq.py http://www.medcrave.com/articles/det/15292/Randomseq-python-command-ndash-line-random-sequence-generator https://medcraveonline.com/MOJPB/MOJPB-07-00235.pdf [code at https://github.com/mauriceling/bactome; (secret looks like a good package to at least know about); references NullSeq and seems to add more bells and whistles; (I used it in a demo of a script [here](https://nbviewer.jupyter.org/github/fomightez/cl_sq_demo-binder/blob/master/notebooks/demo%20get_specified_length_of_end_of_seq_from_FASTA.ipynb#Preparing-for-usage-example) to easily generate a multi-record FASTA file.)
  
  - [DeepSimulator1.5: a more powerful, quicker and lighter simulator for Nanopore sequencing ](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btz963/5698265)  
    >"The first deep learning based Nanopore simulator which can simulate the process of Nanopore sequencing."- https://github.com/lykaust15/DeepSimulator
  
  - [VCFy](https://github.com/cartoonist/vcfy)  
  VCFY generates a VCF file with simulated random variants (SNPs) based on the given probability model for a specified region of a reference genome. There is a related script, ksnper, included in that repostiory that reports the the number of SNPs in all k-mers.
  
  - [Hypothesis-Bio](https://github.com/Lab41/hypothesis-bio/)
  Hypothesis-Bio is a Hypothesis extension for property-based testing of bioinformatic software andutomates the testing process to validate the correctness of bioinformatics tools by generating a wide range of test cases beyond human testers. As part of it, it includes abilities to generate various biological data formats:
    >"This module provides a Hypothesis strategy for generating biological data formats. This can be used to efficiently and thoroughly test your code. Currently supports DNA, RNA, protein, CDS, k-mers, FASTA, & FASTQ formats."  
    
    Learned of Hypothesis-Bio due to [this post](https://twitter.com/Evilution84/status/1233046121087414272) which may also offer more suggestions for making simulated data.


- Perl-based software

  - [simuG: a general-purpose genome simulator](https://github.com/yjx1217/simuG) is a simple, flexible, and powerful tool to simulate genome sequences with pre-defined or random genomic variants by Jia-Xing Yue & Gianni Liti.
  
  - [Ragroc](http://natir.github.io/ragroc/) - allows you to generate random sequences (in raw, fasta, fastq format) and make reverse complement. All the computation are done on the browser in webassembly.
  
  - [seqrequester](https://github.com/marbl/seqrequester#simulating) includes a mode for simulating reads from a supplied genome. Looks like it has 'ultra-long-nanopore', 'pacbio' , and 'pacbio-hifi' distribution settings.


Related
-------

- See [here](https://github.com/fomightez/simulated_data/tree/master/gene_expression) for generating RNA-seq mainly/only(?) count data.

- The bottom of [the top page in this repo](https://github.com/fomightez/simulated_data#related) references a link to [long-read mock microbial community data from PromethION and 36G from MinION ](https://github.com/LomanLab/mockcommunity).

- [ART - Set of simulation tools](https://www.niehs.nih.gov/research/resources/software/biostatistics/art/)
    >"ART is a set of simulation tools to generate synthetic next-generation sequencing reads. ART simulates sequencing reads by mimicking real sequencing process with empirical error models or quality profiles summarized from large recalibrated sequencing data. ART can also simulate reads using user own read error model or quality profiles. ART supports simulation of single-end, paired-end/mate-pair reads of three major commercial next-generation sequencing platforms: Illumina's Solexa, Roche's 454 and Applied Biosystems' SOLiD. ... ART is implemented in C++ ..."
