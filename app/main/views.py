from flask import render_template,redirect,url_for,flash,request
from . import main
from flask_login import login_required,logout_user,login_user
from ..models import User,Product



@main.route('/')
def index():
    return render_template('en/index.html')

@main.route('/mold_making')
def mold_making():
    return render_template('en/services/mold_making.html')

@main.route('/advantages')
def advantages():
    return render_template('en/services/advantages.html')

@main.route('/design_engineering')
def design_engineering():
    return render_template('en/services/design_engineering.html')

@main.route('/injection_molding')
def injection_molding():
    return render_template('en/services/injection_molding.html')

@main.route('/Project_management')
def Project_management():
    return render_template('en/services/Project_management.html')

@main.route('/about_us')
def about_us():
    return render_template('en/about_us/about_us.html')

@main.route('/contact_us')
def contact_us():
    return render_template('en/contact_us/contact_us.html')

@main.route('/Insert_Molding')
def Insert_Molding():
    return render_template('en/products/Insert_Molding.html')

@main.route('/Electrical_Plastics_Molding')
def Electrical_Plastics_Molding():
    return render_template('en/products/Electrical_Plastics_Molding.html')

@main.route('/Rubber')
def Rubber():
    return render_template('en/products/Rubber.html')

@main.route('/Auto_Plastics_Part')
def Auto_Plastics_Part():
    return render_template('en/products/Auto_Plastics_Part.html')

@main.route('/2k_Molding')
def twok_Molding():
    return render_template('en/products/2k_Molding.html')

@main.route('/Casting')
def Casting():
    return render_template('en/products/Casting.html')

@main.route('/Stamping_tool_1')
def Stamping_tool_1():
    return render_template('en/products/Stamping_tool_1.html')

@main.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('en/products/Stamping_tool_2.html')

@main.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('en/products/Stamping_tool_3.html')

@main.route('/Precision')
def precision():
    return render_template('en/products/Precision.html')

@main.route('/prototype')
def prototype():
    return render_template('en/products/Prototype.html')

@main.route('/quality_control')
def quality_control():
    return render_template('en/quality/quality_control.html')

@main.route('/quality_process')
def quality_process():
    return render_template('en/quality/quality_process.html')