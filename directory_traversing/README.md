# Directory Making script
 
- file_hierarchy_simulation_generator.py

>generates a mock directory hierarchy with folders for several organisms containing placeholder mock files like that to be worked with ultimately.



#### Dependencies

Nothing but the fairly standard modules such as os.


#### EXAMPLE RUN

TO RUN:
Enter on the command line, the line

	python file_hierarchy_simulation_generator.py



#### OUTPUT

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


#### Cleaning up

If you are adapting this script and need to run it several times, you'll need to clean up after each run. I put together three lines that can restore things to the pre-run state farily easily, assuming you have a directory above where you placed this script.

	mv file_hierarchy_simulation_generator.py ../
	rm -rf *
	mv ../file_hierarchy_simulation_generator.py .


