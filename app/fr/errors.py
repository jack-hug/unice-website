from flask import render_template
from . import fr

@fr.app_errorhandler(404)
def page_not_found(e):
    return render_template('fr/404.html'),404

@fr.app_errorhandler(500)
def internal_server_error(e):
    return render_template('fr/500.html'),500