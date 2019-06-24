# Imports
from flask import Flask, render_template

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON

from config import config
from helpers.database import db_session
from schema import schema


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # @app.route("/", methods=['GET'])
    # def index():
    #     return render_template('index.html')

    app.add_url_rule(
        '/politico',
        view_func=GraphQLView.as_view(
            'politico',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
