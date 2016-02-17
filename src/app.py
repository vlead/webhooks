
# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, make_response
from flask.ext.cors import CORS

from api import api
# import config file
import config
from app_logger import create_logger

def create_app(config):
    # init our app
    app = Flask(__name__)
    logger = create_logger("app")

    # load config values from the config file
    app.config.from_object(config)

    # register blueprints
    app.register_blueprint(api)
    configure_errorhandlers(app, logger)
    configure_cors(app)

    # all set; return app object
    return app


# configure cross origin resource sharing
def configure_cors(app):
    # CORS(app)
    CORS(app, origins=config.ALLOWED_ORIGINS,
         methods=['GET', 'OPTIONS', 'PUT', 'POST'],
         allow_headers='Content-Type')


# custom error handlers to return JSON errors with appropiate status codes

def configure_errorhandlers(app, logger):

    @app.errorhandler(500)
    def server_error(err):
        logger.error("error code = %s" % "500")
        resp = None
        try:
            logger.error("error desc = %s" % err.description)
            resp = make_response(jsonify(error=err.description), 500)
        except Exception:
            try:
                logger.error("error mesg = %s" % err.message)
                resp = make_response(jsonify(error=err.message), 500)
            except Exception:
                resp = make_response(jsonify(error=str(err)), 500)
                logger.error("error = %s" % str(err))
        return resp

    @app.errorhandler(405)
    def method_not_allowed(err):
        logger.error("error code = %s" % "405")
        resp = None
        try:
            logger.error("error desc = %s" % err.description)
            resp = make_response(jsonify(error=err.description), 405)
        except Exception:
            try:
                logger.error("error mesg = %s" % err.message)
                resp = make_response(jsonify(error=err.message), 405)
            except Exception:
                resp = make_response(jsonify(error=str(err)), 405)
                logger.error("error = %s" % str(err))
        return resp

    @app.errorhandler(404)
    def not_found(err):
        logger.error("error code = %s" % "404")
        resp = None
        try:
            logger.error("error desc = %s" % err.description)
            resp = make_response(jsonify(error=err.description), 404)
        except Exception:
            try:
                logger.error("error mesg = %s" % err.message)
                resp = make_response(jsonify(error=err.message), 404)
            except Exception:
                resp = make_response(jsonify(error=str(err)), 404)
                logger.error("error = %s" % str(err))
        return resp

    @app.errorhandler(400)
    def bad_request(err):
        logger.error("error code = %s" % "400")
        resp = None
        try:
            logger.error("error desc = %s" % err.description)
            resp = make_response(jsonify(error=err.description), 400)
        except Exception:
            try:
                logger.error("error mesg = %s" % err.message)
                resp = make_response(jsonify(error=err.message), 400)
            except Exception:
                resp = make_response(jsonify(error=str(err)), 400)
                logger.error("error = %s" % str(err))
        return resp


if __name__ == "__main__":
    app = create_app(config)
    app.run(debug=True, host='0.0.0.0')
