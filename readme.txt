QBMC: Quantified Bounded Model Checking for Rectangular Hybrid Automata

Authors: Luan Viet Nguyen, Djordje Maksimovic, Taylor T. Johnson, Andreas Veneris

--------------------------------------------------------------------------------

All examples of QBMC, dReach, HyComp are generated from SpaceEx inputs using Hyst:

https://github.com/verivital/hyst

The SMT solver is used in this paper is Z3 via its python API:

https://z3.codeplex.com/


--------------------------------------------------------------------------------

The repository contains:

./readme            	- this file

./spaceex	     	- hybrid automata of all examples in SpaceEx format  

./qbmc             	- a collection of Fischer, Lynch-Shavit and illustrative example using QBMC presented in the paper

./hycomp      		- a collection of Fischer, Lynch-Shavit and illustrative example encoded with a hydi language

./dreach           	- a collection of Fischer, Lynch-Shavit and illustrative example in dReach format

./image			- a collection of all images of the paper and scripts to regenerate them

./run_qbmc.py 		- run all examples of QBMC and output a table of runtimes and memory usages 

--------------------------------------------------------------------------------


1) Example to run QBMC:

python ./qbmc/example/example.py

You can run all examples in a specified folder using run_qbmc.py in Linux. The output will be a table included the runtime and memory usage for each example.

We use memtime to collect data of runtime and memory, and memtime is not supported for Windows.

Example to run QBMC for all examples of Fischer protocol up to k = 8:

python run_qbmc.py -k 8 ./qbmc/Fischer

 
2) For HyComp, we run invariant verification for all examples.

Example to run invariant verification in HyComp:

./hycomp -load path_to_bmc.cmd path_to_examples


3) Example to run dReach up to k = 32:

dReach -k 32 -l 0 ./dreach/example/example.drh 
 

4) Users can download Hycomp and dReach at:

https://es-static.fbk.eu/tools/hycomp/

https://dreal.github.io/


NOTE THAT you need to set appropriate paths to those tools, otherwise they won't run.