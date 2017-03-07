#!/usr/bin/env python
# coding: utf-8

import requests
import json

class modePy:
	def __init__(self):
		self.host = 'api.tinkermode.com';
		self.port = 443;
		self.devicId = '';
		self.token = '';
		
	def setApiHost(self, host):
		self.host = host;
	
	def setDeviceKeys(self, deviceId, token):
		self.deviceId = deviceId;
		self.token = token;

	def triggerEvent(self, eventType, eventData):
		#print('https://' + self.host + '/devices/' + str(self.deviceId) + '/event');
		r = requests.put('https://' + self.host + '/devices/' + str(self.deviceId) + '/event', \
			     json.dumps({"eventType":eventType, "eventData":eventData}), \
			     headers={'Content-Type':'application/json','Authorization':'ModeCloud ' + self.token});
		print(r);	 
 
def foo():
	print('foo');
