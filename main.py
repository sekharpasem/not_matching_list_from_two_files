import pandas as pd

sm_data_df = pd.read_excel('./not_matching_list_from_files.xlsx')
dump_data_df = pd.read_excel('./db_dump_sm_data.xlsx')

mergedStuff = pd.merge(sm_data_df, dump_data_df, on=['CRE DOMAIN ID'], how='inner')
not_matching_list = []
for i, row in mergedStuff.iterrows():
    if row['Reporting Manager Domain_x'] != row['Reporting Manager Domain_y']:
        not_matching_list.append(row)

final_df = pd.DataFrame(not_matching_list)
final_df.to_excel('not_matching_list.xlsx', index=False)
