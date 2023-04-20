from openapi_server.helpers.sliceProfileDb import SliceProfileDb
from flask import jsonify


def create_profile(identifier,json_data):
    profile = SliceProfileDb(id=identifier, data=json_data)
    profile.save()

def update_profile(identifier, profile):
    profile[identifier] = profile

def delete_profile(identifier):

    profile = SliceProfileDb.get_by_id(identifier)

    if not profile:
        raise ValueError

    profile.remove()

    return

def get_resource(identifier):

    profile = SliceProfileDb.get_by_id(identifier)

    if not profile:
        raise ValueError

    return profile

