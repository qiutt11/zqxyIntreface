import time
import re
#from feiqi.operationExcel import operationExcel
#from feiqi.getData import getData
from common.logger import logger
from common.encryptData import encryptData
import json
from data import readConfig

class analyData():
    def __init__(self,data):
        self.data = data
        #logger.get_logger(self.data)
        #caseData=self.data
        #print(self.data)
        self.user=readConfig.readConfig()
        self.logger=logger
        caseData=json.loads(self.data)
        baseData={"app_key":self.user.get_user('app_key'),"digital_signature":"","timestamp":""}
        caseData=self.joindict(caseData,baseData)
        self.sortData=dict(sorted(caseData.items(), key=lambda x: x[0]))
        print("加密前请求数据：%s" % self.sortData)
        self.logger.info("加密前的请求数据：{}".format(self.sortData))
    def getEncryData(self):
        md5str = self.user.get_user('appSecret')
        for k in self.sortData.keys():
            if k == "timestamp":
                self.sortData[k] = re.findall('^\d{13}', str(time.time()).replace('.', ''))[0]
            elif k == 'digital_signature':
                pass
            elif k == "app_key":
                self.sortData[k] = self.user.get_user('app_key')
            else:
                self.sortData[k] = encryptData().encrypt(self.sortData[k])
                pass
        for k in self.sortData.keys():
            if k=="digital_signature":
                pass
            else:
                md5str=md5str+k+self.sortData[k]
        digital_signature=encryptData().getMd5(md5str)
        self.sortData["digital_signature"]=digital_signature
        return self.sortData

    def joindict(self,dict1,dict2):
        dict3={}
        for k,v in dict1.items():
            dict3[k]=v
        for k,v in dict2.items():
            if k not in dict3.keys():
                dict3[k]=v
        return dict3



if __name__ == '__main__':
    caseData='{"ent_name":"湖州云海房地产开发有限公司"}'
    a='1'
    e=analyData(caseData)
    d=e.getEncryData()
    #print(c)
    print(d)







