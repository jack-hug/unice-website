from flask import Blueprint

en = Blueprint('en',__name__)

from . import views,errors