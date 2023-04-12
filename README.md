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

- a script that allows for using long reads make mock short read data:
[Create short paired-end reads from long reads](https://github.com/Chartiza/Microbiome/tree/main/long_reads_to_short_PE_reads)
>"To test different approaches for assembling genomes, I needed data with known microbial content. Only long reads were available, but I needed to test the algorithm on short paired-end reads. This script was written to create short reads from long reads."
