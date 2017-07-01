#coding=utf-8
from Util.HttpClient import *
from config.GloableData import *
from action.GetRequestData import *
from action.ParamsOper import *

def main(filepath):
	data=GetRequestData(filepath)
	api_info=data.getApi(apiName)
	hc=HttpClient()
	for api in api_info:
		requestMethod=api['RequestMethod']
		requesturl=api['RequestURL']
		paramMethod=str(api['ParamsInfo']).split('_')[1]
		test_case=data.getTestCase(api['APITestCase'])
		# print requestMethod,requesturl,paramMethod
		for case in test_case:
			requestData=case['RequestData']
			# print requestData
			hc.request(requestMethod, requesturl, paramMethod=paramMethod, requestData=requestData, headers=None)
			# print 'done'

if __name__ == '__main__':
    main(testdata_path)