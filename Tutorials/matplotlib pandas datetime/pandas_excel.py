Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> file = pd.ExcelFile("C:\Users\Sai Ganesh\Desktop\Python\Python\Section 4")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file = pd.ExcelFile(r"C:\Users\Sai Ganesh\Desktop\Python\Python\Section 4")

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    file = pd.ExcelFile(r"C:\Users\Sai Ganesh\Desktop\Python\Python\Section 4")
  File "C:\Python38\lib\site-packages\pandas\io\excel\_base.py", line 824, in __init__
    self._reader = self._engines[engine](self._io)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_xlrd.py", line 21, in __init__
    super().__init__(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_base.py", line 353, in __init__
    self.book = self.load_workbook(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_xlrd.py", line 36, in load_workbook
    return open_workbook(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\xlrd\__init__.py", line 111, in open_workbook
    with open(filename, "rb") as f:
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\Sai Ganesh\\Desktop\\Python\\Python\\Section 4'
>>> file = pd.ExcelFile(r"C:\Users\Sai Ganesh\Desktop\Python\Python\Section 4")

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    file = pd.ExcelFile(r"C:\Users\Sai Ganesh\Desktop\Python\Python\Section 4")
  File "C:\Python38\lib\site-packages\pandas\io\excel\_base.py", line 824, in __init__
    self._reader = self._engines[engine](self._io)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_xlrd.py", line 21, in __init__
    super().__init__(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_base.py", line 353, in __init__
    self.book = self.load_workbook(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_xlrd.py", line 36, in load_workbook
    return open_workbook(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\xlrd\__init__.py", line 111, in open_workbook
    with open(filename, "rb") as f:
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\Sai Ganesh\\Desktop\\Python\\Python\\Section 4'
>>> file = pd.ExcelFile(r"C:\Users\Sai Ganesh\Desktop\Python\Python\Section 4\original.xlsx")
>>> print(file.sheet_names)
['sales', 'customers']
>>> sheet = file.parse("sales")
>>> print(sheet)
        Date             Customer  Invoice  Amount
0 2018-12-01  Steel Brothers Inc.       98    1340
1 2018-12-10             MMC Inc.       99    1900
2 2018-12-12             MMC Inc.      100    2900
3 2018-12-18  Steel Brothers Inc.      101     977
4 2018-12-21     Steel & Iron LLC      102    3400
>>> type(sheet)
<class 'pandas.core.frame.DataFrame'>
>>> print(sheet.Date)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-18
4   2018-12-21
Name: Date, dtype: datetime64[ns]
>>> sheet.Amount.sum()
10517
>>> sheet.loc[0]
Date        2018-12-01 00:00:00
Customer    Steel Brothers Inc.
Invoice                      98
Amount                     1340
Name: 0, dtype: object
>>> sheet.loc[0,"Amount"]
1340
>>> sheet.set_index("Customer",inplace = True)
>>> sheet.loc["MMC Inc."]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
MMC Inc. 2018-12-12      100    2900
>>> sheet = sheet.reset_index()
>>> sheet["Invoice"]
0     98
1     99
2    100
3    101
4    102
Name: Invoice, dtype: int64
>>> type(sheet["Invoice"])
<class 'pandas.core.series.Series'>
>>> sheet.loc[sheet["Amount"] > 2000]
           Customer       Date  Invoice  Amount
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet.loc[sheet["Invoice"] == 99]
   Customer       Date  Invoice  Amount
1  MMC Inc. 2018-12-10       99    1900
>>> sheet.loc[sheet["Amount"].idxmax{}]
SyntaxError: invalid syntax
>>> sheet.loc[sheet["Amount"].idxmax()]
Customer       Steel & Iron LLC
Date        2018-12-21 00:00:00
Invoice                     102
Amount                     3400
Name: 4, dtype: object
>>> sheet.loc[sheet["Amount"].idxmax()]["Customer"]
'Steel & Iron LLC'
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"]
1            MMC Inc.
2            MMC Inc.
4    Steel & Iron LLC
Name: Customer, dtype: object
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"].unique()
array(['MMC Inc.', 'Steel & Iron LLC'], dtype=object)
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"].unique()[0]
'MMC Inc.'
>>> for customer in sh:eet.loc[sheet["Amount"] > 1800]["Customer"].unique():
	
SyntaxError: invalid syntax
>>> for customer in sh:eet.loc[sheet["Amount"] > 1800]["Customer"].unique():
	
SyntaxError: invalid syntax
>>> for customer in sheet.loc[sheet["Amount"] > 1800]["Customer"].unique():
	print(customer)

	
MMC Inc.
Steel & Iron LLC
>>> 