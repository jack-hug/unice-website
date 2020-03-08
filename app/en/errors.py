from flask import render_template
from . import en

@en.app_errorhandler(404)
def page_not_found(e):
    return render_template('en/404.html'),404

@en.app_errorhandler(500)
def internal_server_error(e):
    return render_template('en/html'),500