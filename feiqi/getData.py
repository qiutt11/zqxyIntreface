from feiqi.operationExcel import operationExcel
from feiqi import dataConfig


#from common.opeartion_json import OperatiobJson

class getData():
    def __init__(self):
        self.operaExcel=OperationExcel()

    def getCaseLines(self):
        self.rowNum=self.operaExcel.getRows()

    #获取url
    def getUrl(self,row):
        col=int(dataConfig.getUrl())
        url=self.operaExcel.getCellValue(row,col)
        return col

    #是否执行
    def getIsRun(self,row):
        flag=None
        col=int(dataConfig.getRun())
        runModle=self.operaExcel.getCellValue(row,col)
        if runModle=='yes':
            flag=True
        else:
            flag=False
    #请求方式
    def getRequestMthod(self,row):
        col=int(dataConfig.getRequestMethod())
        reMethod=self.operaExcel.getCellValue(row,col)
        return reMethod
    #请求数据
    def getData(self,row):
        col=int(dataConfig.getData())
        data=self.operaExcel.getCellValue(row,col)
        return data

    #预期结果
    def getExcept(self,row):
        col=int(dataConfig.getExcept())
        exceptData=self.operaExcel.getCellValue(row,col)
        return exceptData


    #写入结果
    def WriteValue(self,row):
        col=int(dataConfig.getResult())
        self.operaExcel.write_value(row,col,value)

