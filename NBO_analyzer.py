#!/usr/bin/python
from __future__ import print_function

#Python Libraries
import os.path, sys
from glob import glob
from decimal import Decimal
from optparse import OptionParser

#Read molecule data from an input file
class getoutData:
    def __init__(self, file):
        if not os.path.exists(file):
            print(("\nFATAL ERROR: Input file [ %s ] does not exist"%file))

        def getwibergBO(self):
            self.WBObond1, self.WBObond2, self.WBObond3, self.WBObond4, self.file_list = [],[],[],[],[]
            for file in files:
                start=0
                start2=0
                infile = open(file,"r")
                inlines = infile.readlines()
                columnbond1 = 0
                # Recognizes the first bond
                for i in range(0,len(inlines)):
                    if inlines[i].find("Wiberg bond index matrix ") > -1:
                        start = i+2
                        break
                for j in range(start,len(inlines)):
                    if inlines[j].find("Wiberg bond index") > -1:
                        break
                    elif inlines[j].find("Atom") > -1 and inlines[j].find(' '+str(options.bond1.split(',')[0])+' ') > -1:
                        column_WBO = 0
                        for k in inlines[j].split():
                            if str(k) == str(options.bond1.split(',')[0]):
                                columnbond1 = column_WBO
                                start2 = j
                            else:
                                column_WBO = column_WBO + 1
                for j in range(start2,len(inlines)):
                    if inlines[j].find("Wiberg bond index") > -1:
                        break
                    if len(inlines[j].split()) >= 1:
                        if inlines[j].split()[0] == (str(options.bond1.split(',')[1])+'.'):
                            self.WBObond1.append(inlines[j].split()[columnbond1+1])
                            break

                # Recognizes the second bond
                if options.bond2 != "False":
                    for i in range(0,len(inlines)):
                        if inlines[i].find("Wiberg bond index matrix ") > -1:
                            start = i+2
                            break
                    for j in range(start,len(inlines)):
                        if inlines[j].find("Wiberg bond index") > -1:
                            break
                        elif inlines[j].find("Atom") > -1 and inlines[j].find(' '+str(options.bond2.split(',')[0])+' ') > -1:
                            column_WBO2 = 0
                            for k in inlines[j].split():
                                if str(k) == str(options.bond2.split(',')[0]):
                                    columnbond2 = column_WBO2
                                    start2 = j
                                else:
                                    column_WBO2 = column_WBO2 + 1
                    for j in range(start2,len(inlines)):
                        if inlines[j].find("Wiberg bond index") > -1:
                            break
                        if len(inlines[j].split()) >= 1:
                            if inlines[j].split()[0] == (str(options.bond2.split(',')[1])+'.'):
                                self.WBObond2.append(inlines[j].split()[columnbond2+1])
                                break

                # Recognizes the third bond
                if options.bond3 != "False":
                    for i in range(0,len(inlines)):
                        if inlines[i].find("Wiberg bond index matrix ") > -1:
                            start = i+2
                            break
                    for j in range(start,len(inlines)):
                        if inlines[j].find("Wiberg bond index") > -1:
                            break
                        elif inlines[j].find("Atom") > -1 and inlines[j].find(' '+str(options.bond3.split(',')[0])+' ') > -1:
                            column_WBO3 = 0
                            for k in inlines[j].split():
                                if str(k) == str(options.bond3.split(',')[0]):
                                    columnbond3 = column_WBO3
                                    start2 = j
                                else:
                                    column_WBO3 = column_WBO3 + 1
                    for j in range(start2,len(inlines)):
                        if inlines[j].find("Wiberg bond index") > -1:
                            break
                        if len(inlines[j].split()) >= 1:
                            if inlines[j].split()[0] == (str(options.bond3.split(',')[1])+'.'):
                                self.WBObond3.append(inlines[j].split()[columnbond3+1])
                                break

                # Recognizes the fourth bond
                if options.bond4 != "False":
                    for i in range(0,len(inlines)):
                        if inlines[i].find("Wiberg bond index matrix ") > -1:
                            start = i+2
                            break
                    for j in range(start,len(inlines)):
                        if inlines[j].find("Wiberg bond index") > -1:
                            break
                        elif inlines[j].find("Atom") > -1 and inlines[j].find(' '+str(options.bond4.split(',')[0])+' ') > -1:
                            column_WBO4 = 0
                            for k in inlines[j].split():
                                if str(k) == str(options.bond4.split(',')[0]):
                                    columnbond4 = column_WBO4
                                    start2 = j
                                else:
                                    column_WBO4 = column_WBO4 + 1
                    for j in range(start2,len(inlines)):
                        if inlines[j].find("Wiberg bond index") > -1:
                            break
                        if len(inlines[j].split()) >= 1:
                            if inlines[j].split()[0] == (str(options.bond4.split(',')[1])+'.'):
                                self.WBObond4.append(inlines[j].split()[columnbond4+1])
                                break
                if start != 0:
                    self.file_list.append(file)
                print(file,start)
        getwibergBO(self)

class writeGinput:
    def __init__(self, file, MolSpec, args):
        f = open('NBO_analysis'+'_'+options.append+'.txt',"w")
        for point in range(len(MolSpec.file_list)):
            print("   ", MolSpec.file_list[point], '' ">>", MolSpec.file_list[0].split('.')[0]+'_'+options.append+'.txt')
            print_bonds = ''
            for i in range(len(bonds_to_analyze)):
                if bonds_to_analyze[i] != 'False':
                    print_bonds += bonds_to_analyze[i] + '    '
        f.write('Bonds to analyze:    ' + print_bonds + '\n')
        f.write('Wiberg bond orders:\n')
        for i in range(len(MolSpec.WBObond1)):
            f.write('                     ' + MolSpec.WBObond1[i])
            if options.bond2 != "False":
                f.write('   ' + MolSpec.WBObond2[i])
            if options.bond3 != "False":
                f.write('   ' + MolSpec.WBObond3[i])
            if options.bond4 != "False":
                f.write('   ' + MolSpec.WBObond4[i])
            f.write('     ' + MolSpec.file_list[i]+"\n")

if __name__ == "__main__":
    parser = OptionParser(usage="Usage: %prog [options] <input1>.log <input2>.log ...")
    parser.add_option('--append', action="store", default="new", help='Append text to create new filenames')
    parser.add_option('--bond1', action="store", default="False", help='X1,X2 - Bond to analyze with NBO')
    parser.add_option('--bond2', action="store", default="False", help='X3,X4 - Bond to analyze with NBO')
    parser.add_option('--bond3', action="store", default="False", help='X5,X6 - Bond to analyze with NBO')
    parser.add_option('--bond4', action="store", default="False", help='X7,X8 - Bond to analyze with NBO')

    (options, args) = parser.parse_args()

    # Get the filenames from the command line prompt
    files = []
    if len(sys.argv) > 1:
        for elem in sys.argv[1:]:
            try:
                if os.path.splitext(elem)[1] in [".out", ".log"]:
                    for file in glob(elem): files.append(file)
            except IndexError: pass
    else:
        print("\nNo files were found.\n")
        sys.exit()

    # Takes arguments: (1) file(s) (2) new job parameters
    for file in files:
        bonds_to_analyze = []
        if options.bond1 != False:
            bonds_to_analyze.append(options.bond1)
        else:
            print("\nNo bonds were specified.\n")
        if options.bond2 != False:
            bonds_to_analyze.append(options.bond2)
        if options.bond3 != False:
            bonds_to_analyze.append(options.bond3)
        if options.bond4 != False:
            bonds_to_analyze.append(options.bond4)
    MolSpec = getoutData(file)
    writeGinput(file, MolSpec, options)
