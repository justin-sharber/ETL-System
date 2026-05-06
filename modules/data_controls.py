## Data Controls

from preamble import *
from get_columns import *

#%% boolean map
'''
A mapping from all recognizable boolean entries.
Maps to 'TRUE' and 'FALSE', which cast to bool in BQ.
All other entries will safe_cast to null, including blanks.
'''

boolMap = {
    'TRUE': 'TRUE',
    'T': 'TRUE',
    'YES': 'TRUE',
    'Y': 'TRUE',
    '1': 'TRUE',
    'FALSE': 'FALSE',
    'F': 'FALSE',
    'NO': 'FALSE',
    'N': 'FALSE',
    '0': 'FALSE',
    }


#%% function
def cast_types(df, dataKey):
    '''
    Casts data types in df according to the data key.
    STRING is the default data type.
    '''
    dk = dataKey
    
    t = 'DATE'
    cols = get_cols(df, dk, t)
    #- Errors-coerce handles garbage data.
    #- Sales trackers have shown mixed formats.  No significant time cost for the parameter.
    df[cols] = df[cols].apply(lambda col: pd.to_datetime(col, errors='coerce', format='mixed'))
    
    t = 'FLOAT'
    cols = get_cols(df, dk, t)
    df[cols] = df[cols].apply(lambda x: pd.to_numeric(x, errors='coerce'))

    t = 'INT'
    cols = get_cols(df, dk, t)
    df[cols] = df[cols].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    df[cols] = df[cols].fillna(0).round().astype(int)

    t = 'BOOL'
    cols = get_cols(df, dk, t)
    df[cols] = df[cols].apply(lambda col: col.str.upper().map(boolMap).fillna(''))
    
    return df
