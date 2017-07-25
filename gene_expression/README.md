# Scripts for generating simulated data for gene expression analysis

**DESCRIPTIONS**

## mock_expression_ratio_generator.py

> The purpose behind `mock_expression_ratio_generator.py` is to generate mock summary RNA-Seq data demostrating anueploidy in a genome to fully show the ability of the script `plot_expression_across_chromosomes.py` and related scripts.

`mock_expression_ratio_generator.py` takes all genes in a gtf (or gff) and parses that data and then puts a one to
one ratio for all the data except chromosome regions marked as having 
different expression ratio relative baseline. Puts those as random normal
distributions around that value. Saves the data as a Tab-seperated values file
that can be used directly by [plot_expression_across_chromosomes.py](https://github.com/fomightez/sequencework/tree/master/plot_expression_across_chromosomes) and related 
scripts in conjunction with the gtf file to make plots. Currently, I only have summarized
real RNA-Seq data with disomy of one yeast chromosome, and , of course, strains that seem
to have the same copy number as wild-type. Using this script, I can illustrate 
what additional instances of aneuploidy, i.e., disomy of more than one chromosomes, trisomy, haploinsufficciency, etc., 
may vaguely resemble in the plots without the need to run an analysis of others data, for example, [Ryu et al., 2016](https://www.ncbi.nlm.nih.gov/pubmed/27585592), where they reported disomy of chromosome I and XII in their RNA-Seq data.

An excellent source of the annotation files is the iGenomes page of Illumina's website [here](https://support.illumina.com/sequencing/sequencing_software/igenome.html). There you can find a genome annotation file in `GTF` format for many organisisms. For baker's yeast, Saccharomyces cerevisiae, I suggest the one found in the Ensembl download. The direct link to the file is ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Saccharomyces_cerevisiae/Ensembl/R64-1-1/Saccharomyces_cerevisiae_Ensembl_R64-1-1.tar.gz. You'd download it by clicking on `R64-1-1` next to Ensembl, unzipping that file, and then going inside the unzipped directory and navigating the hierarchy of `Saccharomyces_cerevisiae_Ensembl_R64-1-1/Saccharomyces_cerevisiae/Ensembl/R64-1-1/Annotation/Archives/archive-2015-07-17-14-36-40/Genes` to locate the file `genes.gtf`. That is an example of a file that will work well with the script `mock_expression_ratio_generator.py`.

Presently, you need to specify in the actual script code the regions by location on the chromosome and to what degree they differ from the baseline. The dictionary storing that information can be found inside the script under the `USER ADJUSTABLE VALUES`. I eventually plan to change that to allow you to specify this information on the command line when you call the script, but this works for now.

**USAGE**

```text
usage: mock_expression_ratio_generator.py [-h] ANNOTATION_FILE

mock_expression_ratio_generator.py is an acessory script to generate mock data
for plotting with plot_expression_across_chromosomes.py. **** Script by Wayne
Decatur (fomightez @ github) ***
positional arguments:
  ANNOTATION_FILE  Name of file containing the genome annotation. REQUIRED.
                   This is needed to determine the order of individual data
                   points along the chromosome and how to display the data
                   across chromosomes or scaffolds.
optional arguments:
  -h, --help       show this help message and exit
```

**EXAMPLE USE AND VISUALIZATION**

**Script preparation:**

Script `USER ADJUSTABLE VALUES  ` edited to have as `ratio_by_region_dictionary`:

```python
ratio_by_region_dictionary = {
"I":{(1,230218):2.0}, 
"XII":{(1,1078177):2.0},
"XVI":{(1,98010):3.0, (118010,948010):3.0} 
}
```

This is to specify which regions do not have a 1:1 ratio.

**Command run**

    python mock_expression_ratio_generator.py genes.gtf


**First few lines of tab-separated values file produced as `genes_mock_expression_ratios.tsv`:**
```
gene_id	mock_base	mock_exp
YAL069W	66022.6853093	147381.19018
YAL068W-A	85240.4848535	331358.926347
YAL068C	86245.9503597	171221.048364
YAL067W-A	95421.1683197	293475.594665
YAL067C	75617.061132	67246.625205
YAL066W	89931.0568079	95933.6236498
YAL065C	70577.9945921	237409.443024
YAL064W-B	74548.5676547	72217.644534
YAL064C-A	74102.1236196	139528.566449
YAL064W	77790.9892057	159623.579542
YAL063C-A	79882.7099824	121557.359111
YAL063C	82324.5824206	83710.5695801
YAL062W	100232.91788	238335.704026
YAL061W	92398.82293	217455.526866
YAL060W	78405.2043619	194252.535343
YAL059C-A	81118.0267187	54570.3793915
YAL059W	99701.5638416	185200.781503
YAL058W	98476.3743546	144943.862158
YAL056C-A	86021.6875871	197063.270245
YAL056W	64135.3251631	89310.5203018
YAL055W	92642.5835955	312566.516616
YAL054C	81610.944506	192689.717274
YAL053W	93002.6771963	197350.819283
YAL051W	68014.3468141	96504.8679948
YAL049C	88885.0464234	141912.60533
...
```

**Results visualized with `plot_expression_across_chromosomes.py`:**

![example plot](example_imgs/genes_mock_expression_ratios_across_chr.png)

Image above produced with command:

    python plot_expression_across_chromosomes.py genes.gtf genes_mock_expression_ratios.tsv --smooth

using [plot_expression_across_chromosomes.py found here](https://github.com/fomightez/sequencework/tree/master/plot_expression_across_chromosomes). The file produced by that command calling [plot_expression_across_chromosomes.py](https://github.com/fomightez/sequencework/tree/master/plot_expression_across_chromosomes) is named `genes_mock_expression_ratios_across_chr.png`.  
Results show two disomic chromosomes and a signal suggesting a segmental trisomy.

The amplified segment in the simulated data can be seen better when just looking at Chromosome XVI.

![example chromosome plot](example_imgs/genes_mock_expression_ratios_across_chr_XVI.png)

Image above produced with command:

    python plot_expression_across_chromosomes.py genes.gtf genes_mock_expression_ratios.tsv --lines --chr XVI --advance_color 16 --smooth

If you have a lot images to make for each chromosome, I suggest checking out the two scripts desrcibed [here](https://github.com/fomightez/sequencework/tree/master/plot_expression_across_chromosomes#related), sheperds_chr_thru_plot_expression_across_chromosomes.py and generate_reports_for_genome_and_all_chromosomes_various_samples.py.

Related software by others I have encountered
--------------------------------------------

* [sim.counts: RNA-seq Count Data Simulation from Negative-Binomial distribution](https://rdrr.io/cran/ssizeRNA/man/sim.counts.html) - this R function doesn't seem to allow specifically designating regions to alter levels, but you could probably further edit the simulated data to do that for genes in the region in which you are looking to alter the level relative the baseline.

* [Splatter: Simulation Of Single-Cell RNA-seq](http://www.biorxiv.org/content/early/2017/07/24/133173?rss=1) -  Bioconductor (R) package for simple, reproducible and well-documented simulation of single-cell RNA-seq data. Splatter provides an interface to multiple simulation methods including Splat, based on a gamma-Poisson distribution. Splat can simulate single populations of cells, populations with multiple cell types or differentiation paths.

Related resources
----------------

* [On the importance of controls, even when the tools are computational](http://rnainformation.blogspot.co.nz/2017/07/on-importance-of-controls-even-when.html) by Paul Gardner discusses controls for RNA-Seq data.
