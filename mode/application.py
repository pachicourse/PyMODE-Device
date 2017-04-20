#!/usr/bin/env python
# coding: utf-8

import requests
import json

class Application:

    def __init__(self):
        self.host = 'api.tinkermode.com'
        self.port = 443
        self.token = ''

    def set_api_host(self, host):
        self.host = host
    
    def set_user_key(self, token):
        self.token = token
    
    def trigger_command(self, deviceId, action, parameters):
        r = requests.put('https://' + self.host + '/devices/' + str(deviceId) + '/command', \
                         json.dumps({"action":action, "parameters":parameters}), \
                         headers={'Content-Type':'application/json','Authorization':'ModeCloud ' + self.token})
        print(r) 
