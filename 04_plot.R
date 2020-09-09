#!/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)

layout(matrix(c(1,2,3,4),nr=2, byrow=T))
par(font.main=2,font.sub=1,font.lab=1,font.axis=1,cex.main=1,cex.sub=1,cex.lab=1,cex.axis=1,las=1,bty="l",mgp=c(2.2,0.6,0),bg="white")

file=read.table(args[1],head=FALSE)

plot(file$V1, file$V4,xlim=c(-15,15),type='l', col='blue',cex=1, main="IS plot", xlab="boundary +-150kb", ylab="IS value")

dev.off()

