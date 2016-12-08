import pandas as pd

def read(filename, drop_chrom_pos=True, drop_alt=True, drop_ref=True,
                  drop_nonnumeric_data=True, drop_VQSR_output=True):
    data = pd.read_csv(filename, sep='\t')
    data = data.drop(['CHROM'], axis=1)
    data = data.drop(['FILTER'], axis=1)
    data = data.drop(['ID'], axis=1)
    data = data.drop(['sample1.GT'], axis=1)
    data = data.drop(['sample1.PL'], axis=1)
    data = data.drop(['sample1.AD'], axis=1)
    #data = data.drop(['FORMAT'], axis=1)
    data = data.drop(['MQ0'], axis=1)
    #data = data.drop(['sample1'], axis=1)
    if drop_chrom_pos:
        data = data.drop(['POS'], axis=1)
    if drop_ref:
        data = data.drop(['REF'], axis=1)
    if drop_alt:
        data = data.drop(['ALT'], axis=1)
    #if drop_nonnumeric_data:
    #    data = data.drop([], axis=1)
    #if drop_VQSR_output:
    #    data = data.drop(['PASSED_VQSR', 'VQSLOD'], axis=1)
    return data