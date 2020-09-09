# Insulation_Score
For running those scripts, some files are needed:
1)TADs file
2)chromosomes size file
3)bin interactions from dump or sth else, with Chr

python 01_Calculate_Insulation_Score.py chrom.sizes.file  dump_observed.file output binsize window
python 02_makeboundary.py TADs.file outfile binsizesize window
python 03_boundaryValue2Plot.py boundaryfilefrom02*.py ISscorefrom1*.py outfile
./04_plot.R input
