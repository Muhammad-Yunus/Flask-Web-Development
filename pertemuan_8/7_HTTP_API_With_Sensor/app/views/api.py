from . import app
from . import request
from . import jsonify

# load sensor factory object
from . import factory

# Create Exposed API to receive sensor data
@app.route('/api/v1/sensor/post', methods=['POST'])
def sensor_post():
    try : 
        json_data = request.json
        name = json_data['name']
        device_no = json_data['device_no']
        temperature = float(json_data['temperature'])
        humidity = float(json_data['humidity'])
        # insert data
        factory.insertData(name, device_no, temperature, humidity)
        
        message = {
            'status': 200,
            'message': 'Success'
        }
        resp = jsonify(message)
        return resp

    except Exception as e:
        message = {
            'status': 500,
            'message': "[ERROR] " + str(e)
        }
        resp = jsonify(message)
        return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp