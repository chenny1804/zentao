import xlrd
from xlutils.copy import copy
import time
def write_to_xls(strs,row,col):
    rb=xlrd.open_workbook("chariot_test.xls")
    wb=copy(rb)
    ws=wb.get_sheet(0)
    ws.write(row,col,strs)
    wb.save("chariot_test.xls")
def get_max_rows():
    rb=xlrd.open_workbook("chariot_test.xls")
    rs=rb.sheet_by_index(0)
    return rs.nrows
def get_max_cols():
    rb=xlrd.open_workbook("chariot_test.xls")
    rs=rb.sheet_by_index(0)
    return rs.ncols
if __name__=="__main__":
    row=get_max_rows()
    print row
    col=get_max_col()
    print col
    write_to_xls(str(time.strftime('%Y-%m-%d %H:%M:%S')),row,0)
