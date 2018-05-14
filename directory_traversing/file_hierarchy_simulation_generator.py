#! /usr/bin/env python

# file_hierarchy_simulation_generator.py by Wayne Decatur
# ver 0.1
#
#
#
#*******************************************************************************
# Verified compatible with both Python 2.7 and Python 3.6; written initially in 
# Python 2.7. 
#
#
# PURPOSE: generate fake file hierarchy for testing iterative processing of
# folders containing genome and protein sequence information.
#
# Dependencies:
# Only typical modules like os.
#
# Adjust the 'USER ADJUSTABLE VALUES' to match the settings you need.
#
# v.0.1. Started
#
#
#
# TO RUN:
# For example, enter on the command line terminal, the line
#-----------------------------------
# python file_hierarchy_simulation_generator.py
#-----------------------------------
# Or paste into a Jupyter notbeooks cell and run.
#
#
#*******************************************************************************


##################################
#  USER ADJUSTABLE VALUES        #

##################################
#

directories_to_make = (
    'a_marina',
    'e_coli',
    'b_subtilis',
    'v_parahaemolyticus',
    'c_perfringens',
    'l_acidophilus')

sequences_to_use = (
    '> gi|158303474|gb|CP000828.1|:3233-4009 Acaryochloris marina MBIC11017, complete genome\nATGCTAGGTGCAATTGCATGCTAGGTGCAATTGCATGCTAGGTGCAATTGC',
    '> gi|158303475|gb|CP000829.1|:5233-6009 Acaryochloris marina MBIC11017, complete genome\nATGCTAGGGGCAATTGCCTGCTAGGTGCAATTGCATGCTAGGTGCAATTGC',
    '> gi|758863732|gb|AJO84690.1|:2973916-2975355 nitric oxidase, Escherichia coli, complete genome\nATGAATGTATTAGACTCCAAGCTGGTGTCGCTACTTCGTCAAGA',
    '> gi|758863727|gb|AJO84685.1|:322233-322933 sorbitol-6-phosphate 2-dehydrogenase, Escherichia coli, complete genome\nATGTCGGACAAGGCTTTGCGCGCTGGTGAGGATGGC',
    '> gi|158303474|gb|CP000828.1|:3233-4009 Acaryochloris marina MBIC11017, complete genome\nATGCTAGGTGCAATTGCATGCTAGGTGCAATTGCATGCTAGGTGCAATTGC',
    '> gi|158303475|gb|CP000829.1|:5233-6009 Acaryochloris marina MBIC11017, complete genome\nATGCTAGGGGCAATTGCCTGCTAGGTGCAATTGCATGCTAGGTGCAATTGC',
    '> gi|758863732|gb|AJO84690.1|:2973916-2975355 nitric oxidase, Escherichia coli, complete genome\nATGAATGTATTAGACTCCAAGCTGGTGTCGCTACTTCGTCAAGA',
    '> gi|758863727|gb|AJO84685.1|:322233-322933 sorbitol-6-phosphate 2-dehydrogenase, Escherichia coli, complete genome\nATGTCGGACAAGGCTTTGCGCGCTGGTGAGGATGGC',
    '> gi|158303474|gb|CP000828.1|:3233-4009 Acaryochloris marina MBIC11017, complete genome\nATGCTAGGTGCAATTGCATGCTAGGTGCAATTGCATGCTAGGTGCAATTGC',
    '> gi|158303475|gb|CP000829.1|:5233-6009 Acaryochloris marina MBIC11017, complete genome\nATGCTAGGGGCAATTGCCTGCTAGGTGCAATTGCATGCTAGGTGCAATTGC',
    '> gi|758863732|gb|AJO84690.1|:2973916-2975355 nitric oxidase, Escherichia coli, complete genome\nATGAATGTATTAGACTCCAAGCTGGTGTCGCTACTTCGTCAAGA',
    '> gi|758863727|gb|AJO84685.1|:322233-322933 sorbitol-6-phosphate 2-dehydrogenase, Escherichia coli, complete genome\nATGTCGGACAAGGCTTTGCGCGCTGGTGAGGATGGC'
    )

genomes_to_use = (
    '>gi|158303474|gb|CP000828.1| Acaryochloris marina MBIC11017, complete genome\nAATAAATACTTACAGGTATTCCACCTGAAACTCTTTCTATGAATGACTTTCAAGTCTATATCCTATATTT\nATCCTCAATAAAATATGCACAATAGATCTCTACTGAGAAAACTTTATATTTTAGAAGCAATTCATCTCCC\nTTTTAAAATAC',
    '>gi|26111730|gb|AE014075.1| Escherichia coli CFT073, complete genome\nAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC\nTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAA\nTATAGGCATAGCG',
    '>gi|255767013|ref|NC_000964.3| Bacillus subtilis subsp. subtilis str. 168 chromosome, complete genome\nATCTTTTTCGGCTTTTTTTAGTATCCACAGAGGTTATCGACAACATTTTCACATTACCAACCCCTGTGGA\nCAAGGTTTTTTCAACAGGTTGTCCGCTTTGTGGATAAGATTGTGACAACCATTGCAAGCTCTCGTTTATT\nTTGGTATTAT',
    '>gi|686270189|ref|NZ_JNTW01000020.1| Vibrio parahaemolyticus strain CFSAN001611 CFSAN001611_contig0019, whole genome shotgun sequence\nGCAATTGCTTGGTCTTTTTGTTTCGATTAAGGGCCTAAACAGCTATAAAACCGCTTTTTCTTTATTTTTT\nAGCAGCTTATCCATTTCATCTCGATTCGCGATGAAGGTTGCCATCTCCTTCTTAGGAACAGAGCTCGCCA\nTCGGAATATTTG',
    '>gi|47118322|dbj|BA000016.3| Clostridium perfringens str. 13 DNA, complete genome\nTCTAAATAAGTTTTACACAAAATAAGTTATCAACAGCTGTTATTTTTGTGGATAACTTATTGAATCCAAC\nTATACCTTTATGTTATCATATTAATGCATTGTGAATAACTTTATCTAATATAACAACTTATCCACACTTG\nTGAATAATCCTGTTGAT',
    '>gi|238694164|ref|NZ_GG669567.1| Lactobacillus acidophilus ATCC 4796 SCAFFOLD2, whole genome shotgun sequence\nCTATTGTTGAATTAAAATCGATTTGTTGGAATTCCTTGATTAGTTCAATTATAGATGGTGAAACATTTCC\nTTTTGATTTAGTTGCAATGAAGAAATCAATATAAATTAAACTTTTGTCTATTGGTAATAAATTTATAGGA\nGACTGTTTTATTCG'
    )

#
#*******************************************************************************
#*******************************************************************************




















#*******************************************************************************
#*******************************************************************************
###DO NOT EDIT BELOW HERE - ENTER VALUES ABOVE###



###-----------------Actual Main function of script---------------------------###
# last example at http://pymotw.com/2/ospath/ has a nice example where it makes 
# simple directory heierarchy with files. This is based on that.
import os

for idx, directory in enumerate(directories_to_make):
    os.mkdir(directory)
    file_write_handle = open (directory+"/prot_1.ffn", "w")
    file_write_handle.write(sequences_to_use[(2*idx)+0])
    file_write_handle.close()
    file_write_handle = open (directory+"/prot_2.ffn", "w")
    file_write_handle.write(sequences_to_use[(2*idx)+1])
    file_write_handle.close()
    file_write_handle = open (directory+"/genome.ffa", "w")
    file_write_handle.write(genomes_to_use[idx])
    file_write_handle.close()


#*******************************************************************************
#*******************************************************************************
