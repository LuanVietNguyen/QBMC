# This script will run all qbmc example 
# Luan Nguyen, August 2014
# command: e.g -- python run_qbmc -k 10 ./qbmc/Fischer


import os
import sys
import subprocess
import shutil
import fileinput
from tabulate import tabulate
import re

arglist = sys.argv;
#print arglist;
if arglist[1] == "-k":
	k =  arglist[2]
else:
	k = "8";
EXAMPLES_PATH = arglist[3]

def runFiles(filepath):
	table = [];
	files = os.listdir(filepath);
	for f in files:
		if f.endswith(".py"):
			filepath = EXAMPLES_PATH + "/" + f;
			replaceKvalue(filepath,"k = ",k); 
			command = "memtime python " + EXAMPLES_PATH + "/" + f;
			#print command;
			process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE ,shell=True);

			out,error = process.communicate();
			output = out + error;
			rv = [];
			rv.append(f);
			rv.append(str(k));
			#print s;
			# add values into table
			table.append(parseValues(output, rv));
			sys.stdout.flush();
			sys.stderr.flush(); 
		#print table
	print tabulate(table, headers=["Example", "k", "Time", "RSS Memmory"]);


# parse elapsed time, memmory usage for each input file
def parseValues(stream, value):
	for line in stream.splitlines():
		if "Max RSS" in line:
			#print line;
			ls =  line.split();
			for i in range(0, len(ls)):
				#print ls[i]; 
				if ls[i] == "elapsed":
					value.append(ls[i-1] + "s");
			value.append(ls[len(ls) - 1]);	
	return value;

# replace k value in each file
def replaceKvalue(filename,searchExp,replaceExp):
    	for line in fileinput.input(filename, inplace=1):
		if searchExp in line:
	    	#line = line.replace(searchExp,replaceExp)
			line = re.sub(r'\d+', replaceExp,line)
		sys.stdout.write(line)


def main():
	if os.path.isdir(EXAMPLES_PATH):
		runFiles(EXAMPLES_PATH);
	else:
		print "the folder can't be found";

if __name__== '__main__':
	main()



				
