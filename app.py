from flask import Flask, request
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

todos = {'t1': 'todo1', 't2': 'todo2'}

class Todos(Resource):
    def get(self, todo_id):
        return {
            todo_id: todos[todo_id]
        }

    def put(self, todo_id):
        return request.form 



# Create routes
api.add_resource(Todos, '/<string:todo_id>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
