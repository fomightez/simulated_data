#!/usr/bin/env python
# mock_expression_ratio_generator.py
__author__ = "Wayne Decatur" #fomightez on GitHub
__license__ = "MIT"
__version__ = "0.2.0"


# mock_expression_ratio_generator.py by Wayne Decatur
# ver 0.2
#
#*******************************************************************************
# Written in Python 2.7 to be compatible with Python 3.
#
# PURPOSE: Wanted a way to generate mock data for illustrating the options in
# the script `plot_expression_across_chromosomes.py` and related scripts.
# Takes all genes in a gtf (or gff) and parses that data and then puts a one to
# one ratio for all the data except chromosome regions marked as having 
# different expression ratio relative baseline. Puts those as random normal
# distributions around that value. Saves the data as a Tab-separated values file
# that can be used by `plot_expression_across_chromosomes.py` and related 
# scripts in conjunction with the gtf file to make plots. Currently, I only have
# real RNA-Seq data with disomy of one yeast chromosome, and strains that seem
# to have the same copy number as wild-type. Using this script I can illustrate 
# what other results, i.e., disomy of more than one chromosomes, trisomy, etc., 
# may sort of look like in the plots.
# There is an option to use only a fraction of the genes to generate mock data.
# That can be useful for workig with large genomes, like human, in order to 
# speed up testing / development of related scripts. Default is one eighth.
#
#
#
#
# Dependencies beyond the mostly standard libraries/modules:
#  
#
#
# VERSION HISTORY:
# v.0.1. basic working version
# v.0.2. refactored main part to speed up & added option to only use fraction.
#
# to do:
# - initially for `ratio_by_region_dictionary` that gets used by `get_ratio_mean` function, I hard-coded it for development phase. NEXT MAKE SO it works with argparse to populate the `get_ratio_mean`-storing dictionary.
# - fully document at github
#
#
#
#
# TO RUN:
# Example,
# Enter on the command line of your terminal, the line
#-----------------------------------
# python mock_expression_ratio_generator.py genes.gtf
#-----------------------------------
#
#
#*******************************************************************************
#





#*******************************************************************************
##################################
#  USER ADJUSTABLE VALUES        #

##################################
#

fraction_to_use = 0.125 #fraction to use when `use_fraction` flag used on command 
# line or when `use_fraction=True` supplied to main function; 1/8 = 0.125 

# `genome_annotation_fields` to match your genome annotation source data. You'll 
# most likely only need one of these. 
genome_annotation_fields_for_gtf = ("seqname", "source", "feature type", "start", 
    "end", "score", "strand", "frame", "attribute")
genome_annotation_fields_for_gff = ("seqname", "source", "feature type", "start", 
    "end", "score", "strand", "frame", "group")
genome_annotation_fields_for_bed = ("chrom", "chromStart", "chromEnd", "name", 
    "score", "strand", "thickStart", "thickEnd", "itemRgb", "blockCount", 
    "blockSizes", "blockStarts")
column_types_for_gff  = {"seqname":'object',
                "source":'object',
                "feature type":'object',
                "start":'int64',
                "end":'int64',
                "score":'object',
                "strand":'object',
                "frame":'object',
                "group":'object',
               }
column_types_for_gtf = {"seqname":'object',
                "source":'object',
                "feature type":'object',
                "start":'int64',
                "end":'int64',
                "score":'object',
                "strand":'object',
                "frame":'object',
                "attribute":'object',
               }

suffix_for_saving_result = "_mock_expression_ratios.tsv"


ratio_by_region_dictionary = {
"I":{(1,230218):2.0}, 
"XII":{(1,107817):2.0, (646906,862541.6):3.0},
"XVI":{(1,98010):3.0},
"7":{(1,159345973):2.0}, 
"11":{(1,135086622):3.0}, 
} # This is a dictionary of dictionaries for each chromosome region that differs
# from a "typical" mean of 1.0 expression ratio realtive the baseline. The keys 
# of the main dictionary are the chromosome or scaffold designations. These 
# have to match with those found in the genome annotation file, 
# (typically `GTF` or `GFF` format). Specifically, it is located in the 
# `seqname` field of the file, see http://www.ensembl.org/info/website/upload/gff.html
# Each subdictionary for each chromosome is composed of a region specified by
# a tuple, that serves as the key for the region, with the values being the 
# mean expression ratio for the region. These values are not checked against
# anything, and so in order to cover the whole chromosome, you can just specify
# an outrageously high value.

#
#*******************************************************************************
#**********************END USER ADJUSTABLE VARIABLES****************************













#*******************************************************************************
#*******************************************************************************
###DO NOT EDIT BELOW HERE - ENTER VALUES ABOVE###

import sys
import os
import argparse
import pandas as pd
import numpy as np
import random



###---------------------------HELPER FUNCTIONS---------------------------------###

def generate_output_file_name(file_name, suffix):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    It also indicates in resulting file name name specific chromosomes or 
    scaffolds if plotting was limited to those.

    Specific example
    ================
    Calling function with
        ("data1.txt", "_across_chr.png")
    returns
        "data1_across_chr.png"

    '''
    main_part_of_name, file_extension = os.path.splitext(
        file_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    return main_part_of_name + suffix



def extract_gene_ids(row):
    '''
    parses out the gene_id from the attributes list in a line in annoation file 
    formatted in Ensembl format, for example Ensembl-formatted yeast genome from 
    ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Saccharomyces_cerevisiae/Ensembl/R64-1-1/Saccharomyces_cerevisiae_Ensembl_R64-1-1.tar.gz
    Here the annotation file has been read in as a pandas dataframe and the 
    `attributes` field is in column 9, specified by `row.iloc[8]` in the code.
    Using that instead of the column name because not called attributes list
    in the gff format but it has `group` field at same position.

    takes a row of a pandas dataframe derived from an annotation file

    returns a string of the systematic gene id
    '''
    return row.iloc[8].split("gene_id")[1].split('"')[1].strip()

def calculate_position(row):
    '''
    takes a row of pandas dataframe derived from an annotaion file & calculates 
    the average position of a gene or feature along the chromosome by taking the
    average of the start and end

    returns an integer
    '''
    return (int(row["start"]) + int(row["end"]))/2



def checkIfRomanNumeral(numeral):
    """
    Controls that the userinput only contains valid roman numerals
    function from praveen's answer at 
    https://stackoverflow.com/questions/20973546/check-if-an-input-is-a-valid-roman-numeral
    """
    numeral = numeral.upper()
    valid_roman_numerals = ["M", "D", "C", "L", "X", "V", "I", "(", ")"]
    valid = True
    for letters in numeral:
        if letters not in valid_roman_numerals:
            #print("Sorry that is not a valid roman numeral")
            valid = False
            break
    return valid

def int_to_roman(input):
    """
    from Paul Winkler's http://code.activestate.com/recipes/81611-roman-numerals/
    (had to reindent; was causing text editor to default to wrong spacing
    otherwise. Plus updated some idioms too.)
    Convert an integer to Roman numerals.

    Examples:
    >>> int_to_roman(0)
    Traceback (most recent call last):
    ValueError: Argument must be between 1 and 3999

    >>> int_to_roman(-1)
    Traceback (most recent call last):
    ValueError: Argument must be between 1 and 3999

    >>> int_to_roman(1.5)
    Traceback (most recent call last):
    TypeError: expected integer, got <type 'float'>

    >>> for i in range(1, 21): print int_to_roman(i)
    ...
    I
    II
    III
    IV
    V
    VI
    VII
    VIII
    IX
    X
    XI
    XII
    XIII
    XIV
    XV
    XVI
    XVII
    XVIII
    XIX
    XX
    >>> print int_to_roman(2000)
    MM
    >>> print int_to_roman(1999)
    MCMXCIX
    """
    if type(input) != type(1):
        raise TypeError ("expected integer, got {0}".format(type(input)))
    if not 0 < input < 4000:
        raise ValueError ("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i,e in enumerate(ints):       #formerly `for i in range(len(ints))`
        count = int(input / e) #formerly `count = int(input / ints[i])`
        result += nums[i] * count
        input -= e * count #formerly `input -= ints[i] * count`
    return result

def roman_to_int_if_possible(input):
    """
    modified from Paul Winkler's roman_to_int at
    http://code.activestate.com/recipes/81611-roman-numerals/
    (had to reindent; was causing text editor to default to wrong spacing
    otherwise. Plus updated some idioms too.)

    Try to convert a roman numeral to an integer. 
    Return original input if not possible.
    """
    #if type(input) != type(""):
    #   raise TypeError, "expected string, got %s" % type(input)
    input = input.upper()
    nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    ints = [1000, 500, 100, 50,  10,  5,   1]
    places = []
    for c in input:
        if not c in nums:
            #raise ValueError, "input is not a valid roman numeral: %s" % input
            return input
    for i,e in enumerate(input):  #formerly `for i in range(len(input)):`
        c = e #formerly `c = input[i]`
        value = ints[nums.index(c)]
        # If the next place holds a larger number, this value is negative.
        try:
            nextvalue = ints[nums.index(input[i +1])]
            if nextvalue > value:
                value *= -1
        except IndexError as e:
            # there is no next place.
            pass
        places.append(value)
    sum = 0
    for n in places: sum += n
    # Easiest test for validity...
    if int_to_roman(sum) == input:
        return sum
    else:
        #raise ValueError, 'input is not a valid roman numeral: %s' % input
        return input
    
def seqname_roman_to_numeric(row):
    '''
    takes a row of pandas dataframe derived from an annotaion file and attempts 
    to convert the seqname value in roman numeral form to a numeric

    returns an integer if able to convert; 
    returns original value if unable to convert
    '''
    return roman_to_int_if_possible(row["seqname"])


def seqname_string_to_numeric(row):
    '''
    takes a row of pandas dataframe derived from an annotaion file and attempts 
    to convert the seqname value in string form to a numeric

    returns an integer if able to convert; 
    returns original value if unable to convert
    '''
    try:
        return int(row["seqname"])
    except ValueError as e:
        return row["seqname"]  

def nonneg_random_norm_distr(number):
    '''
    generator for normal distribution
    '''
    while True:
        rn = np.random.normal(loc=number, scale=0.4)
        if rn >= 0.000:
            yield rn
        else:
            yield -rn

def decision(probability):
    '''
    from https://stackoverflow.com/questions/5886987/true-or-false-output-based-on-a-probability
    '''
    return random.random() < probability

def get_noisy_value(ratio_mean):
    '''
    generator to add some noise to some values coming from a generator for 
    normal distribution centered on the ratio mean.
    '''
    normal_distribution_val = next(nonneg_random_norm_distr(ratio_mean))
    if decision(0.0012):
        # print ("...making some noise now..") #for debugging 
        return normal_distribution_val +  random.uniform(1,10) # I picked adding
        # because it seemed without noise a good range of values with log2 below
        # the centered number but not above.
    else:
        return normal_distribution_val

def overlap(a,b):
    '''
    tells if two tuples, representing ranges overlap.

    Examples
    -------
    >>>overlap((10, 20) (15, 25))
    True
    >>>>overlap((10, 20) (25, 55))
    False

    based on 
    https://bytes.com/topic/python/answers/457949-determing-whether-two-ranges-overlap
    '''

    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]

def get_ratio_mean_for_region(row):
    '''
    function to use the ratio_by_region_dictionary to get mean ratio for regions
    that are in regions on the chromosomes or scaffolds that vary from baseline.

    returns a float that will be used as mean ratio 

    somewhat based on Vinicide's answer at
    https://www.reddit.com/r/learnprogramming/comments/3ikao1/python_best_way_to_map_a_range_of_numbers_to_a/
    and 
    Robin Haswell's answer at 
    https://bytes.com/topic/python/answers/457949-determing-whether-two-ranges-overlap
    '''
    ratio_by_region_dict = ratio_by_region_dictionary[row["seqname"]]
    for region in ratio_by_region_dict:
        if overlap((region[0], region[1]),(row["start"],row["end"])):
            return ratio_by_region_dict[region]
    # if no overlap with any region, the ratio mean for the gene or feature is 
    # assumed to be 1.0 because same as baseline.
    return 1.0


def get_ratio_value(row):
    '''
    takes a row of pandas dataframe derived from an annotaion file and gets the
    expression value to set in the "level_val" column.

    returns a float that will be in most likely normal distribution around the
    mean ratio for expression in that chrosome region. It may beyond that 
    distribution because I'd like to add a low level of noise to closer
    approximate real data.
    '''
    if row["seqname"] in ratio_by_region_dictionary:
        # next,determine if current gene or feature would be in the region that
        # has a expression mean ratio that deviates from the baseline 1.0
        ratio_mean = get_ratio_mean_for_region(row)
        # use that ratio mean to get a noisy value
        return get_noisy_value(ratio_mean)
    else:
        # if not in the `ratio_by_region_dictionary`, the ratio mean is assumed
        # to be 1.0 because same as baseline
        return get_noisy_value(1.0)


def make_mock_expression_values(row):
    '''
    takes a row of pandas dataframe derived from an annotaion file, where the
    expression ratio, has been added as `level_val` and uses that to calculate
    some mock data values for the wild-type(baseline) and experimental strain

    returns a dataframe row (series) with two values added:
    first value is the wild-type(baseline) value
    second is the experimental strain values
    '''
    random_val = random.uniform(63764,100671)
    row["mock_base"] = random_val
    row["mock_exp"] = random_val * row["level_val"]
    return row


###--------------------------END OF HELPER FUNCTIONS-------------------------###
###--------------------------END OF HELPER FUNCTIONS-------------------------###






#*******************************************************************************
###------------------------'main' function of script--------------------------##

def mock_expression_ratio_generator(annotaton_file, use_fraction=False, 
    fraction_to_use=fraction_to_use):
    '''
    Main function of script. 

    Simplisitcally makes data that can be used as input for the script 
    `plot_expression_across_chromosomes.py`.
    Allows for generating different relative ratios for regions and chromosomes.

    You can set `use_fraction` to `True` and only a random fraction of the genes
    to generate mock data. Useful with large genomes, like human, in order to
    speed up testing other scripts where mock data is used for development.

    The default fraction is 0.125 , a.k.a, an eighth. However, `fraction_to_use`
    can be supplied when calling the main function with `use_fraction=True`. If 
    using the script on the command line then edit `fraction_to_use` under 
    'USER ADJUSTABLE VALUES' before running it.
    '''
    # ANNOTATION FILE ACCESSING AND GENOME DATAFRAME INITIAL PREPARATION
    # Because it is very related and a good approach, this essentially just
    # follows the initial code of `plot_expression_across_chromosomes.py`
    # open annotation file and make it a Pandas dataframe
    sys.stderr.write("\nReading annotation file and getting data on genes and "
        "chromosomes...")
    #determine if annotation is gff or gtf
    if "gff" in annotaton_file.name.lower():
        col_names_to_apply = genome_annotation_fields_for_gff 
        column_types = column_types_for_gff

    if "gtf" in annotaton_file.name.lower():
        col_names_to_apply = genome_annotation_fields_for_gtf 
        column_types = column_types_for_gtf


    # read in annotation file
    init_genome_df = pd.read_csv(
        annotaton_file, sep='\t', header=None, low_memory=False,
        names=col_names_to_apply, comment='#',dtype=column_types) # comment handling 
    # added because I came across gtfs with a header that had `#`  at start of each 
    # line. Others must have encountered same because I saw someone dealing with it 
    # at https://github.com/shenlab-sinai/ngsplotdb/pull/2/files. I cannot use that 
    # solution since I use Pandas read_csv function. (`read_table`) was 
    # deprecated recently. dtypes added when speed and working with large files
    # became an issue, see 
    # https://github.com/fomightez/sequencework/issues/1#issuecomment-465760222
    # When I tested timing lines using yeast data (gtf; 12 Mb) and 
    # https://stackoverflow.com/a/14452178/8508004, I found it slightly faster
    # (0.42 vs 0.50) with `low_memory=False`, and so that is why that is used. I 
    # suspect the difference would be even starker with the 1.4 Gb human GTF. I only 
    # ended up seeing it get this far with the because I used `sys.exit(1)` to stop 
    # it after the read.
    #(LATER: When just read of human gtf timed in a notebook with `%%time`, with 
    # `low_memory=False` it took only 1 min 10s whereas it was 4min 44s when 
    #`True`. That effort with human data was done running in Cyverse. Oddly, on
    # Cyverse it turned out never to take that long again when `True`, usually
    # disparity only about 40 seconds.)

    #sys.stderr.write("...parsing genes...") # There is no point in this because I 
    # found stderr , for reasons I don't understand, although have seen similar when
    # working in notebooks, won't output after pandas read starts even though with 
    # yeast gtf (12 Mb) that read is almost instantaneous (see timing above.) 

  

    # Parse out gene_ids from attribute or group, i.e., 9th column in the annotation 
    # file.

    #init_genome_df = (init_genome_df[init_genome_df[init_genome_df.columns[-1]].
        #str.contains("gene_id")]) #for yeast and human this doesn't seem to 
        # remove anything and so there is no point trying to use it to limit to
        # pertinent rows.

    init_genome_df["gene_id"] = init_genome_df.apply(extract_gene_ids, axis=1)

    # Next want to end up with one entry per gene with the start and end 
    # coordinates. I was originally doing this using the code in docstring below 
    # but  efficiency became an issue when someone tried with human data. And
    # I recalled learning appending can be very infficient, see 
    # https://stackoverflow.com/a/31713471/8508004 and Tinkerbeast's comment at 
    # https://stackoverflow.com/a/25376997/8508004 . So code after doesn't
    # use `.append` and accomplishes the same outcome with more pythonic
    # pandas-based steps.
    '''
    # copy each row to a new dataframe, unless gene already present. 
    # This wil give me unique gene_ids for each and I can make that index.
    # Because it takes first occurence of each gene, it only has that as start and
    # end. Then to get the full range of data for start and end for each gene, I can
    # subset the initial dataframe on each gene_id and get the min and max and use
    # those values to replace `start` and `end` for the new dataframe. For those
    # on Crick strand, it will turn around the start, end information, but that is
    # fine since just want an avg relative position and don't care about direction.
    genome_df = pd.DataFrame(columns=init_genome_df.columns)
    for i, row in init_genome_df.iterrows():
        if not any(genome_df.gene_id == row.gene_id):
            genome_df = genome_df.append(row)
    genome_df = genome_df.set_index('gene_id')
    for id in list(genome_df.index.values):
        sub_df = init_genome_df.loc[init_genome_df["gene_id"] == id]
        min_val = min(sub_df[["start","end"]].min()) # `sub_df["start","end"].min()` 
        # gives values for the two columns and so min() of that gives single 
        #value
        max_val = max(sub_df[["start","end"]].max())
        genome_df.loc[id, "start"] = min_val
        genome_df.loc[id, "end"] = max_val

    # provide feedback on number of unique genes identified
    sys.stderr.write("Information for {0} genes parsed...".format(len(genome_df)))
    # calculate average position
    # genome_df["position"] = genome_df[["start","end"]].apply(np.mean, axis=1) # gives float and I'd prefer as integer
    genome_df["position"] = genome_df.apply(calculate_position, axis=1)
    # make a column of chrosomes as numbers, either converting from the string 
    # they would be by default (I think?) or converting from roman numerals. 
    # This will be used for sorting later
    # First determine if chromosomes are numbers with X and Y (and others?) or 
    # ifin the form of roman numerals
    chromosomes_in_roman_num = False
    # check if majority look like integers. If that is the case verify most are 
    # valid roman numerals just to be sure.
    seqname_set = set(genome_df['seqname'].tolist())
    chromosomes_in_roman_num = not bool(len([s for s in seqname_set if s.isdigit()]) > len(seqname_set)/2) #checks if most chromosomes seem to be digits and says they are roman numerals if that is false
    if chromosomes_in_roman_num:
        most_valid_rom_numerals = bool(len([n for n in seqname_set if checkIfRomanNumeral(n)]) > len(seqname_set)/2)
        # provide feedback if don't seem to be roman numerals
        if not most_valid_rom_numerals:
            sys.stderr.write("***WARNING***The chromosomes seem to not be in "
                "numeric form, but most aren't valid roman numerals "
                "either.***WARNING***....")
        else:
            sys.stderr.write("The chromosomes appear to be in roman numeral "
                "form....")
    else:
        sys.stderr.write("The chromosomes appear to be in numeric form....")
    # Second, convert if `chromosomes_in_roman_num` otherwise just try to coerce 
    # string to integer, allowing not to coerce and not throw an error in case 
    # of the sex chromosomes
    if chromosomes_in_roman_num:
        # try and convert each row but allow for non type change without error
        genome_df["chr_as_numeric"] = genome_df.apply(
            seqname_roman_to_numeric, axis=1)
    else:
        genome_df["chr_as_numeric"] = genome_df.apply(
            seqname_string_to_numeric, axis=1)
    longest_chr_or_scaffold = len(max(seqname_set, key=len))
    # Prepare genome dataframe for adding the mock data by adding a column for 
    # relative level and fill with 'NaN'
    genome_df["level_val"] = np.nan
    '''
    # Use groupby and `.agg()` to get min and max. Then move the multi-index
    # dataframe produced to single index, where gene_id is the index, and the
    # 'seqname' gets moved from hierarchical index to a column.
    genome_df = init_genome_df.groupby(
        ["gene_id","seqname"]).agg({'start': 'min','end': 'max'}) 
    genome_df = genome_df.reset_index(level=['seqname']) #based on 
    # https://stackoverflow.com/a/20461206/8508004 . Note that I later realized 
    # I could have also just used `
    # genome_df = init_genome_df.groupby(["gene_id"]).agg({"seqname":'first','start': 'min','end': 'max'})`
    # to do the aggregating and level reset as well. Don't know yet why `first` 
    # needs quotes but I tried and it worked based on seeing `first in use at 
    # https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/ .
    # (Noting this thoroughly here b/c gist snippets points here for `groupby`.)
    # provide feedback on number of unique genes identified
    sys.stderr.write("Information for {0} genes parsed.."
        ".".format(len(genome_df)))

    # limit to a fraction if `use_fraction` indicated
    if use_fraction:
        from sklearn.model_selection import train_test_split
        train, test = train_test_split(
        genome_df, test_size = fraction_to_use)
        genome_df = test
        sys.stderr.write("\nBecause `use_fraction` indicated, {0} genes will be "
            "used in total...".format(len(genome_df)))


    # calculate average position
    # genome_df["position"] = genome_df[["start","end"]].apply(np.mean, axis=1) # gives float and I'd prefer as integer
    genome_df["position"] = genome_df.apply(calculate_position, axis=1)






    # For ease and consistency between the related scripts, add the mock data to 
    # the "level_val" column that is made in the course of the initial part of 
    # script `plot_expression_across_chromosomes.py`
    sys.stderr.write("\nFilling in the mock values for each gene...")
    genome_df["level_val"] = genome_df.apply(get_ratio_value, axis=1)


    # Now make mock data for the base and experimental based on the ratio needed
    genome_df = genome_df.apply(make_mock_expression_values, axis=1) # based on 
    # Nelz1's answer at 
    # https://stackoverflow.com/questions/23586510/return-multiple-columns-from-apply-pandas
    # because couldn't use approach I used for `genome_df["level_val"] = genome_df.apply(get_ratio_value, axis=1)`
    # since need to make multiple columns for result and couldn't do leaving off
    # `axis=1` because want a different random value for each row and not one for
    # the entire column (although probably would have been fine mostly for here)



    # Write the gene id and mock levels to a Tab-separated values text file
    extracted_df = genome_df[['mock_base','mock_exp']].copy() # based on http://stackoverflow.com/questions/34682828/pandas-extracting-specific-selected-columns-from-a-dataframe-to-new-dataframe ,
    # see `Process of making median and mean TPM tables for NMD targets.md`
    output_file_name = generate_output_file_name(annotaton_file.name, suffix_for_saving_result)
    extracted_df.to_csv(output_file_name, sep='\t',index = True) 
    sys.stderr.write( "\nMock data saved as: {}\n".format(output_file_name))

###--------------------------END OF MAIN FUNCTION----------------------------###
###--------------------------END OF MAIN FUNCTION----------------------------###










#*******************************************************************************
###------------------------'main' section of script---------------------------##
def main():
    """ Main entry point of the script """
    # placing actual main action in a 'helper'script so can call that easily 
    # with a distinguishing name in Jupyter notebooks, where `main()` may get
    # assigned multiple times depending how many scripts imported/pasted in.
    kwargs = {}
    #if df_save_as_name == 'no_pickling':
    #   kwargs['pickle_df'] = False
    kwargs['use_fraction'] = use_fraction
    #kwargs['return_df'] = False #probably don't want dataframe returned if 
    # calling script from command line
    mock_expression_ratio_generator(annotaton_file,**kwargs)
    # using https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/#calling-a-function
    # to build keyword arguments to pass to the function above
    # (see https://stackoverflow.com/a/28986876/8508004 and
    # https://stackoverflow.com/a/1496355/8508004 
    # (maybe https://stackoverflow.com/a/7437238/8508004 might help too) for 
    # related help). Makes it easy to add more later.





if __name__ == "__main__" and '__file__' in globals():
    """ This is executed when run from the command line """
    # Code with just `if __name__ == "__main__":` alone will be run if pasted
    # into a notebook. The addition of ` and '__file__' in globals()` is based
    # on https://stackoverflow.com/a/22923872/8508004
    # See also https://stackoverflow.com/a/22424821/8508004 for an option to 
    # provide arguments when prototyping a full script in the notebook.
    ###-----------------for parsing command line arguments-------------------###
    import argparse
    parser = argparse.ArgumentParser(prog='mock_expression_ratio_generator.py',
    description="mock_expression_ratio_generator.py is an acessory script to \
    generate mock data for plotting with plot_expression_across_chromosomes.py.\
    **** Script by Wayne Decatur   \
    (fomightez @ github) ***")

    parser.add_argument("annotation", help="Name of file containing the genome \
    annotation. REQUIRED. This is needed to determine the order of individual \
    data points along the chromosome and how to display the data across \
    chromosomes or scaffolds.", 
    type=argparse.FileType('r'), metavar="ANNOTATION_FILE")

    parser.add_argument("-uf", "--use_fraction", help="Add this optional flag \
        if using a large GTF/GFF file, such as 1.4 Gb human GTF, and want \
        only use a random fraction of the genes to speed up generation of mock \
        data and any subsequent applications of that mock data. Default is to \
        use one eighth of the data and that value be adjusted by editing \
        `fraction_to_use` under 'USER ADJUSTABLE VALUES' in the script\
        .",action="store_true")



    #I would also like trigger help to display if no arguments provided because 
    #need at least one input file
    if len(sys.argv)==1:    #from http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    annotaton_file = args.annotation
    use_fraction = args.use_fraction


    main()

#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
