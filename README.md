# SortSamples
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

A PluMA plugin that accepts as input a TXT file of tab-delimited 
keyword-value pairs.  Keywords:

otufile: CSV file samples and counts, with samples represented as columns
metadata: CSV file of samples and properties (samples are rows)
orderby: Property of metadata to order by

The plugin will then output an equivalent otufile with samples
ordered by the selected property, in CSV format
