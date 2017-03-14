#!/usr/bin/env python
# coding: utf-8

import requests
import json
import websocket
import threading

class Device:

	def __init__(self):
		self.host              = 'api.tinkermode.com'
		self.port              = 443
		self.devicId           = ''
		self.token             = ''
		self.on_open           = default_on_open
		self.on_message        = default_on_message
		self.on_error          = default_on_error
		self.on_close          = default_on_close
		self.websocket_debug   = False

	def set_api_host(self, host):
		self.host = host
	
	def set_device_keys(self, deviceId, token):
		self.deviceId = deviceId
		self.token = token

	def websocket_trace(self, b):
		self.websocket_debug = b

	def trigger_event(self, eventType, eventData):
		r = requests.put('https://' + self.host + '/devices/' + str(self.deviceId) + '/event', \
				 json.dumps({"eventType":eventType, "eventData":eventData}), \
			         headers={'Content-Type':'application/json','Authorization':'ModeCloud ' + self.token})
		print(r)	

	def listen_commands(self):
		websocket.enableTrace(self.websocket_debug)
		ws = websocket.WebSocketApp('wss://' + self.host + '/devices/' + str(self.deviceId) + '/command',
					    header=["Authorization: ModeCloud %s" % self.token], on_open=self.on_open, \
					    on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)

		# Start websocket
		try:
			ws.run_forever()
		# Ctrl+C to close websocket
		except KeyboardInterrupt:
			ws.close()

# websocket callback
wait = 0.5 #sec

# when open websocke
def default_on_open(ws):
	global wait
	wait = 0.5
	print('connected')

# when get message
def default_on_message(ws, message):
	print(message)

# when error
def default_on_error(ws, error):
	print("error")
	global wait
	if wait < 60:
		wait *= 2 # first error => wait for 1sec.
	__try_reconnect(ws)

# when close websocket
def default_on_close(ws):
	print('disconnected')

def __try_reconnect(ws):
	print('wait for', wait, 'sec to reconnect')
	t = threading.Timer(wait, __reconnect, args=[ws])
	t.start();

def __reconnect(ws):
	print('reconnecting ..')
	
	#Start websocket
	try:
		ws.run_forever()
	# Ctrl+C to close websocket
	except KeyboardInterrupt:
		ws.close()
