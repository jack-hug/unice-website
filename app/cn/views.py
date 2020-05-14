from flask import Flask,render_template,redirect,url_for,session
from datetime import datetime
from . import cn
from .. import db
from ..models import User,Product

@cn.route('/')
def index():
    return render_template('cn/index.html')

@cn.route('/mold_making')
def mold_making():
    return render_template('cn/services/mold_making.html')

@cn.route('/advantages')
def advantages():
    return render_template('cn/services/advantages.html')

@cn.route('/design_engineering')
def design_engineering():
    return render_template('cn/services/design_engineering.html')

@cn.route('/injection_molding')
def injection_molding():
    return render_template('cn/services/injection_molding.html')

@cn.route('/Project_management')
def Project_management():
    return render_template('cn/services/Project_management.html')

@cn.route('/about_us')
def about_us():
    return render_template('cn/about_us/about_us.html')

@cn.route('/contact_us')
def contact_us():
    return render_template('cn/contact_us/contact_us.html')

@cn.route('/Insert_Molding')
def Insert_Molding():
    return render_template('cn/products/Insert_Molding.html')

@cn.route('/Electrical_Plastics_Molding')
def Electrical_Plastics_Molding():
    return render_template('cn/products/Electrical_Plastics_Molding.html')

@cn.route('/Rubber')
def Rubber():
    return render_template('cn/products/Rubber.html')

@cn.route('/Auto_Plastics_Part')
def Auto_Plastics_Part():
    return render_template('cn/products/Auto_Plastics_Part.html')

@cn.route('/2k_Molding')
def twok_Molding():
    return render_template('cn/products/2k_Molding.html')

@cn.route('/Casting')
def Casting():
    return render_template('cn/products/Casting.html')

@cn.route('/Stamping_tool_1')
def Stamping_tool_1():
    return render_template('cn/products/Stamping_tool_1.html')

@cn.route('/Stamping_tool_2')
def Stamping_tool_2():
    return render_template('cn/products/Stamping_tool_2.html')

@cn.route('/Stamping_tool_3')
def Stamping_tool_3():
    return render_template('cn/products/Stamping_tool_3.html')

@cn.route('/Precision')
def Precision():
    return render_template('cn/products/Precision.html')

@cn.route('/prototype')
def Prototype():
    return render_template('cn/products/Prototype.html')

@cn.route('/quality_assurance')
def quality_assurance():
    return render_template('cn/quality/quality_assurance.html')

@cn.route('/process_flowchart')
def process_flowchart():
    return render_template('cn/quality/process_flowchart.html')

