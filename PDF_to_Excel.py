import tabula
from tabula.io import read_pdf
import pandas as dp


path_of_pdf = input("Please enter the path of your PDF file :")

DataFrame = tabula.io.read_pdf(path_of_pdf, pages='all')

if DataFrame:
    for i, df in enumerate(DataFrame):
        df.to_excel(f'ConvertedExcel_{i}.xlsx', index=False)
    print(f"Excel file(s) Generated successfully. Please Check at pdf location")
else:
    print("No tables found in the PDF.")
