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
        'data' : [27, 32, 40],
        'backgroundColor' : ['green', 'orange', 'red'],
        'value' : 33.5,
        'minValue' : 25
      }
    ]
    temperature_data['type'] = 'gauge' # if we want to load data into gauge, we neet to add this rpoperty
    
    return render_template('index.html', 
                          sensor_data=sensor_data, 
                          temperature_data=temperature_data)

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
      }]

      socketio.sleep(1)
      emit('SensorHistoryEvent', msg)
      print("\n\nsend data to client! \n", msg)
    else : 
      print("stop stream")

# socketio handler for gauge chart
@socketio.on('StartTemperatureEvent')
def handle_message(data):
    print('received message : ', data)
    if data == 'start' or data == 'update' :

      msg = {}
      msg['datasets'] = [{
          'value' : np.around(np.random.uniform(low=25, high=40), decimals=2),
      }]

      socketio.sleep(1)
      emit('TemperatureEvent', msg)
      print("\n\nsend data to client! \n", msg)
    else : 
      print("stop stream")
