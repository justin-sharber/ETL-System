## Clean columns
from string import punctuation

#%%
def cleaner(cols):
    '''
    Cleans df columns.
    Replaces all non-letter characters with underscores.
    '''
    s = cols
    s = s.str.strip()
    s = s.str.replace(' ', '_')
    for p in punctuation:
        s = s.str.replace(p, '_')#.str.replace('__','_')
    return s
