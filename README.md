# variant-call-filter

TLDR: This project consists of variant call filtering experiments. The primary objective is to attain similar performance (i.e. precision and recall) to GATK's VQSR tool without requiring as many modeling assumptions or manual user input.

## Variant Calling and Filtering 

When a gene sequencing pipeline finds evidence of a variant (AKA mutation or SNP), it outpus a "variant call". In practice, one finds that many of these variant calls tend to be false positives. In other words, the genome of interest does not in fact contain the "called" genetic variant. In the datasets I used, approximately 10-15% of the variant calls are false positives. In order to obtain a high quality variant call set, one must attempt to filter out the false positives. This is the goal of my project.

## Dataset

I used variant calls obtained by Illumina reads from individual NA12878. Information about how to get the dataset is available on the [Genome Analysis Toolkit (GATK) website](http://gatkforums.broadinstitute.org/gatk/discussion/1213/whats-in-the-resource-bundle-and-how-can-i-get-it). After obtaining the ".vcf" file you want to filter (and the associated ".idx" file), you should run my [preprocessing steps](https://github.com/nmchaves/variant-call-filter/blob/master/preprocessing/multi_chrom/preprocess_VCF.ipynb). This notebook applies VQSR, converts the data to a more convenient table format, selects legitimate numerical features from the data (e.g. it drops features with NaN's), and it scales/normalizes the non-categorical data.

## GATK Approach

GATK has a variant call filtering tool called [Variant Quality Score Recalibration (VQSR)](http://gatkforums.broadinstitute.org/gatk/discussion/39/variant-quality-score-recalibration-vqsr). In short, VQSR fits a Gaussian Mixture Model to genetic variant data in order to classify proposed variants as true variants or not.

## My Approach

Since we now have access to gold standard variant call datasets, I used such data to train supervised learning algorithms, such as logistic regression, support vector machine, and random forest. I've ran several [experiments](https://github.com/nmchaves/variant-call-filter/tree/master/experiments), which are contained in Jupyter notebooks for transparency.
