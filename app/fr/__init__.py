from flask import Blueprint

fr = Blueprint('fr',__name__)

from . import views,errors