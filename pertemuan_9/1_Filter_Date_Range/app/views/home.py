from . import app, db

from . import login_required
from . import render_template
from . import request
from . import flash
from . import redirect
from . import url_for
from . import desc
from . import and_
from . import session

# Model
from . import Sensor
from . import FilterDate

# Form
from . import FilterDateForm

from . import datetime
from . import np

# load sensor factory object
from . import factory

# load utils functions
from .utils import parse_time

# load SocketIO 
from . import socketio 
from . import emit

# Views
@app.route('/')
@login_required
def home():
    # query to FilterDate model to get last saved filter format
    baseQuery = {}
    filter_date = FilterDate.query.get(1) or FilterDate()
    
    # create filter form using filter_date value
    form_filter_date = FilterDateForm(obj=filter_date) 

    # if using Quick Rage Filter
    if filter_date.quick_range == True : 
      # calculate datetime for given quick range
      # e.g : 3h -> get exact time for 3 hours ago from now.
      quick_range_datetime = datetime.now() - parse_time(filter_date.data)
      
      baseQuery = Sensor.query.filter(
                                and_(
                                  Sensor.time >= quick_range_datetime, 
                                  )
                                ).order_by(desc(Sensor.time))    
    # If using Range Filter
    else :
      baseQuery = Sensor.query.filter(
                                and_(
                                  Sensor.time >= filter_date.from_date, 
                                  Sensor.time <= filter_date.to_date
                                  )
                                ).order_by(desc(Sensor.time))

    # Get History from database for line chart sensor_data
    sensors = baseQuery.all()
    datasets_label = set([item.device_type for item in sensors])
    
    # color map between label vs color
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
        'label' : 'Humidity',
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
        'text': 'Humidity (%)'
      }
    }


    return render_template('index.html', 
                          sensor_data=sensor_data, 
                          temperature_data=temperature_data,
                          humidity_data=humidity_data,
                          form_filter_date=form_filter_date)

# view for filter date range dashboard
@app.route('/filter_date/<filter>', methods=['GET', 'POST'])
@login_required
def filter_date(filter):
  filter_date = FilterDate.query.get(1) or FilterDate()
  if request.method == 'POST' :
    form = FilterDateForm(request.form)
    if form.validate_on_submit() : 
      filter_date.quick_range=False
      filter_date.from_date=form.from_date.data
      filter_date.to_date=form.to_date.data
  else : 
    filter_date.quick_range=True 
    filter_date.data=filter
  db.session.add(filter_date) if filter_date.id is None else ''
  db.session.commit()

  flash("Filter applied!", "success")
  return redirect(url_for("home"))


@socketio.on("StartSensorHistoryEvent")
def event_handler(msg):
  print(msg)

@socketio.on("StartTemperatureEvent")
def event_handler(msg):
  print(msg)

@socketio.on("StartHumidityEvent")
def event_handler(msg):
  print(msg)