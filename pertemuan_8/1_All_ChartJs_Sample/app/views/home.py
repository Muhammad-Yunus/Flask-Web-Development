from . import app

from . import login_required
from . import render_template

#SocketIO
from . import socketio
from flask_socketio import emit

from datetime import datetime

# Views
@app.route('/')
@login_required
def home():

    # dummy data line chart sensor_data
    data = [{
        'x' : datetime(2021, 11, 12, 9, 0, 0, 0).timestamp()*1000,
        'y' : 25.1
      },
      {
        'x' : datetime(2021, 11, 12, 9, 0, 5, 0).timestamp()*1000,
        'y' : 26.7
      },
      {
        'x' : datetime(2021, 11, 12, 9, 0, 10, 0).timestamp()*1000,
        'y' : 23.0
      },
      {
        'x' : datetime(2021, 11, 12, 9, 0, 15, 0).timestamp()*1000,
        'y' : 29.5
      },
      {
        'x' : datetime(2021, 11, 12, 9, 0, 30, 0).timestamp()*1000,
        'y' : 27.4
      },
      {
        'x' : datetime(2021, 11, 12, 9, 0, 35, 0).timestamp()*1000,
        'y' : 30.1
      }]
    sensor_data = {}
    sensor_data['event'] = 'SensorHistoryEvent'
    sensor_data['start_event'] = 'StartSensorHistoryEvent'
    sensor_data['name'] = 'SensorHistory'
    sensor_data['labels'] = [item['x'] for item in data]
    sensor_data['datasets'] = [
      {
        'label' : 'Temperature',
        'borderColor'         : '#f56954',
        'backgroundColor'     : '#f56954',
        'data' : data
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

    # dummy data pie chart sensor_data_by_type
    sensor_data_by_type = {}
    sensor_data_by_type['event'] = 'SensorHistoryByTypeEvent'
    sensor_data_by_type['start_event'] = 'StartSensorHistoryByTypeEvent'
    sensor_data_by_type['name'] = 'SensorHistoryByType'
    sensor_data_by_type['labels'] = ['Temperature','Humidity','Water Level','Power','Speed','Debit']
    sensor_data_by_type['datasets'] = [
      {
        'data': [700,500,400,600,300,100],
        'backgroundColor' : ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de'],
      }
    ]

    # dummy data line chart monthly_sales_data
    monthly_sales_data = {}
    monthly_sales_data['event'] = 'MonthlySalesEvent'
    monthly_sales_data['start_event'] = 'StartMonthlySalesEvent'
    monthly_sales_data['name'] = 'MonthlySales'
    monthly_sales_data['labels'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    monthly_sales_data['datasets'] = [
      {
        'label'               : 'Shoe',
        'borderColor'         : '#f56954',
        'backgroundColor'     : '#f56954',
        'data'                : [28, 48, 40, 19, 86, 27, 90]
      },
      {
        'label'               : 'Bag',
        'borderColor'         : '#00a65a',
        'backgroundColor'     : '#00a65a',
        'data'                : [65, 59, 80, 81, 56, 55, 40]
      },
    ]
    monthly_sales_data['options'] = {
      'legend' : {
        'display': True,
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

    return render_template('index.html', 
                          sensor_data=sensor_data, 
                          sensor_data_by_type=sensor_data_by_type,
                          monthly_sales_data=monthly_sales_data,
                          temperature_data=temperature_data)