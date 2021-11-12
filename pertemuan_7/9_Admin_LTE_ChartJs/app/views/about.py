from . import app

from . import render_template

# Views

@app.route('/about')
def about():
    return render_template("about.html")