from mode import device

mode_device = device.Device()
#m.setApiHost("example.com")
#print(m.host)

DEVICE_ID = 1
API_KEY = 'v1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

mode_device.set_device_keys(DEVICE_ID, API_KEY)
mode_device.set_api_host('iot-device.jp-east-1.api.cloud.nifty.com')

mode_device.trigger_event('mode-py_test', {'value':'banana'})
