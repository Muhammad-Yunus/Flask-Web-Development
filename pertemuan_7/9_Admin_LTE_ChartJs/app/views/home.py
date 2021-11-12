from . import app

from . import login_required
from . import render_template

# Views
@app.route('/')
@login_required
def home():
    # dummy data line chart
    line_chart = {}
    line_chart['name'] = 'monthlySales'
    line_chart['labels'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    line_chart['datasets'] = [
        {
          'label'               : 'Temperature',
          'backgroundColor'     : 'rgba(60,141,188,0.9)',
          'borderColor'         : 'rgba(60,141,188,0.8)',
          'pointRadius'         : False,
          'pointColor'          : '#3b8bba',
          'pointStrokeColor'    : 'rgba(60,141,188,1)',
          'pointHighlightFill'  : '#fff',
          'pointHighlightStroke': 'rgba(60,141,188,1)',
          'data'                : [28, 48, 40, 19, 86, 27, 90]
        },
        {
          'label'               : 'Humidity',
          'backgroundColor'     : 'rgba(210, 214, 222, 1)',
          'borderColor'         : 'rgba(210, 214, 222, 1)',
          'pointRadius'         : False,
          'pointColor'          : 'rgba(210, 214, 222, 1)',
          'pointStrokeColor'    : '#c1c7d1',
          'pointHighlightFill'  : '#fff',
          'pointHighlightStroke': 'rgba(220,220,220,1)',
          'data'                : [65, 59, 80, 81, 56, 55, 40]
        },
      ]

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
          }
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
