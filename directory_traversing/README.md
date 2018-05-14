#Directory and file traversing demo

Python scripts by Wayne Decatur for demonstrating Directory and file traversing.

Done along the lines of approach requested by Linlin Zhao <linlin.zhao mail at uni-duesseldorf DOT_HERE de> on Biopython list.

- file_hierarchy_simulation_generator.py

>generates a mock directory hierarchy with folders for several organisms containing placeholder mock files like that to be worked with ultimately.



####Dependencies

Nothing but the fairly standard modules such as os.


#### EXAMPLE RUN

TO RUN:
Enter on the command line, the line

	python file_hierarchy_simulation_generator.py



##### OUTPUT

Several folders will be made each harboring two mock fasta files concerning proteins ending in `.ffn` and one mock genome file ending in `.ffa`.

The result is represented as a directory tree the likes of which you can generate with the program or supposed one-liner in the comments [here](http://www.cyberciti.biz/faq/linux-show-directory-structure-command-line/). (Note the one-liner didn't seem to represent the files within the directories when I tried it on PythonAnywhere.)


	+--- a_marina
	|     |
	|     +--- genome.ffa
	|     +--- prot_1.ffn
	|     +--- prot_2.ffn
	|
	+--- b_subtilis
	|     |
	|     +--- genome.ffa
	|     +--- prot_1.ffn
	|     +--- prot_2.ffn
	|
	+--- c_perfringens
	|     |
	|     +--- genome.ffa
	|     +--- prot_1.ffn
	|     +--- prot_2.ffn
	|
	+--- e_coli
	|     |
	|     +--- genome.ffa
	|     +--- prot_1.ffn
	|     +--- prot_2.ffn
	|
	+--- l_acidophilus
	|     |
	|     +--- genome.ffa
	|     +--- prot_1.ffn
	|     +--- prot_2.ffn
	|
	+--- v_parahaemolyticus
	      |
	      +--- genome.ffa
	      +--- prot_1.ffn
	      +--- prot_2.ffn


##### Cleaning up
If you are adapting this script and need to run it several times, you'll need to clean up after each run. I put together three lines that can restore things to the pre-run state farily easily, assuming you have a directory above where you placed this script.

	mv file_hierarchy_simulation_generator.py ../
	rm -rf *
	mv ../file_hierarchy_simulation_generator.py .






- file_hierarchy_processorv0.1.py

> Takes a demo file hierarchy and traverses it, processing the FASTA-formatted sequences of proteins to get coordinates to mine the corresponding genome FASTA-formatted sequence.




####Dependencies
Beyond biopython, only typical modules like os, sys, and fnmatch.

First you should run `file_hierarchy_simulation_generator.py`, and then run the `file_hierarchy_processorv0.1.py` script in the same directory.


#### EXAMPLE RUN

TO RUN, after having run `file_hierarchy_simulation_generator.py` in the saem directory:
Enter on the command line, the line

	python file_hierarchy_processorv0.1.py



##### OUTPUT

A file with text mined from genome of each organism as directed by coordinates of the protein fasta sequences. The sequences are all mock sequences as this is just a demo of the process of traversing the file hierarchy and accessing sequence data with Biopython.





