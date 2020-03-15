from flask import Blueprint

cn = Blueprint('cn',__name__)

from . import views,errors