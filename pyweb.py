#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, error
import bottle
import hashlib

token = 'shu1jia1'

@route('/')
def check_signature():
    signature = request.query.signature
    timestamp = request.query.timestamp
    nonce = request.query.nonce
    print(signature+',timestamp:'+timestamp)
    L = [timestamp, nonce, token]
    L.sort()
    s = L[0] + L[1] + L[2]
    return hashlib.sha1(s).hexdigest() == signature

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/hello')
def hello():
    return 'This website is under construction...'


@error(404)
def error404(error):
    return 'Nothing here, sorry'


# templates目录
@bottle.route('/web/<filename:path>')
def webfile(filename):
    return bottle.static_file(filename, root="./webdoc/")  # 相对路径


@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)


# @route('/my_ip')
# def show_ip():
run(host='0.0.0.0', port=8009)
