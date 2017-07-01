#coding=utf-8
from Util.ParseExcel import ParseExcel
from config.GloableData import *
from Util.Encrypt import EncryptMD5

def params_oper(params,encrypt):
	params=eval(params)
	encrypt=eval(encrypt)
	try:
		for key,value in encrypt.items():
			if value[0]=='md5':
				params[key] = EncryptMD5.encrypt_md5(params[key])
		return params
	except Exception,e:
		raise e

if __name__=='__main__':
	pe=ParseExcel()
	pe.loadWorkBook(testdata_path)
	sheet=pe.getSheetByName(u'登录接口用例')
	params=pe.getCellOfValue(sheet,coordinate='C2')
	print params_oper(params,'{"password":["md5"]}')
