from . import app, mqtt
from . import json

# load sensor factory object
from . import factory


# subscribe into Topic
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
  mqtt.subscribe('dashboard/sensor')

# handle message at topic
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
  topic = message.topic
  if topic == 'dashboard/sensor' :
    payload = message.payload.decode()
    payload_dict = json.loads(payload)
    
    name = payload_dict['name']
    device_no = payload_dict['device_no']
    temperature = float(payload_dict['temperature'])
    humidity = float(payload_dict['humidity'])
    
    print("\nReceive : %s, %s, %.2fC, %.2f%%\n" % (name, device_no, temperature, humidity))
    
    # insert data
    factory.insertData(name, device_no, temperature, humidity)