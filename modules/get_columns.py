## Get columns
import pandas as pd

def get_cols(df, dataKey, typeTerm):
    '''
    Quick helper function for drawing columns from data key.
    '''
    dk = dataKey
    cols = dk[dk.str.contains(typeTerm)].index
    cols = [col for col in cols if col in df.columns]
    return cols
