from flask import abort, make_response, Response
from ..db import db
import os
import requests

# validate model
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    
    except:
        response = {'message': f'{cls.__name__} {model_id} invalid'}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {'message': f'{cls.__name__} {model_id} not found'}
        abort(make_response(response, 404))
    
    return model

# create model
def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    
    except KeyError:
        response = {'details': f'Invalid data'}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201

# get models with filters

# modify model (patch) 

# replace model (put)

# delete model
def delete_model(cls, model_id):
    model_to_delete = validate_model(cls, model_id)
    
    db.session.delete(model_to_delete)
    db.session.commit()

    return Response(status=204, mimetype='application/json')