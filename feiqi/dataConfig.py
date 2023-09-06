#获取excel的每个列

class global_var:

    Id='0'
    request_name='1'
    url='2'
    run='3'
    request_method='4'
    header='5'
    data='6'
    expect='7'
    result='8'

def getId():
    return global_var.Id
def getUrl():
    return global_var.url
def getRun():
    return global_var.run
def getRequestMethod():
    return global_var.request_method
def getHeader():
    return global_var.header
# def get_case_depend():
#     return global_var.case_depend
# def get_data_depend():
#     return global_var.data_depend
# def get_file_depend():
#     return global_var.file_depend
def getData():
    return global_var.data
def getExpect():
    return global_var.expect
def getResult():
    return global_var.result




