from . import app

from . import login_required
from . import render_template

from sqlalchemy import desc

# import Model
from . import Sensor

# Views
@app.route('/')
@login_required
def home():

    baseQuery = Sensor.query.order_by(desc(Sensor.time))

    sensors = baseQuery.all()
    labels = []
    datasets = []
    datasets_label = set([item.device_type for item in sensors])
    for label in datasets_label : 
        item_datasets = {}
        item_datasets['label'] = label 
        item_datasets['data'] = [{'x' : item.time.timestamp()*1000 ,
                                  'y' : item.value } for item in sensors if item.device_type == label]
        datasets.append(item_datasets)
    # dummy data line chart
    line_chart = {}
    line_chart['name'] = 'SensorHistory'
    line_chart['labels'] = labels
    line_chart['datasets'] = datasets
    line_chart['type'] = 'time_series'

    line_chart['options'] = {
      'maintainAspectRatio' : False,
      'responsive' : True,
      'legend': {
        'display': True
      },
      'scales': {
        'xAxes': [{ 
          'gridLines' : {
            'display' : True,
          },
          'type': "time",
          'time': {
            'unit': 'day'
          },
          'position': "bottom"
        }],
        'yAxes': [{
          'gridLines' : {
            'display' : True,
          }
        }]
      }
    }

    # dummy data pie chart
    pie_chart = {}
    pie_chart['labels'] = ['Temperature','Humidity','Water Level','Power','Speed','Debit']
    pie_chart['datasets'] = [
        {
          'data': [700,500,400,600,300,100],
          'backgroundColor' : ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de'],
        }
      ]

    return render_template('index.html', line_chart=line_chart, pie_chart=pie_chart)
