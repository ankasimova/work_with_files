from zipfile import ZipFile

zip_ = ZipFile('../resources/hello.zip')
print(zip_.namelist())

zip_.extract('Hello.txt')