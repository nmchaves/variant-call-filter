"""
import vcf
vcf_reader = vcf.Reader(open('data/VQSRfilter/NA12878.LowSeq.illumina.bwa.sorted.dedup.20.sam.wFlag.qual.raw.snps.vqsr.recal.vcf', 'r'))
print vcf_reader
print len(vcf_reader)
#for record in vcf_reader:
#    print record
"""
from sets import Set
import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt


def plot_embedding(embedding):
    """
    Plot a 2-dimensional embedding of a dataset
    :param embedding: The embedding
    :return: None
    """
    print 'plotting'
    fig, ax = plt.subplots(figsize = (10,10))
    #for i,group in df.groupby(colorby):
    #    group.plot(x='DIM1',y='DIM2',kind='scatter',label=i,color=colors[color],title=plot_title,ax=ax)
    #    color = color + 1
    plt.plot(embedding[:,0], embedding[:,1], 'bo')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.show()


def get_feature_names(df):
    row_info = df['INFO'][0].split(';')
    feature_names = Set([])
    for (key, val) in parse_attributes(row_info):
        feature_names.add(key)
    return list(feature_names)


def parse_attributes(attributes):
    for attr in attributes:
        if "=" in attr:
            [key, val] = attr.split('=')
            yield (key, val)


def num_header_lines(filename):
    num_headers = 0
    with open(filename) as f:
        for line in f:
            if line[0] == "#":
                num_headers += 1
            else:
                break
    return num_headers


def features_from_VCF(filename):
    """
    Generate a Pandas dataframe from a VCF file
    :param filename: Path to the VCF file
    :return: Pandas dataframe containing features for each record in VCF
    """

    # For now, ignore non-numeric columns
    ignore_cols = {'DB', 'POSITIVE_TRAIN_SITE', 'culprit'}

    df = pd.read_csv(filename, sep='\t')
    num_rows = df.shape[0]
    feature_names = get_feature_names(df)
    features = pd.DataFrame(np.zeros(shape=(num_rows, len(feature_names))), columns=feature_names)
    #row_info = df['INFO'][0]
    for index, row in df.iterrows():
        attrs = row['INFO'].split(';')
        for (key, val) in parse_attributes(attrs):
            if key in feature_names and key not in ignore_cols:
                # TODO: This is NOT the correct/robust way to handle this case. This is the case where the
                # location has multiple calls (e.g. heterozygosity for example). For now, just take the first
                # attribute for simplicity
                if ',' in val:
                    val = val.split(',')[0]
                features.set_value(index, key, val)

            passed_VQSR = row['FILTER']
        if passed_VQSR != 'PASS':
            print passed_VQSR

    return features

"""
if __name__ == "main":
    print 'a'
    features = features_from_VCF('data/VQSRfilter/NA12878.LowSeq.illumina.bwa.sorted.dedup.20.sam.wFlag.qual.raw.snps.vqsr.recal copy.vcf')

    print 'Obtained features'

    model = TSNE(n_components=2, random_state=0)
    embedding = model.fit_transform(features[:100])
    plot_embedding(embedding)

    print 'b'

    features.to_csv('test6.txt', sep='\t')
"""
print 'a'
features = features_from_VCF('data/VQSRfilter/NA12878.LowSeq.illumina.bwa.sorted.dedup.20.sam.wFlag.qual.raw.snps.vqsr.recal copy.vcf')

print 'Obtained features'
"""
model = TSNE(n_components=2, random_state=0)
embedding = model.fit_transform(features[:100])
plot_embedding(embedding)
"""
print 'b'

#features.to_csv('test6.txt', sep='\t')



