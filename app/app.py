from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/ability')
def ability():
    return render_template('ability.html')



if __name__ == "__main__":
    app.run(debug=True)
