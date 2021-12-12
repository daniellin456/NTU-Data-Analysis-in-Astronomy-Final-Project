import pandas as pd
from marvin import config
config.setDR('DR16')
from marvin.utils.general import downloadList

df = pd.read_csv('marvin_GOOD_table.csv')
plateifus = df['plateifu']

print( len(plateifus) )
for i in range( 1183, len(plateifus) ):
    
    inputList = []
#    if ( plateifus[i] in bad_plateifus ):
#        continue

    inputList.append( plateifus[i] )
    #downloadList( inputList, dltype='maps', daptype='HYB10-GAU-MILESHC', verbose=True)
    #downloadList( inputList, dltype='cube', daptype='HYB10-GAU-MILESHC', verbose=True)
