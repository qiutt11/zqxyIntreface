import common.analyData
from feiqi.getData import getData
from feiqi.operationExcel import operationExcel
from common.analyData import analyData


class getUrlParams:
    def __init__(self,caseId):
        self.rowNum=operationExcel.getRowNum(caseId)
        self.url=getData.getUrl(self.rowNum)
        self.rqMethod = getData.getRequestMthod(self.rowNum)
        self.enData=analyData(caseId).getEncryData()
    def getUrlParams(self):
        #if self.rqMethod=="post" or self.rqMethod=="POST":
        url="http://39.105.137.51:18080"+self.url
        #elif self.rqMethod=='get' or self.rqMethod=="GET":
        #    for k in self.enData.keys():

         #       url="http://39.105.137.51:18080"+k+self.enData[k]
        #return url
