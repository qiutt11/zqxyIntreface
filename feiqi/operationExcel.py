import xlrd
import os

class operationExcel:
    def __init__(self,filename=None,sheetId=None):
        if filename:
            self.filename=filename
            self.sheetId=sheetname
        else:
            self.filename="../data/company.xlsx"
            self.path=os.path.join(os.path.abspath(os.path.dirname(__file__)),self.filename)
            self.sheetId=0
        self.data=self.getData()

    #获取sheet内容
    def getData(self):
        data=xlrd.open_workbook(self.path)   ##打开excel文件并创建对象存储
        tables=data.sheets()[self.sheetId]   ##获取sheeetID的内容
        return tables

    def getSheetData(self):
        cls=[]
        data=xlrd.open_workbook(self.path)   ##打开excel文件并创建对象存储
        tables=data.sheets()[self.sheetId]   ##获取sheeetID的内容
        nrows=tables.nrows
        for i in range(nrows):
            if tables.row_values(i)[0]!="caseId":
                cls.append(tables.row_values(i))

        return cls
    @property
    #获取单元格行数
    def getRows(self):
        tables=self.data
        return tables.nrows()

    #获取单元格的数据
    def getCellValue(self,row,col):
        return self.data.cell_value(row,col)


    #根据对应的caseId找到相应的行号
    def getRowNum(self,caseId):
        num=0
        colsData=self.getRowValue()
        for colData in colsData:
            if caseId in colData:
                return num
            num+=1


    #根据行号找到该行内容
    def getRowValue(self,row):
        tables=self.data
        rowData=tables.row_values()
        return rowData


    #获取某一列的内容
    def getColValue(self,colId=None):
        if colId!=None:
            colData=self.data.col_values()
        else:
            colData=self.data.col_values(0)
        return colData

    def writeValue(self,row,col):
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)






