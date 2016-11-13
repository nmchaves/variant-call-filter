import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
from sets import Set


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

def features_from_VCF(filename):
    """
    Generate a Pandas dataframe from a VCF file
    :param filename:
    :return: The Pandas dataframe
    """
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
                features.set_value(index, key, val)

    return features

df = features_from_VCF('data/VQSRfilter/small_test.txt')
df.to_csv('test4.txt', sep='\t')