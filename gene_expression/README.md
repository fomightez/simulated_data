# mock_expression_ratio_generator.py

> The purpose behind `mock_expression_ratio_generator.py` is to generate mock data for illustrating the options in
the script `plot_expression_across_chromosomes.py` and related scripts.

`mock_expression_ratio_generator.py` takes all genes in a gtf (or gff) and parses that data and then puts a one to
one ratio for all the data except chromosome regions marked as having 
different expression ratio relative baseline. Puts those as random normal
distributions around that value. Saves the data as a Tab-seperated values file
that can be used directly by `plot_expression_across_chromosomes.py` and related 
scripts in conjunction with the gtf file to make plots. Currently, I only have
real RNA-Seq data with disomy of one yeast chromosome, and strains that seem
to have the same copy number as wild-type. Using this script I can illustrate 
what other results, i.e., disomy of more than one chromosomes, trisomy, etc., 
may sort of look like in the plots.

An excellent source of the annotation files is the iGenomes page of Illumina's website [here](https://support.illumina.com/sequencing/sequencing_software/igenome.html). There you can find a genome annotation file in `GTF` format for many organisisms. For baker's yeast, Saccharomyces cerevisiae, I suggest the one found in the Ensembl download. The direct link to the file is tp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Saccharomyces_cerevisiae/Ensembl/R64-1-1/Saccharomyces_cerevisiae_Ensembl_R64-1-1.tar.gz. You'd download it by clicking on `R64-1-1` next to Ensembl, unzipping that file, and then going inside the unzipped directory and navigating the hierarch of `Saccharomyces_cerevisiae_Ensembl_R64-1-1/Saccharomyces_cerevisiae/Ensembl/R64-1-1/Annotation/Archives/archive-2015-07-17-14-36-40/Genes` to locate the file `genes.gtf`. That is an example of a file that will work well with the script `mock_expression_ratio_generator.py`.




Related scripts by others I have encountered
------------------------------------

[sim.counts: RNA-seq Count Data Simulation from Negative-Binomial distribution ](https://rdrr.io/cran/ssizeRNA/man/sim.counts.html)
