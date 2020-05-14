from flask import Flask,render_template,redirect,url_for,session
from datetime import datetime
from . import fr
from .. import db
from ..models import User,Product

@fr.route('/')
def index():
    return render_template('fr/index.html')

@fr.route('/mold_making')
def mold_making():
    return render_template('fr/services/mold_making.html')

@fr.route('/advantages')
def advantages():
    return render_template('fr/services/advantages.html')

@fr.route('/design_engineering')
def design_engineering():
    return render_template('fr/services/design_engineering.html')

@fr.route('/injection_molding')
def injection_molding():
    return render_template('fr/services/injection_molding.html')

@fr.route('/Project_management')
def Project_management():
    return render_template('fr/services/Project_management.html')

@fr.route('/about_us')
def about_us():
    return render_template('fr/about_us/about_us.html')

@fr.route('/contact_us')
def contact_us():
    return render_template('fr/contact_us/contact_us.html')

@fr.route('/Insert_Molding')
def Insert_Molding():
    return render_template('fr/products/Insert_Molding.html')

@fr.route('/Electrical_Plastics_Molding')
def Electrical_Plastics_Molding():
    return render_template('fr/products/Electrical_Plastics_Molding.html')

@fr.route('/Rubber')
def Rubber():
    return render_template('fr/products/Rubber.html')

@fr.route('/Auto_Plastics_Part')
def Auto_Plastics_Part():
    return render_template('fr/products/Auto_Plastics_Part.html')

@fr.route('/2k_Molding')
def twok_Molding():
    return render_template('fr/products/2k_Molding.html')

@fr.route('/Casting')
def Casting():
    return render_template('fr/products/Casting.html')

@fr.route('/Stamping_tool_1')
def Stamping_tool_1():
    return render_template('fr/products/Stamping_tool_1.html')

@fr.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('fr/products/Stamping_tool_2.html')

@fr.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('fr/products/Stamping_tool_3.html')

@fr.route('/Precision')
def Precision():
    return render_template('fr/products/Precision.html')

@fr.route('/Prototype')
def Prototype():
    return render_template('fr/products/Prototype.html')

@fr.route('/quality_assurance')
def quality_assurance():
    return render_template('fr/quality/quality_assurance.html')

@fr.route('/process_flowchart')
def process_flowchart():
    return render_template('fr/quality/process_flowchart.html')

