from openapi_server.helpers.resourceDb import ResourceDb
from flask import jsonify


def create_resource(identifier,classname,json_data):
    resource = ResourceDb(id=identifier, object_class=classname, data=json_data)
    resource.save()

def update_resource(identifier, resource):
    resource[name] = resource

def delete_resource(identifier):


    resource = ResourceDb.get_by_id(identifier)

    if not resource:
        raise ValueError

    resource.remove()

    return

def get_resource(identifier):

    resource = ResourceDb.get_by_id(identifier)

    if not resource:
        raise ValueError

    return resource

