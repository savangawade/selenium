import openpyxl
from tabulate import tabulate
filename = r"C:\Users\ADMIN\Desktop\tcorange.xlsx"
workbook = openpyxl.load_workbook(filename)
worksheet = workbook['Sheet1']
non_null_cells_list = []
for row in worksheet.iter_rows(min_row=1, max_col=20, values_only=True):
    non_null_cells = [cell for cell in row if cell is not None]
    if non_null_cells:
        non_null_cells_list.append(non_null_cells)
print(tabulate(non_null_cells_list))



