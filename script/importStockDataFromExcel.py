from xlrd import open_workbook
wb = open_workbook('/home/ganesh/Downloads/kalpatru-1.xlsx')
from stock.models import Stock

for s in wb.sheets():
    rows=s.nrows

    for row in range(1,rows):
        rowValues = []
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            rowValues.append(value)
        print rowValues

        stkObj=Stock()
        stkObj.type=str(rowValues[0])
        stkObj.company_Name=str(rowValues[0])
        # stkObj.supply_Place=str(rowValues[1])
        # stkObj.bill_No=str(rowValues[1])
        # stkObj.bill_Date=str(rowValues[1])
        # stkObj.bill_Rec_Date=str(rowValues[1])
        # stkObj.bill_Amount=str(rowValues[1])
        # stkObj.lr_No=str(rowValues[1])
        # stkObj.lr_Date=str(rowValues[1])
        # stkObj.cases=str(rowValues[1])
        # stkObj.carriers_Name=str(rowValues[1])
        # stkObj.permit_No=str(rowValues[1])
        # stkObj.doc_Month=str(rowValues[1])
        # stkObj.F_C_O=str(rowValues[1])
        # stkObj.date=str(rowValues[1])
        # stkObj.qrt=str(rowValues[1])
        # stkObj.year=str(rowValues[1])
        # stkObj.remarks=str(rowValues[1])
        # stkObj.commodity=str(rowValues[1])
        stkObj.save()


