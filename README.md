# Insulation_Score
For running those scripts, some files are needed:
1)TADs file, eg, TADs_boundary.bed_example
2)chromosomes size file, eg, chrom.sizes.hg38.filter
3)bin interactions from dump or sth else, with Chr, eg, dump_observed_example
So, first step is calculate IS within whole genome, then extract the boundaries values and plot. 
# calculate whole genome IS
python 01_Calculate_Insulation_Score.py chrom.sizes.file  dump_observed.file output binsize window
binsize usually 10000, window usually 120000, but you can set whatever the binsize and window you want to try. just be careful binsize(means positions) in all files should be compatible to each other.
From this step you already get the value what you need, you can plot them by your own amazing scripts, but if you want to use following not smart but useful scripts... ok.
# make boundaries to plot
python 02_makeboundary.py TADs.file outfile binsizesize window
binsize usually same as first step, 10000, window is the left and right region of the TADs you want to show, usually 150000
this step is stupid, just easy for me, I will improve it ... in future
this step just extract all the positions what I need, nothing else.
# extract IS for positions 
python 03_boundaryValue2Plot.py boundary_file_from_second_step IS_score_from_first_step outfile

# Plot 
./04_plot.R outfile_from_03

Good luck!
