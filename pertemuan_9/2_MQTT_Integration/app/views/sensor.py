from . import app
from . import db

from . import login_required, roles_required, roles_accepted

from . import render_template
from . import url_for
from . import request
from . import flash
from . import redirect
from . import session

from . import or_, and_, not_

# import Forms
from . import SensorForm

# import Model
from . import Sensor


# Views

@app.route('/sensors/<int:id>', methods=['GET', 'POST'])
@login_required
def sensor(id):
    sensor = Sensor.query.get(id)
    if request.method == 'POST' :
        form = SensorForm(request.form)
        if form.validate_on_submit() :
            sensor = Sensor() if sensor is None else sensor
            sensor.name = form.name.data
            sensor.device_no = form.device_no.data
            sensor.device_type = form.device_type.data
            sensor.time = form.time.data
            sensor.value = form.value.data
            db.session.add(sensor) if sensor.id is None else ''
            db.session.commit()

            flash("Sensor submitted successfully!", "success")
            return redirect(url_for("sensors"))
        else : 
            return render_template("sensor.html", form=form)
    else:
        form = SensorForm(obj=sensor)
        return render_template("sensor.html", form=form)


@app.route('/sensors', methods=['GET', 'POST'])
@login_required
@roles_required('user')
def sensors():

    search_key = "search_sensors"  # this is can be changes by preference
    if request.method == "POST":
        session[search_key] = request.form.get(search_key)

    page = request.args.get('page')
    page = int(1 if page == None else page)
    baseQuery = Sensor.query.filter(
                                or_(
                                    Sensor.name.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        ),
                                    Sensor.device_no.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        ),
                                    Sensor.device_type.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        )
                                )
                            )

    per_page = 3     # this is can be changes by preference
    destination = 'sensors'  # this is need to set into current route function name.
    record_list = baseQuery.paginate(page, per_page, error_out=False) 
    min_page = record_list.page - 2 if record_list.page - 2 > 0 else 1
    max_page = min_page + 5 if min_page + 5 <= record_list.pages + 1 else record_list.pages + 1
    record_count = baseQuery.count()

    record_header = ['No', 'Name', 'Sensor No', 'Sensor Type', 'Send On', 'Value'] # this is can be same as a field in Table

    return render_template("sensor_list.html", 
                            record_list=record_list, 
                            record_header=record_header,
                            record_count=record_count,
                            min_page=min_page,
                            max_page=max_page,
                            destination=destination,
                            search_key=search_key)