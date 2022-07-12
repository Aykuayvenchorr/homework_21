from models import *
from config import db
import json


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(User(
            **row
        )
        )
    db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(Order(
            **row
        )
        )
    db.session.commit()


def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(Offer(
            **row
        )
        )
    db.session.commit()


def init_db():
    db.drop_all()
    db.create_all()
    with open('data/user.json', encoding='utf-8') as file:
        data = json.load(file)
        insert_data_user(data)

    with open('data/order.json', encoding='utf-8') as file:
        data = json.load(file)
        insert_data_order(data)

    with open('data/offer.json', encoding='utf-8') as file:
        data = json.load(file)
        insert_data_offer(data)


def get_all(model):
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())

    return result


def get_by_pk(model, pk):
    try:
        return db.session.query(model).get(pk).to_dict()
    except Exception as e:
        print(e)
        return {}


def update_universal(model, user_id, values):
    db.session.query(model).filter(model.id == user_id).update(values)
    db.session.commit()


def delete_universal(model, user_id):
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return {}
