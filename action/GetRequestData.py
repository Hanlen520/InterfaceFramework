#coding=utf-8
from openpyxl import load_workbook
from config.GloableData import *
from Util.ParseExcel import *
from action.ParamsOper import *

class GetRequestData(object):
    def __init__(self,testdata_path):
		self.pe=ParseExcel()
		self.pe.loadWorkBook(testdata_path)


    def getApi(self,apiName):
		api_sheet = self.pe.getSheetByName(apiName)
		rows = self.pe.getRowsNumber(api_sheet)
		cols = self.pe.getColsNumber(api_sheet)
		result = []
		for row in range(2, rows + 1):
			api_info = {}
			for clo in range(4, cols + 1):
				api_info[self.pe.getCellOfValue(api_sheet, rowNo=1, colsNo=clo)] = self.pe.getCellOfValue(
					api_sheet, rowNo=row, colsNo=clo)
				# result_row.append(self.pe.getCellOfValue(api_sheet, rowNo=row, colsNo=clo))
			result.append(api_info)
		return result

    def getTestCase(self,apiTest):
		testcase_sheet=self.pe.getSheetByName(apiTest)
		rows=self.pe.getRowsNumber(testcase_sheet)
		cols=self.pe.getColsNumber(testcase_sheet)
		result=[]
		for row in range(2,rows+1):
			test_info={}
			for clo in range(1,cols+1):
				test_info[self.pe.getCellOfValue(testcase_sheet,rowNo=1,colsNo=clo)]=self.pe.getCellOfValue(testcase_sheet,rowNo=row,colsNo=clo)
			if test_info['BodyEncrypt']:
				test_info['RequestData']=params_oper(test_info['RequestData'], test_info['BodyEncrypt'])

				# result_row.append(self.pe.getCellOfValue(testcase_sheet,rowNo=row,colsNo=clo))
			result.append(test_info)
		return result

if __name__=='__main__':
	grd=GetRequestData(testdata_path)
	# print grd.getApi(apiName)
	print grd.getTestCase(u"登录接口用例")
