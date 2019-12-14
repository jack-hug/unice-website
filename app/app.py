from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wen hai yan and unice'
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

@app.route('/products_Insert_Molding')
def products_Insert_Molding():
    return render_template('products_Insert_Molding.html')

@app.route('/products_Electrical_Plastics_Molding')
def products_Electrical_Plastics_Molding():
    return render_template('products_Electrical_Plastics_Molding.html')

@app.route('/products_Rubber')
def products_Rubber():
    return render_template('products_Rubber.html')

@app.route('/products_Auto_Plastics_Part')
def products_Auto_Plastics_Part():
    return render_template('products_Auto_Plastics_Part.html')

@app.route('/products_2k_Molding')
def products_2k_Molding():
    return render_template('products_2k_Molding.html')

@app.route('/products_Casting')
def products_Casting():
    return render_template('products_Casting.html')

@app.route('/Stamping tool_1')
def Stamping_tool_1():
    return render_template('Stamping_tool_1.html')

@app.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('Stamping_tool_2.html')

@app.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('Stamping_tool_3.html')

@app.route('/plastic')
def plastic():
    return render_template('plastic.html')

@app.route('/ability_equipment')
def ability_equipment():
    return render_template('ability_equipment.html')

@app.route('/ability_quality')
def ability_quality():
    return render_template('ability_quality.html')

@app.route('/ability_team')
def ability_team():
    return render_template('ability_team.html')



if __name__ == "__main__":
    app.run(debug=True)



