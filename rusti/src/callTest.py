from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        print("dring get")
        return {'hello': 'world'}
    def post(self):
        print("dring post")
        print(request.form['data'])
        return {'hello': request.form['data']}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)