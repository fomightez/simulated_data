# mock_expression_ratio_generator.py

> The purpose behind `mock_expression_ratio_generator.py` is to generate mock data for illustrating the options in
the script `plot_expression_across_chromosomes.py` and related scripts.

`mock_expression_ratio_generator.py` takes all genes in a gtf (or gff) and parses that data and then puts a one to
one ratio for all the data except chromosome regions marked as having 
different expression ratio relative baseline. Puts those as random normal
distributions around that value. Saves the data as a Tab-seperated values file
that can be used by `plot_expression_across_chromosomes.py` and related 
scripts in conjunction with the gtf file to make plots. Currently, I only have
real RNA-Seq data with disomy of one yeast chromosome, and strains that seem
to have the same copy number as wild-type. Using this script I can illustrate 
what other results, i.e., disomy of more than one chromosomes, trisomy, etc., 
may sort of look like in the plots.






Related
-------

[sim.counts: RNA-seq Count Data Simulation from Negative-Binomial distribution ](https://rdrr.io/cran/ssizeRNA/man/sim.counts.html)
