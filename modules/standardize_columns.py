## Control column order
import pandas as pd

def standardizeColumns(df, dk):
    '''
    Standardizes columns against a data key.
    Fixes case.
    Creates missing columns w nulls.
    Reorders columns.
    '''
    
    df = df.rename(columns=str.lower)

    #- spam missing columns
    lowerCols = dk.index.str.lower()
    for col in lowerCols:
        if col not in df.columns:
            #print('spamming', col)
            df[col] = pd.NA

    #- slice - reorder
    df = df[lowerCols].copy()

    df.columns=list(dk.index)
    
    return df
