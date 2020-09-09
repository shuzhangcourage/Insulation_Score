#!/binsize/bash

"""usage python 02_makeboundary.py TADs.file outfile binsizesize window"""
import sys

boundary=open(sys.argv[1])
out=open(sys.argv[2],'w')
binsize=int(sys.argv[3]) #same as your IS's binsize, 10000
window=int(sys.argv[4]) #150000 left and right region of boundary you want to show
n=int(window/binsize)

def makeboundary():
	for eachline in boundary:
		line=eachline.strip().split()
		for i in range(0,n,1):
			if i==0:
				w=line[0]+"\t"+line[1]+"\t"+str(int(line[1])+10000)+"\t"+"0"+"\n"
				out.write(w)
				w=line[0]+"\t"+line[2]+"\t"+str(int(line[2])+10000)+"\t"+"0"+"\n"
				out.write(w)
			else:
				w=line[0]+"\t"+str(int(line[1])+i*binsize)+"\t"+str(int(line[1])+i*binsize+binsize)+"\t"+str(i)+"\n"
				out.write(w)
				w=line[0]+"\t"+str(int(line[2])+i*binsize)+"\t"+str(int(line[2])+i*binsize+binsize)+"\t"+str(i)+"\n"
				out.write(w)
				w=line[0]+"\t"+str(int(line[1])-i*binsize-binsize)+"\t"+str(int(line[1])-i*binsize)+"\t"+str(-1*i)+"\n"
				out.write(w)
				w=line[0]+"\t"+str(int(line[2])-i*binsize-binsize)+"\t"+str(int(line[2])-i*binsize)+"\t"+str(-1*i)+"\n"
				out.write(w)
	return

makeboundary()
