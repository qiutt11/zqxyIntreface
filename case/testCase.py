import json
import unittest,sys
from common import analyData,assertRs,runMethod,logger,analyJson
from common.logger import logger
from common.retry import retry_handler
#from common.runMethod import runMethod
#from common.analyData import analyData
#import paramunittest
#from common.getUrlParams import  getUrlParams
import urllib.parse
from data import doExcel,readConfig
from library import ddt


sheetName=sys.argv[1]
sheetId=sys.argv[2]
baseUrl=sys.argv[3]

d=doExcel.doExcel(sheetName,sheetId) #带上模块名，不然会报错
data1 = d.getData()
@ddt.ddt
class testInterface(unittest.TestCase):
    @ddt.data(*data1)
    def test_(self,A):
        """
        test report description
        :return:
        """
        # print("测试用例数据：%s"%aaaa)
        caseId = A['caseId']
        interface = A['interface']
        url=A['url']
        isRun=A['isRun']
        method=A['method']
        data=A['data']
        expected=A['expected']
        exceptlist=list(expected.split(','))
        #url=self.config.get_http("service")+url
        if isRun.lower()=='yes':
            self.logger.info("*********************************执行{}开始***********************".format(interface))
            url = baseUrl + url
            print("请求url地址：{}；请求方式:{}".format(url,method))
            self.logger.info("请求url地址：{};请求方式{}".format(url,method))
            requestData=analyData.analyData(data).getEncryData()
            print('加密后的请求数据：%s'%requestData)
            self.logger.info('加密后的请求数据：{}'.format(requestData))
            res = self.runMethod.runRequest(method, url, requestData)
            print("接口返回数据：%s"%res)
            self.logger.info('{}接口返回数据：{}'.format(interface,res))
            errCode=res['err_code']
            if errCode=="200":
                code=self.analyJson.getkey_value(res,"code")
                if self.assertRs.isIn(code,exceptlist):
                    flag=True
                else:
                    flag=False
            elif errCode=='-1002':
                errMsg = res['err_msg']
                if errMsg=="图片大小不能小于5K":
                    flag=True
                else:
                    flag=False
            else:
                flag=False
            self.assertEqual(flag, True)
             # 取文件中的True和用例跑出来的True对比，做期望值
            # print str(login_result)
              # 实际结果为bool值，转成字符串与期望结果做对比
        else:
            pass

    # @retry_handler(retry_time=3, retry_interval=5, retry_on_exception=[AssertionError,IndexError])
    # def test_retry(self):
    #     self.run(self,A)
    #     print('AssertionError,重试')
    #     self.logger.info('失败重试')

    def setUp(self):
        """
        :return:
        """
        print("******************测试开始前准备*******************")
        self.runMethod = runMethod.runMethod()
        self.logger = logger
        self.assertRs = assertRs.assertRs()
        self.config = readConfig.readConfig()
        self.analyJson=analyJson.analyJson()


    def tearDown(self):
        print("******************测试结束，输出log完结********************")
        self.logger.info('*********************************测试结束，输出log结束*******************************')




