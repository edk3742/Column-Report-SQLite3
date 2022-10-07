# %%
import pandas as pd
import re

#convert design table textfile to a dataframe
df = pd.read_csv('Pages from Axial Capacity.txt', sep='\t',error_bad_lines=False)

#search thru the design tables file to find import indices
depths = df.loc[df['Start'].str.contains('Shape W',na=False)] 
wt_index = [i+1 for i in depths.index]
wt_index_cap = [i+5 for i in depths.index]

wt_list = [i.split(' ') for i in df.iloc[wt_index]['Start']]

#reformat wt_list into list of lists
res = [list(map(lambda sub:''.join(
      [ele for ele in sub if ele.isnumeric()]), i)) for i in wt_list]

#reformat depths to W14,W12,etc.
depths = depths['Start'].tolist()
depths=[ele.split(" ")[1] for ele in depths]
depths = list(map(lambda x: x[:-1],depths))

#change res such that the first index is the section depth
#and the entries are the plf weights, typical AISC naming convention
for newVal, subList in zip(depths, res):
    subList[0] = newVal


capacities = df.loc[df['Start'].str.contains('ASD LRFD ASD',na=False)] 
capacities_start_index = [i+1 for i in capacities.index]
capacities_end = df.loc[df['Start'].str.contains('Properties',na=False)] 

def phicpn(design_shapes:str,height:int):
    '''
    design_shapes is a list of sections i.e. ['W14X176','W14X120']
    height is an integer from 0-20 and 22-40 by two's, see Table 4-1 in the steel manual
    
    output is a dataframe of the shape and capacity
    '''
    shape_cap = []
    shape_nam = []
    for i in design_shapes:
        xsects = re.split('X',i,flags=re.IGNORECASE)
        for idx,val in enumerate(res):
            if val[0]==xsects[0] and xsects[1] in val[1:]:
                phic_idx=(idx)
                phic_index=(res[idx].index(xsects[1]))
                df_subframe = df[capacities_start_index[phic_idx]:capacities_end.index[phic_idx]]
                df_subframe = df_subframe["Start"].str.split(" ").apply(lambda x: [float(i) for i in x])
                for idx,val in enumerate(df_subframe):
                    if val[0] == height or val[0]>height:
                        shape_nam.append(i)
                        shape_cap.append(val[phic_index*2])
                        break
    data_tuples = zip(shape_nam,shape_cap)
    phicpn_table = pd.DataFrame(data_tuples,columns=['AISC_Manual_Label','Cap'])
    return phicpn_table



# %%
