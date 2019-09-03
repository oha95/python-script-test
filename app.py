from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class Team(Resource):
    def get(self):
        return {
            'team': ['oussama', 'yacine', 'ludovic']
        }

api.add_resource(Team, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)