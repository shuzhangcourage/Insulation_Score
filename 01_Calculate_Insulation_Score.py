#!/bin/python

""" Usage: python 01_Calculate_Insulation_Score.py chrom.sizes.file  dump_observed.file output binsize window"""

import sys
from sys import argv
import math

chromosize=open(sys.argv[1])
observed=open(sys.argv[2])
output=open(sys.argv[3],'w')
binsize=int(sys.argv[4]) #usually use 10000
window=int(sys.argv[5]) #usually use 120000

def Insulation_score():

	dict_whole={} ## list all subkeys within a key
	dict_bin={} ## sum the value of all subkeys
	dict_window={} ## all subkeys
	dict_chr={} ## chromosom

	for eachline in chromosize:
		line=eachline.strip().split()
		if line[0] not in dict_chr:
			dict_chr[line[0]]=[0,0]
		for i in range(0,int(line[1]),binsize):
			key=line[0]+":"+str(i)
			dict_whole[key]=[]
			dict_bin[key]=[0,0]
			if i-window>=0 and i+binsize+window<=int(line[1]):
				for x in range(i-window,i,binsize):
					for y in range(i+binsize,i+binsize+window,binsize):
						subkey=line[0]+":"+str(x)+":"+str(y)
						dict_whole[key].append(subkey)
						if subkey not in dict_window:
							dict_window[subkey]=0

	##add observed to each region 			
	for eachline in observed:
		line=eachline.strip().split()
		if line[0]+":"+line[1]+":"+line[2] in dict_window and line[3] != "NaN":
			key=line[0]+":"+line[1]+":"+line[2]
			dict_window[key]=float(line[3])
	##calculate IS				
	for i in dict_whole:
		for j in dict_whole[i]:
			if dict_window[j]!=0:
				dict_bin[i][0]+=1
				dict_bin[i][1]+=dict_window[j]
	##calculate IS_avg
	for i in dict_bin:
		key=i.split(":")[0]
		dict_chr[key][0]+=1
		dict_chr[key][1]+=dict_bin[i][1]
	##calculate normalize IS
	for i in dict_bin:
		Chr=i.split(":")[0]
		averageChr=dict_chr[Chr][1]/dict_chr[Chr][0]
		IS=dict_bin[i][1]
		if IS<12:
			w=Chr+"\t"+i.split(":")[1]+"\t"+"None"+"\n"
			output.write(w)	
		if IS>=12:
			Score=IS/averageChr
			IS_normalize=math.log(Score,2)
			w=Chr+"\t"+i.split(":")[1]+"\t"+str(IS_normalize)+"\n"
			output.write(w)
	return 

#exe
Insulation_score()			
