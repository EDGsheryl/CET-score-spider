#coding=gbk
import xlwt

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

md = open('out.txt', 'r')

row=2
col=1

for stringmd in md.readlines():
    str= stringmd.split(' ')
    for s in str:
        sheet.write(row,col,s)
        col=col+1
    col=1
    row=row+1
wbk.save('chhulinew.xls')
