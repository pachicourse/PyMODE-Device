from mode import device

def test_func(ws, message):
	print(message + ' in test.py')

mode_device = device.Device()

DEVICE_ID = 1
API_KEY = 'v1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

mode_device.set_device_keys(DEVICE_ID, API_KEY)
mode_device.set_api_host('iot-device.jp-east-1.api.cloud.nifty.com')

#mode_device.trigger_event('mode-py_test', {'value':'hoge'})

mode_device.on_message = test_func
mode_device.listen_commands()
