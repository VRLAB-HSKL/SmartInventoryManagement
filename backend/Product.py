from flask_restful import Resource
from flask import request, jsonify, abort, Response
import Create_db
from flask_jwt_extended import jwt_required

# *Funktioniert wurde getestet
class Add_Product(Resource):
    @jwt_required()
    def get(self):
        try:
            name = request.args.get('name')
            email = request.args.get('email')
            count = request.args.get('count')
            if (len(name) == 0 or len(email) == 0 or len(count) == 0):
                raise Exception()

        except Exception:
            abort(Response("Error in Klasse Add_Product, Parameter leer"))

        if Create_db.Insert_Product(name, email, count):
            print("Successfully added")
            return jsonify({"Poduct added": True})


# *Funktioniert wurde getestet
class Delete_Product(Resource):
    @jwt_required()
    def get(self):
        try:
            name = request.args.get('name')
            email = request.args.get('email')
            if (len(name) == 0 or len(email) == 0):
                raise Exception()

        except Exception:
            abort(Response("Error in Klasse Delete_Product, Parameter leer"))

        if Create_db.Delete_Product(name, email):
            print("Successfully deleted")
            return jsonify({"Poduct deleted": True})

# *Funktioniert wurde getestet


class Update_Product(Resource):
    @jwt_required()
    def get(self):
        try:
            name = request.args.get('name')
            email = request.args.get('email')
            count = request.args.get('count')
            if (len(name) == 0 or len(email) == 0 or len(count) == 0):
                raise Exception()

        except Exception:
            abort(Response("Error in Klasse Update_Product, Parameter leer"))

        if Create_db.Update_Product(name, email, count):
            print("Successfully updated")
            return jsonify({"Poduct updated": True})


# *Funktioniert wurde getestet
class Show_Product(Resource):
    @jwt_required()
    def get(self):
        try:
            print("Gettit")
            email = request.args.get('email')
            #name = request.args.get('name')
            if (len(email) == 0):
                raise Exception()

        except Exception:
            abort(Response("Error in Klasse Show_Product, Parameter leer"))

        data = Create_db.Show_Products(email)
        print(data)
        return data
