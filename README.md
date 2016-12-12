# variant-caller

TLDR: This project consists of variant call filtering experiments. The primary objective is to attain similar sensitivity/specifity to GATK's VQSR tool without requiring as many modeling assumptions or manual user input.

## Variant Calling and Filtering 

When a gene sequencing pipeline finds evidence of a variant (AKA mutation or SNP), it outpus a "variant call". In practice, one finds that many of these variant calls tend to be false positives. In other words, the genome of interest does not in fact contain the "called" genetic variant. In the dataset I used, approximately 15% of the variant calls are false positives. In order to obtain a variant call set with high sensitivity and specificity, one must attempt to filter out the false positives. This is the goal of my project.

## Dataset

I used variant calls obtained by Illumina reads from chromosome 20 of individual NA12878. Information about how to get the dataset is available on the [Genome Analysis Toolkit (GATK) website](http://gatkforums.broadinstitute.org/gatk/discussion/1213/whats-in-the-resource-bundle-and-how-can-i-get-it).

## GATK Approach

GATK has a variant call filtering tool called [Variant Quality Score Recalibration (VQSR)](http://gatkforums.broadinstitute.org/gatk/discussion/39/variant-quality-score-recalibration-vqsr). In short, VQSR fits a Gaussian Mixture Model to genetic variant data in order to classify proposed variants as true variants or not.

## My Approach

Since we now have access to gold standard variant call datasets, I used such data to train supervised learning algorithms, such as logistic regression, support vector machine, and random forest. I used 10-fold cross validation on a 70% training set to train each model. I then evaluated the models on a 30% held-out test set. See my [Jupyter notebook](https://github.com/nmchaves/variant-call-filter/blob/master/filters/test_multiple_filters.ipynb) for the results of my experiments.
