from mode import mode

modeDevice = mode.modePy();
#m.setApiHost("example.com");
#print(m.host);

DEVICE_ID = 1;
API_KEY = 'v1.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

modeDevice.setDeviceKeys(DEVICE_ID, API_KEY);
modeDevice.setApiHost('iot-device.jp-east-1.api.cloud.nifty.com');

modeDevice.triggerEvent('mode-py_test', {'value':'banana'});
