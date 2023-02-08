import pandas as pd

def compare_excel_spreadsheets(file1, file2):
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    df_diff = df1 != df2
    diff_locations = df_diff.stack()
    changed = diff_locations[diff_locations]
    changed.index.names = ['Row', 'Column']
    result = pd.DataFrame({'Original': df1.stack()[changed.index],
                           'New': df2.stack()[changed.index]},
                         index=changed.index)
    result.to_excel('differences.xlsx')

compare_excel_spreadsheets('file1.xlsx', 'file2.xlsx')

