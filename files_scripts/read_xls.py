import xlrd

book = xlrd.open_workbook('../resources/file_example_XLS_10.xls')
print(book.nsheets)
print(book.sheet_names())


