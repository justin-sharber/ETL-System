## Prep file
from base_modules import *

def prepFile(dataInfo, fp):
    '''
    Core ETL function.  Operates on individual file level.
    
    Parameters:
        dataInfo - pd Series, contaning parameters from master list.
        fp - file path of the spreadsheet to load.
    '''
    info = dataInfo
    fn = fp.split('/')[-1]
    
    #- dataframe
    df = readFile(fp, info)
    df.columns = cleaner(df.columns)
    df = supplementData(df, info, fn)

    #- data key
    dk0 = read_data_key(info, slim=False)
    dk0.Column = cleaner(dk0.Column)
    dk = dk0.set_index('Column').DataType
    
    #- data controls
    df = standardizeColumns(df, dk)
    df = cast_types(df, dk)
    df = dropDelimiters(df, dk)    
    
    #- Fill nulls in key columns for sql merge
    keys = get_key_columns(dk0)
    df[keys] = df[keys].fillna('')
    
    #- import data
    schema = get_schema(dk)
    bqImport(df, info, schema)
    bq_query_from_file(info)
    
    return df

