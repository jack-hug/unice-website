from flask import render_template
from . import cn

@cn.app_errorhandler(404)
def page_not_found(e):
    return render_template('cn/404.html'),404

@cn.app_errorhandler(500)
def internal_server_error(e):
    return render_template('cn/500.html'),500