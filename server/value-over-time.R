#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

if (length(args) != 3) {
    stop("Usage: value-over-time.R <interaction> <logfile> <graph>", call.=FALSE)
}

infile = args[2]
outfile = args[3]

data <- read.table(infile,header=FALSE, sep=",")
colnames(data) <- c("timestamp_raw","host","application","interaction","value")
data$timestamp = as.POSIXct(strptime(data$timestamp_raw, "%Y-%m-%dT%H:%M"))

# using first arg to match all interactions using that prefix
plotdata = subset(data, grepl(glob2rx(paste(args[1],"*", sep='')), interaction), select=c("interaction","value","timestamp"))

# factor for color mapping
plotdata$interaction_factor = factor(plotdata$interaction)

my_grey = rgb(46, 46, 46, 255, NULL, 255)
my_red = rgb(179, 32, 32, 255, NULL, 255)
my_colors = c(my_grey,my_red)

# and output
png(outfile)
plot(plotdata$timestamp,plotdata$value,main=args[1],xlab="time",ylab="value",pch=20,col=my_colors[plotdata$interaction_factor])
dev.off()
