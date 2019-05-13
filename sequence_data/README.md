
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


- Perl-based software

  - [simuG: a general-purpose genome simulator](https://github.com/yjx1217/simuG) is a simple, flexible, and powerful tool to simulate genome sequences with pre-defined or random genomic variants by Jia-Xing Yue & Gianni Liti.


Related
-------

See [here](https://github.com/fomightez/simulated_data/tree/master/gene_expression) for generating RNA-seq mainly/only(?) count data.

The bottom of [the top page in this repo](https://github.com/fomightez/simulated_data) references a link to [long-read mock microbial community data from PromethION and 36G from MinION ](https://github.com/LomanLab/mockcommunity).
