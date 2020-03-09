from flask import render_template,redirect,url_for,flash,request
from . import en
from flask_login import login_required,logout_user,login_user
<<<<<<< HEAD
from ..models import User
=======
from ..models import User,Product
>>>>>>> 79cf03d207100cf23ceca964fd12e4ea29dfdded



@en.route('/')
def index():
    return render_template('en/index.html')

@en.route('/mold_making')
def mold_making():
    return render_template('en/services/mold_making.html')

@en.route('/advantages')
def advantages():
    return render_template('en/services/advantages.html')

@en.route('/design_engineering')
def design_engineering():
    return render_template('en/services/design_engineering.html')

@en.route('/injection_molding')
def injection_molding():
    return render_template('en/services/injection_molding.html')

@en.route('/Project_management')
def Project_management():
    return render_template('en/services/Project_management.html')

@en.route('/about_us')
def about_us():
    return render_template('en/about_us/about_us.html')

@en.route('/contact_us')
def contact_us():
    return render_template('en/contact_us/contact_us.html')

@en.route('/Insert_Molding')
def Insert_Molding():
    products =Product.query.all()
    return render_template('en/products/Insert_Molding.html',products = products)

@en.route('/Electrical_Plastics_Molding')
def Electrical_Plastics_Molding():
    return render_template('en/products/Electrical_Plastics_Molding.html')

@en.route('/Rubber')
def Rubber():
    return render_template('en/products/Rubber.html')

@en.route('/Auto_Plastics_Part')
def Auto_Plastics_Part():
    return render_template('en/products/Auto_Plastics_Part.html')

@en.route('/2k_Molding')
def twok_Molding():
    return render_template('en/products/2k_Molding.html')

@en.route('/Casting')
def Casting():
    return render_template('en/products/Casting.html')

@en.route('/Stamping_tool_1')
def Stamping_tool_1():
    return render_template('en/products/Stamping_tool_1.html')

@en.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('en/products/Stamping_tool_2.html')

@en.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('en/products/Stamping_tool_3.html')

@en.route('/Components')
def components():
    return render_template('en/products/Components.html')

@en.route('/quality_assurance')
def quality_assurance():
    return render_template('en/quality/quality_assurance.html')

@en.route('/process_flowchart')
def process_flowchart():
    return render_template('en/quality/process_flowchart.html')