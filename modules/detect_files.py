## Detect files
from preamble import *

#- file list loc as global
file_list_fp = utilFolder+'file list.csv'

#%% functions
def read_file_list():
    listA = pd.read_csv(file_list_fp).dropna()
    # - turn to series
    listA = listA[listA.columns[0]]
    return listA
    
    
def glob_files(path=dataFolder):
    '''
    Reads all spreadsheets with recursive glob.
    '''
    g = glob(path+'/**', recursive=True)
    #- only take spreadsheets
    g = [f for f in g if 'csv' in f.lower() or 'xls' in f.lower()]
    #- clean paths
    g = [f.replace("\\", "/") for f in g]

    listB = pd.Series(g).sort_values()
    listB.name = 'Filepaths'
    return listB

#%% test
#g = glob_files()
#len(g)
