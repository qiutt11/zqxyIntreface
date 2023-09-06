from common.logger import logger
import json

logger=logger

# def analyze_json(jsons):
#     key_value=''
#     if isinstance(jsons,dict):
#         for key in jsons.keys():
#             key_value=jsons.get(key)
#             if isinstance(key_value,dict):
#                 analyze_json(key_value)
#             elif isinstance(key_value,list):
#                 for json_array in key_value:
#                     analyze_json(json_array)
#             else:
#                 print(str(key) + " = " + str(key_value))
#     elif isinstance(jsons,list):
#         for json_array in jsons:
#             analyze_json(json_array)
class analyJson():

    def repkey_value(self,jsons,key,value,default=None):
        if isinstance(jsons,dict):
            for k in jsons.keys():
                if k in jsons.keys():
                    if k==key:
                        jsons[key]=value
                        return jsons
                    elif  isinstance(jsons[k],dict):
                        ret=self.repkey_value(jsons[k],key,value)
                        if ret is not default:
                            return jsons


    def getkey_value(self,jsons,key,default=None):
        key_value=''
        if isinstance(jsons,dict):
            for json_result in jsons.values():
                if key in jsons.keys():
                    key_value=jsons.get(key)
                    return key_value
                else:
                    ret=self.getkey_value(json_result,key)
                    if ret is not default:
                        return ret
        elif isinstance(jsons,list):
            for json_array in jsons:
                 ret=self.getkey_value(json_array,key)
                 if ret is not default:
                     return ret


    def is_dict(self,content):
        try :
            eval(content)
        except SyntaxError:
            return False
        return True

# def getkey_value(jsononly,key,default=None):
#     if isinstance(jsononly,dict):
#         for k,v in jsononly.items():
#             if k==key:
#                 return v
#             elif isinstance(v,dict):
#                 ret=getkey_value(v,key,default=None)
#                 if ret is not default:
#                     return ret

if __name__=="__main__":
    jsons= {"err_code":"200","err_msg":"请求成功","data":{"electric_loaned_warning":{"code":"-1000","msg":"查询失败,未知错误"},"query_id":"202012171434638509153729359204"}}

    token=analyJson().getkey_value(jsons,"code")
    #print(analyJson().rpHeader_token(token))


    print(token)






