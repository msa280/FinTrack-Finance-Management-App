import camelot
import zipfile
import pandas as pd
import os

def convert_and_zip(filepath):
    tables = camelot.read_pdf(filepath, pages='1-end', flavor='stream', strip_text='\n')
    print(tables)
    tables.export('statement.csv', f='csv', compress=True)

    all_tables = []

    for table in tables:
        df = table.df
        all_tables.append(df)

    if all_tables:
        combined_table = pd.concat(all_tables, ignore_index=True)
        excel_path = 'statement.xlsx'
        combined_table.to_excel(excel_path, index=False)
        print(f"Combined table exported to {excel_path}")

    df = pd.read_excel('statement.xlsx', sheet_name=0)  # reads the first sheet of your excel file
    df = df[(df['Country'] == 'UK') & (df['Status'] == 'Yes')]  # Filtering dataframe
    df.to_excel('file.xlsx', sheet_name='Filtered Data')  # Saving to a new sheet called Filtered Data

def main():
    filepath = "statement.pdf"
    convert_and_zip(filepath)

main()







