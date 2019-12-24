from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wen hai yan and unice'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mold_making')
def mold_making():
    return render_template('services/mold_making.html')

@app.route('/advantages')
def advantages():
    return render_template('services/advantages.html')

@app.route('/design_engineering')
def design_engineering():
    return render_template('services/design_engineering.html')

@app.route('/injection_molding')
def injection_molding():
    return render_template('services/injection_molding.html')

@app.route('/Project_management')
def Project_management():
    return render_template('services/Project_management.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us/about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us/contact_us.html')

@app.route('/Insert_Molding')
def Insert_Molding():
    return render_template('products/Insert_Molding.html')

@app.route('/Electrical_Plastics_Molding')
def Electrical_Plastics_Molding():
    return render_template('products/Electrical_Plastics_Molding.html')

@app.route('/Rubber')
def Rubber():
    return render_template('products/Rubber.html')

@app.route('/Auto_Plastics_Part')
def Auto_Plastics_Part():
    return render_template('products/Auto_Plastics_Part.html')

@app.route('/2k_Molding')
def twok_Molding():
    return render_template('products/2k_Molding.html')

@app.route('/Casting')
def Casting():
    return render_template('products/Casting.html')

@app.route('/Stamping tool_1')
def Stamping_tool_1():
    return render_template('products/Stamping_tool_1.html')

@app.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('products/Stamping_tool_2.html')

@app.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('products/Stamping_tool_3.html')

@app.route('/plastic')
def plastic():
    return render_template('products/plastic.html')

@app.route('/quality_assurance')
def quality_assurance():
    return render_template('quality/quality_assurance.html')

@app.route('/process_flowchart')
def process_flowchart():
    return render_template('quality/process_flowchart.html')


if __name__ == "__main__":
    app.run(debug=True)



