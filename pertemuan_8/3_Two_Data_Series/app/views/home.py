from . import app

from . import login_required
from . import render_template

from sqlalchemy import desc

#SocketIO
from . import socketio
from flask_socketio import emit

from datetime import datetime
import numpy as np
import time
# Views
@app.route('/')
@login_required
def home():
    curr_time = datetime.now().timestamp()*1000 # get current timestamp
    # dummy data line chart sensor_data
    sensor_data = {}
    sensor_data['event'] = 'SensorHistoryEvent'
    sensor_data['start_event'] = 'StartSensorHistoryEvent'
    sensor_data['name'] = 'SensorHistory'
    sensor_data['labels'] = [curr_time]
    sensor_data['datasets'] = [
      {
        'label' : 'Temperature',
        'borderColor'         : '#f56954',
        'backgroundColor'     : '#f56954',
        'data' : [{
                  'x' : curr_time,
                  'y' : 25.1
                }]
      },
      {
        'label' : 'Humidity',
        'borderColor'         : '#00a65a',
        'backgroundColor'     : '#00a65a',
        'data' : [{
                  'x' : curr_time,
                  'y' : 25.1
                }]
      }
    ]
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

    # dummy data gauge chart temperature
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
        'value' : 33.5,
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

    # dummy data gauge chart humidity
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
        'value' : 55.5,
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
      curr_time = datetime.now().timestamp()*1000 # get current timestamp
      msg = {}
      msg['label'] = curr_time
      msg['datasets'] = [{
        'label' : 'Temperature',
        'data'  : {
                  'y' : np.around(np.random.uniform(low=21, high=40), decimals=2), # get random value
                  'x' : curr_time
                  },
        'borderColor'         : '#f56954',
        'backgroundColor'     : '#f56954',
      },
      {
        'label' : 'Humidity',
        'data'  : {
                  'y' : np.around(np.random.uniform(low=0, high=100), decimals=2), # get random value
                  'x' : curr_time
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

      msg = {}
      msg['datasets'] = [{
        'value' : np.around(np.random.uniform(low=25, high=40), decimals=2)
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

      msg = {}
      msg['datasets'] = [{
        'value' : np.around(np.random.uniform(low=0, high=100), decimals=2)
      }]

      socketio.sleep(1)
      emit('HumidityEvent', msg)
      print("\n\nsend data to client! \n", msg)
    else : 
      print("stop stream")
