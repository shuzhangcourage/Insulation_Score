#!/bin/python

"""usage python 03_boundaryValue2Plot.py boundaryfilefrom02*.py ISscorefrom1*.py outfile"""
import sys
import os

boundaryfile=open(sys.argv[1])
ISfile=open(sys.argv[2])
outfile=open(sys.argv[3],"w")

def extract():
	dict1={}
	dict2={}
	list1=[]
	for eachline in boundaryfile:
		line=eachline.strip().split()
		key=':'.join([line[0],line[1],line[2]])
		dict1[key]=[line[3],0]
		if line[3] not in dict2:
			dict2[line[3]]=[0,0]
			list1.append(int(line[3]))
	for eachline in ISfile:
		line=eachline.strip().split()
		key=':'.join([line[0],line[1],str(int(line[1])+10000)])
		if key in dict1:
			if line[2]!="None":
				dict1[key][1]=line[2]
	for i in dict1:
		if float(dict1[i][1])!=0:
			dict2[dict1[i][0]][0]+=float(dict1[i][1])
			dict2[dict1[i][0]][1]+=1
	list1.sort()
	for j in list1:
		j=str(j)
		#w=j+"\t"+str(dict2[j][0])+"\t"+str(dict2[j][1])+"\t"+str(dict2[j][0]/dict2[j][1])+"\n"
		w=j+"\t"+str(dict2[j][0]/dict2[j][1])+"\n"
		outfile.write(w)

extract()

