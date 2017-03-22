#!/usr/bin/env python
# coding: utf-8

import requests
import json
import websocket
import threading

class Device:
    
    def __init__(self):
        self.host = 'api.tinkermode.com'
        self.port = 443
        self.devicId = ''
        self.token = ''
        self.websocket_debug = False
        self.wait = 0.5
        self.ex_on_open = _default_extend_function
        self.ex_on_message = _default_extend_function
        self.ex_on_error = _default_extend_function
        self.ex_on_close = _default_extend_function

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
       	                            header=["Authorization: ModeCloud %s" % self.token], on_open=self._on_open, \
                                    on_message=self._on_message, on_error=self._on_error, on_close=self._on_close)

        # Start websocket
        try:
        	ws.run_forever()
        # Ctrl+C to close websocket
        except KeyboardInterrupt:
        	ws.close()
    

    # websocket callback methods
    # when open websocke
    def _on_open(self, ws):
        self.wait = 0.5
        print('connected')
        self.ex_on_open(ws)

    # when get message
    def _on_message(self, ws, message):
        print(message)
        self.ex_on_message(ws, message)

    # when error
    def _on_error(self, ws, error):
        print("error")
        self.ex_on_error(ws, error)
        if self.wait < 60:
        	self.wait *= 2 # first error => wait for 1sec.
        print(self.wait)
        self._try_reconnect(ws)
    
    # when close websocket
    def _on_close(self, ws):
        print('disconnected')
        self.ex_on_close(ws)

    def _try_reconnect(self, ws):
        print('wait for', self.wait, 'sec to reconnect')
        t = threading.Timer(self.wait, self._reconnect, args=[ws])
        t.start();

    def _reconnect(self, ws):
        print('reconnecting ..')
        
        #start websocket
        try:
        	ws.run_forever()
        # Ctrl+C to close websocket
        except KeyboardInterrupt:
            ws.close()

    # extend websocket callback methods  
    def extend_on_open(self, f):
        self.ex_on_open = f
    
    def extend_on_message(self, f):
        self.ex_on_message = f
    
    def extend_on_error(self, f):
        self.ex_on_error = f
    
    def extend_on_close(self, f):
        self.ex_on_close = f

def _default_extend_function(*arg):
    return

