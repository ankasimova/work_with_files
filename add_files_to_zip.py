from zipfile import ZipFile
import os
from PyPDF2 import PdfReader

zip_object = ZipFile('sample.zip', 'w')
zip_object.write('files_for_zip/docs-pytest-org-en-latest.pdf')
zip_object.write('files_for_zip/file_example_XLSX_50.xlsx')
zip_object.write('files_for_zip/report.csv')

zip_object.close()

source_files = '/Users/vladkim/Desktop/qaguru_work_with_files/sample.zip'
destination_folder = '/Users/vladkim/Desktop/qaguru_work_with_files/resources/sample.zip'
os.rename(source_files, destination_folder)

# Show list of files in .zip
zip_ = ZipFile('../resources/sample.zip')
print(zip_.namelist())

# Read PDF







