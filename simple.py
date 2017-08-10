#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from bottle import route, run, template
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
run(host='0.0.0.0', port=80)
