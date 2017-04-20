from mode import device, application

def test_func(ws, message):
	print(message + ' in test.py')

mode_device = device.Device()
mode_app = application.Application()

DEVICE_ID = 1
DEVICE_API_KEY = 'v1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
USER_API_KEY = 'v1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#Setup
mode_device.set_device_keys(DEVICE_ID, API_KEY)
mode_device.set_api_host('iot-device.jp-east-1.api.cloud.nifty.com')
mode_app.set_api_host('iot-device.jp-east-1.api.cloud.nifty.com')
mode_app.set_user_key(USER_API_KEY)

mode_device.trigger_event('mode-py_test', {'value':'hoge'})
mode_app.trigger_command(DEVICE_ID, 'action', {'value':'huge'})

mode_device.set_on_message(test_func)
mode_device.listen_commands()
