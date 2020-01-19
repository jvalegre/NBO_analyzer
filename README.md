# NBO_analyzer
Python script that exports Wiberg bond orders from NBO calculations to a file. Multiple bond orders can be chosen.

Instructions:

First, copy all the log files with the Wiberg bond orders results from NBO calculations to the same folder where NBO_analyzer.py is contained.

Then, write one of these command lines:

1) For only 1 bond:

python NBO_analyzer.py --append NAME --bond1 X,Y *.log


2) For more than 1 bond (up to 4 bonds):

python NBO_analyzer.py --append NAME --bond1 X1,Y1 --bond2 X2,Y2 --bond3 X3,Y3 --bond4 X4,Y4 *.log 


By default, the text file generated is called "NBO_analysis_append", where --append specifies the append name.


Example command line for 4 bonds generating the file "NBO_analysis_michael_addtn":

python NBO_analyzer.py --append Michael_addtn --bond1 3,15 --bond2 6,7 --bond3 7,15 --bond4 7,22 *.log 
