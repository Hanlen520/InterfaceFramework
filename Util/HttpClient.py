#coding=utf-8
import requests
import traceback
import urllib

class HttpClient(object):
	def __init__(self):
		pass

	def request(self, requestMethod, requesturl, paramMethod=None, requestData=None, headers=None, **kwargs):
		try:
			if requestMethod.lower() == "post":
				return self.__post(paramMethod, requesturl, requestData=requestData, headers=headers, **kwargs)
			elif requestMethod == "get":
				return self.__get(requestUrl=requesturl, params=requestData, **kwargs)
		except Exception, e:
			raise traceback.format_exc()

	def __post(self, paramMethod, requestUrl, requestData = None, headers = None, **kwargs):
		try:
			if paramMethod == "form":
				responseObj = requests.post(url = requestUrl, data = requestData, headers = headers, timeout = 3, **kwargs)
				return responseObj
			elif paramMethod == "json":
				responseObj = requests.post(url = requestUrl, json = requestData, headers = headers, timeout = 3, **kwargs)
				return responseObj
			elif paramMethod == "url":
				url = ""
				if isinstance(requestData, (str, unicode)):
					url = requestUrl + "?%s" %urllib.quote_plus(requestData)
				elif isinstance(requestData, dict):
					url = requestUrl + "?%s=%s" %(requestData.keys()[0], requestData.values()[0])
				responseObj = requests.post(url = url, headers = headers, timeout = 3, **kwargs)
				return responseObj
		except Exception, e:
			raise traceback.format_exc()

	def __get(self, requestUrl, params=None, **kwargs):
		try:
			url = requestUrl
			if params:
				url = requestUrl + "%s" if requestUrl.endswith("/") else requestUrl + "/%s"
				responseObj = requests.get(url=url, timeout=10, **kwargs)
			return responseObj
		except Exception.e:
			raise traceback.format_exc()