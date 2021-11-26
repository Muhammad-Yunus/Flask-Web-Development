# Utils
from . import np
from . import datetime
from . import db 

# Model
from . import Sensor

class SensorDataFactory :
  def __init__(self):
    self.data = {}

  def insertData(self, name, device_no, temperature, humidity):
    self.data =  {
      'temperature' : np.around(temperature, decimals=2),
      'humidity'    : np.around(humidity, decimals=2),
      'time'        : datetime.now()
    }
    # save to db for presistent
    Temperature = Sensor(name=name,
          device_no=device_no,
          device_type='Temperature',
          time=self.data['time'],
          value=self.data['temperature']
          )
    Humidity = Sensor(name=name,
          device_no=device_no,
          device_type='Humidity',
          time=self.data['time'],
          value=self.data['humidity']
          )
    db.session.add(Temperature)      
    db.session.add(Humidity)
    db.session.commit()

  def getData(self):
    return self.data
