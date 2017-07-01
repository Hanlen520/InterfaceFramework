#coding=utf-8
import os

#excel文件变量
apiName='API'
#工程目录
project_path=os.path.dirname(os.path.dirname(__file__))
#测试数据文件
testdata_path=os.path.join(project_path,'TestCase','InterfaceTestCase.xlsx')


if __name__=='__main__':
	print testdata_path