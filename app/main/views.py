from flask import Flask,render_template,redirect,url_for,session
from datetime import datetime
from . import main
from .. import db
from ..models import User,Product

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/mold_making')
def mold_making():
    return render_template('services/mold_making.html')

@main.route('/advantages')
def advantages():
    return render_template('services/advantages.html')

@main.route('/design_engineering')
def design_engineering():
    return render_template('services/design_engineering.html')

@main.route('/injection_molding')
def injection_molding():
    return render_template('services/injection_molding.html')

@main.route('/Project_management')
def Project_management():
    return render_template('services/Project_management.html')

@main.route('/about_us')
def about_us():
    return render_template('about_us/about_us.html')

@main.route('/contact_us')
def contact_us():
    return render_template('contact_us/contact_us.html')

@main.route('/Insert_Molding')
def Insert_Molding():
    products =Product.query.all()
    return render_template('products/Insert_Molding.html',products = products)

@main.route('/Electrical_Plastics_Molding')
def Electrical_Plastics_Molding():
    return render_template('products/Electrical_Plastics_Molding.html')

@main.route('/Rubber')
def Rubber():
    return render_template('products/Rubber.html')

@main.route('/Auto_Plastics_Part')
def Auto_Plastics_Part():
    return render_template('products/Auto_Plastics_Part.html')

@main.route('/2k_Molding')
def twok_Molding():
    return render_template('products/2k_Molding.html')

@main.route('/Casting')
def Casting():
    return render_template('products/Casting.html')

@main.route('/Stamping_tool_1')
def Stamping_tool_1():
    return render_template('products/Stamping_tool_1.html')

@main.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('products/Stamping_tool_2.html')

@main.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('products/Stamping_tool_3.html')

@main.route('/plastic')
def plastic():
    return render_template('products/plastic.html')

@main.route('/quality_assurance')
def quality_assurance():
    return render_template('quality/quality_assurance.html')

@main.route('/process_flowchart')
def process_flowchart():
    return render_template('quality/process_flowchart.html')

