from . import app, db

from . import login_required
from . import render_template

from . import desc

# Model
from . import Sensor

#SocketIO
from . import socketio
from flask_socketio import emit

from . import datetime
from . import np

# load sensor factory object
from . import factory

# Views
@app.route('/')
@login_required
def home():
    curr_time = datetime.now().timestamp()*1000 # get current timestamp
    # Get History from database for line chart sensor_data

    baseQuery = Sensor.query.order_by(desc(Sensor.time))
    sensors = baseQuery.all()
    datasets_label = set([item.device_type for item in sensors])
    color_map = {
      'Temperature' : '#f56954',
      'Humidity' : '#00a65a'
    }
    sensor_data = {}
    sensor_data['event'] = 'SensorHistoryEvent'
    sensor_data['start_event'] = 'StartSensorHistoryEvent'
    sensor_data['name'] = 'SensorHistory'
    sensor_data['labels'] = []
    sensor_data['datasets'] = [{
        'label' : label,
        'borderColor'         : color_map[label],
        'backgroundColor'     : color_map[label],
        'data' : [{
                  'x' : item.time.timestamp()*1000,
                  'y' : item.value
                } for item in sensors if item.device_type == label]
      } for label in datasets_label ]

    sensor_data['options'] = {
      'legend' : {
        'display': True,
      },
      'scales': {
        'xAxes': [{
          'display' : True,
          'type': 'time',
          'time': {
              'unit': 'second'
          }
        }]
      },
      'elements': {
          'point': {
            'radius': 3
          }
      }
    }

    # get last temperature data for gauge chart
    last_sensor_temperature = baseQuery.filter_by(device_type='Temperature').first() or {}
    
    temperature_data = {}
    temperature_data['event'] = 'TemperatureEvent'
    temperature_data['start_event'] = 'StartTemperatureEvent'
    temperature_data['name'] = 'Temperature'
    temperature_data['labels'] = ['cold', 'warm', 'hot']
    temperature_data['datasets'] = [
      {
        'label' : 'Temperature',
        'data' : [27, 32, 40],
        'backgroundColor' : ['green', 'orange', 'red'],
        'value' : getattr(last_sensor_temperature, 'value', 25),
        'minValue' : 25
      }
    ]
    temperature_data['type'] = 'gauge' # if we want to load data into gauge, we neet to add this rpoperty
    temperature_data['options'] = {
      'title': {
        'display': True,
        'text': 'Temperature (°C)'
      }
    }

    # get last humidity data for gauge chart
    last_sensor_humidity = baseQuery.filter_by(device_type='Humidity').first() or {}

    humidity_data = {}
    humidity_data['event'] = 'HumidityEvent'
    humidity_data['start_event'] = 'StartHumidityEvent'
    humidity_data['name'] = 'Humidity'
    humidity_data['labels'] = ['dry', 'comfort', 'moist']
    humidity_data['datasets'] = [
      {
        'label' : 'Temperature',
        'data' : [40, 70, 100],
        'backgroundColor' : ['DarkSeaGreen', 'ForestGreen', 'DarkOliveGreen'],
        'value' : getattr(last_sensor_humidity, 'value', 0),
        'minValue' : 0
      }
    ]
    humidity_data['type'] = 'gauge' # if we want to load data into gauge, we neet to add this rpoperty
    humidity_data['options'] = {
      'title': {
        'display': True,
        'text': 'Humidity (%H)'
      }
    }

    return render_template('index.html', 
                          sensor_data=sensor_data, 
                          temperature_data=temperature_data,
                          humidity_data=humidity_data)

# socketio handler for line chart
@socketio.on('StartSensorHistoryEvent')
def handle_message(data):
    print('received message : ', data)
    if data == 'start' or data == 'update' :
      # insert & get dummy data to and from database
      data = factory.getData()

      msg = {}
      msg['label'] = data['time'].timestamp()*1000
      msg['datasets'] = [{
        'label' : 'Temperature',
        'data'  : {
                  'y' : data['temperature'],
                  'x' : data['time'].timestamp()*1000
                  },
        'borderColor'         : '#f56954',
        'backgroundColor'     : '#f56954',
      },
      {
        'label' : 'Humidity',
        'data'  : {
                  'y' : data['humidity'],
                  'x' : data['time'].timestamp()*1000
                  },
        'borderColor'         : '#00a65a',
        'backgroundColor'     : '#00a65a',
      }]

      socketio.sleep(1)
      emit('SensorHistoryEvent', msg)
      print("\n\nsend data to client! \n", msg)
    else : 
      print("stop stream")

# socketio handler for temperature gauge chart
@socketio.on('StartTemperatureEvent')
def handle_message(data):
    print('received message : ', data)
    if data == 'start' or data == 'update' :
      # get dummy data
      data = factory.getData()
      msg = {}
      msg['datasets'] = [{
        'value' : data['temperature']
      }]

      socketio.sleep(1)
      emit('TemperatureEvent', msg)
      print("\n\nsend data to client! \n", msg)
    else : 
      print("stop stream")

# socketio handler for humidity gauge chart
@socketio.on('StartHumidityEvent')
def handle_message(data):
    print('received message : ', data)
    if data == 'start' or data == 'update' :
      # get dummy data
      data = factory.getData()
      msg = {}
      msg['datasets'] = [{
        'value' : data['humidity']
      }]

      socketio.sleep(1)
      emit('HumidityEvent', msg)
      print("\n\nsend data to client! \n", msg)
    else : 
      print("stop stream")
