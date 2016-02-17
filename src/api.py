# -*- coding: utf-8 -*-

import os
import csv
import requests
from datetime import datetime
import inspect
from flask import session, render_template, Blueprint, request, jsonify, abort,\
    current_app, redirect, url_for
from config import *
from flask import current_app

from flask import Flask, redirect, url_for
from werkzeug import secure_filename

from utils import parse_request, jsonify_list
from app_logger import create_logger

api = Blueprint('APIs', __name__)

logger = create_logger("api")

@api.route("/")
def index():
    logger.debug("helloooooo")
    return render_template("index.html")


@api.route("/hello")
def hello():
    return "<html><head>Hello</head><body><p> Hello World </p></body></html>"

@api.route("/push", methods=['POST'])
def push():

    logger.debug("in push post api")

    if request.json:
        data = request.get_json()

    logger.debug("data = %s" % str(data))
    logger.debug("clone_url = %s" % str(data['repository']['clone_url']))
    

    return "success"
