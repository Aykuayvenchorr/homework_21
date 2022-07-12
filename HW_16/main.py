import json

from flask import request, jsonify

from config import app
from models import User, Order, Offer
from service import init_db, get_all, get_by_pk, insert_data_user, update_universal, insert_data_order, delete_universal


@app.route('/users', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        insert_data_user(request.json)
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_pk(user_id):
    if request.method == 'GET':
        data = get_by_pk(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        data = update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["ok"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == 'DELETE':
        data = delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(["ok"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

@app.route('/orders', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        insert_data_order(request.json)
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_pk(order_id):
    if request.method == 'GET':
        data = get_by_pk(Order, order_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        data = update_universal(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["ok"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        data = delete_universal(Order, order_id)
        return app.response_class(
            response=json.dumps(["ok"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/offers', methods=['GET', 'POST'])
def get_all_offers():
    return app.response_class(
        response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_pk(offer_id):
    if request.method == 'GET':
        data = get_by_pk(Offer, offer_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        data = update_universal(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["ok"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == 'DELETE':
        data = delete_universal(Offer, offer_id)
        return app.response_class(
            response=json.dumps(["ok"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
