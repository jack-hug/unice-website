#!/usr/bin/env python
import os
from app import create_app,db
from app.models import User,Product_category,Product_class
from flask_script import Manager,Shell


app = create_app(os.getenv('UNICE_CONFIG') or 'development')
manager = Manager(app)

def make_shell_context():
    return dict(db=db, User=User,Product_category = Product_category,Product_class = Product_class,app = app)

manager.add_command('shell',Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()