import connexion
import six
import uuid
from typing import Dict
from typing import Tuple
from typing import Union
from flask import make_response,jsonify
import json

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.error_response_error import ErrorResponseError  # noqa: E501
from openapi_server.models.patch_item import PatchItem  # noqa: E501
from openapi_server.models.resource import Resource  # noqa: E501
from openapi_server.models.service_profile import ServiceProfile  # noqa: E501
from openapi_server.models.scope import Scope  # noqa: E501
from openapi_server.helpers import resourceHelper
from openapi_server import util


def delete_moi(class_name, id_):  # noqa: E501
    """Deletes one resource

    With HTTP DELETE one resource is deleted. The resources to be deleted is identified with the target URI. # noqa: E501

    :param class_name: 
    :type class_name: str
    :param id: 
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        resourceHelper.delete_resource(id_)
    except ValueError:
        response=ErrorResponse(ErrorResponseError('NOT_FOUND: Cannot find resource.'))
        return make_response(jsonify(response),404)

    return 

def get_moi_attributes(class_name, id_, attributes, scope=None, filter=None, fields=None):  # noqa: E501
    """Reads one or multiple resources

    With HTTP GET resources are read. The resources to be retrieved are identified with the target URI. The attributes and fields parameter of the query components allow to select the resource properties to be returned. # noqa: E501

    :param class_name: 
    :type class_name: str
    :param id: 
    :type id: str
    :param attributes: This parameter specifies the attributes of the scoped resources that are returned.
    :type attributes: List[str]
    :param scope: This parameter extends the set of targeted resources beyond the base resource identified with the path component of the URI. No scoping mechanism is specified in the present document.
    :type scope: dict | bytes
    :param filter: This parameter reduces the targeted set of resources by applying a filter to the scoped set of resource representations. Only resource representations for which the filter construct evaluates to \&quot;true\&quot; are targeted. No filter language is specified in the present document.
    :type filter: str
    :param fields: This parameter specifies the attribute field of the scoped resources that are returned.
    :type fields: List[str]

    :rtype: Union[Resource, Tuple[Resource, int], Tuple[Resource, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        scope =  Scope.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        resource=resourceHelper.get_resource(id_)
    except ValueError:
        response=ErrorResponse(ErrorResponseError('NOT_FOUND: Cannot find resource.'))
        return make_response(jsonify(response),404)

    return make_response(resource.data,200)

def modify_moi_attributes(class_name, id_):  # noqa: E501
    """Patches one or multiple resources

    With HTTP PATCH resources are created, updated or deleted. The resources to be modified are identified with the target URI (base resource) and the patch document included in the request message body. # noqa: E501

    :param class_name: 
    :type class_name: str
    :param id: 
    :type id: str
    :param resource: The request body describes changes to be made to the target resources. The following patch media types are available   - \&quot;application/merge-patch+json\&quot; (RFC 7396)   - \&quot;application/3gpp-merge-patch+json\&quot; (TS 32.158)   - \&quot;application/json-patch+json\&quot; (RFC 6902)   - \&quot;application/3gpp-json-patch+json\&quot; (TS 32.158)
    :type resource: dict | bytes

    :rtype: Union[Resource, Tuple[Resource, int], Tuple[Resource, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        resource = Resource.from_dict(connexion.request.get_json())  # noqa: E501
    return


def create_moi(class_name, id_):  # noqa: E501
    """Replaces a complete single resource or creates it if it does not exist

    With HTTP PUT a complete resource is replaced or created if it does not exist. The target resource is identified by the target URI. # noqa: E501

    :param class_name: 
    :type class_name: str
    :param id_: 
    :type id_: str
    :param resource: 
    :type resource: dict | bytes

    :rtype: Union[Resource, Tuple[Resource, int], Tuple[Resource, int, Dict[str, str]]
    """
    

    if connexion.request.is_json:
        resource = Resource.from_dict(connexion.request.get_json())  # noqa: E501

    json_object = connexion.request.get_json()

    resourceHelper.create_resource(id_ ,class_name, json.dumps(json_object))
    
    return resource

def allocate_nsi(service_profile):  # noqa: E501
    """to allocate a network slice instance provided by the service provider, the network slice instance may be new or existing

    With HTTP POST a complete Service Profile iscreated if it does not exist. # noqa: E501

    :param service_profile:
    :type service_profile: dict | bytes

    :rtype: Union[ServiceProfile, Tuple[ServiceProfile, int], Tuple[ServiceProfile, int, Dict[str, str]]
    """

    if connexion.request.is_json:
        service_profile = ServiceProfile.from_dict(connexion.request.get_json())  # noqa: E501

    json_object = connexion.request.get_json()

    identifier=uuid.uuid1()

    serviceProfileHeper.create_service_profile(identifier,json.dumps(json_object))

    serviceProfile.service_profile_id(identifier)

    return serviceProfile


def deallocate_nsi(id):  # noqa: E501
    """Deallocates a Network Slice

    With HTTP DELETE one resource is deleted. The resources to be deleted is identified with the target URI. # noqa: E501

    :param id:
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    try:
        ServiceProfileHelper.delete_resource(id_)
    except ValueError:
        response=ErrorResponse(ErrorResponseError('NOT_FOUND: Cannot find service profile.'))
        return make_response(jsonify(response),404)

    return


def get_nsi(id, scope=None, filter=None, attributes=None, fields=None):  # noqa: E501
    """Reads Service Profile information

    With HTTP GET resources are read. The resources to be retrieved are identified with the target URI. The attributes and fields parameter of the query components allow to select the resource properties to be returned. # noqa: E501

    :param id:
    :type id: str
    :param scope: This parameter extends the set of targeted resources beyond the base resource identified with the path component of the URI. No scoping mechanism is specified in the present document.
    :type scope: dict | bytes
    :param filter: This parameter reduces the targeted set of resources by applying a filter to the scoped set of resource representations. Only resource representations for which the filter construct evaluates to \&quot;true\&quot; are targeted. No filter language is specified in the present document.
    :type filter: str
    :param attributes: This parameter specifies the attributes of the scoped resources that are returned.
    :type attributes: List[str]
    :param fields: This parameter specifies the attribute field of the scoped resources that are returned.
    :type fields: List[str]

    :rtype: Union[ServiceProfile, Tuple[ServiceProfile, int], Tuple[ServiceProfile, int, Dict[str, str]]
    """

    if connexion.request.is_json:
        scope =  Scope.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        serviceProfile=serviceProfileHelper.get_resource(id_)
    except ValueError:
        response=ErrorResponse(ErrorResponseError('NOT_FOUND: Cannot find resource.'))
        return make_response(jsonify(response),404)

    return make_response(serviceProfile.data,200)

def allocate_nssi(slice_profile):  # noqa: E501
    """to allocate a network slice subnet instance provided by the service provider, the network slice subnet instance may be new or existing

    With HTTP POST a complete Slice Profile is created if it does not exist. # noqa: E501

    :param slice_profile:
    :type slice_profile: dict | bytes

    :rtype: Union[SliceProfile, Tuple[SliceProfile, int], Tuple[SliceProfile, int, Dict[str, str]]
    """

    if connexion.request.is_json:
        slice_profile = SliceProfile.from_dict(connexion.request.get_json())  # noqa: E501

    json_object = connexion.request.get_json()

    identifier=uuid.uuid1()

    sliceProfileHeper.create_service_profile(identifier,json.dumps(json_object))

    sliceProfile.slice_profile_id(identifier)

    return sliceProfile



def deallocate_nssi(slice_profile_id):  # noqa: E501
    """Deallocates a Network Slice Subnet

    With HTTP DELETE one resource is deleted. The resources to be deleted is identified with the target URI. # noqa: E501

    :param slice_profile_id:
    :type slice_profile_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    try:
        SliceProfileHelper.delete_resource(slice_profile_id)
    except ValueError:
        response=ErrorResponse(ErrorResponseError('NOT_FOUND: Cannot find service profile.'))
        return make_response(jsonify(response),404)

    return


def get_nssi(slice_profile_id, scope=None, filter=None, attributes=None, fields=None):  # noqa: E501
    """Reads Slice Profile information

    With HTTP GET resources are read. The resources to be retrieved are identified with the target URI. The attributes and fields parameter of the query components allow to select the resource properties to be returned. # noqa: E501

    :param slice_profile_id:
    :type slice_profile_id: str
    :param scope: This parameter extends the set of targeted resources beyond the base resource identified with the path component of the URI. No scoping mechanism is specified in the present document.
    :type scope: dict | bytes
    :param filter: This parameter reduces the targeted set of resources by applying a filter to the scoped set of resource representations. Only resource representations for which the filter construct evaluates to \&quot;true\&quot; are targeted. No filter language is specified in the present document.
    :type filter: str
    :param attributes: This parameter specifies the attributes of the scoped resources that are returned.
    :type attributes: List[str]
    :param fields: This parameter specifies the attribute field of the scoped resources that are returned.
    :type fields: List[str]

    :rtype: Union[SliceProfile, Tuple[SliceProfile, int], Tuple[SliceProfile, int, Dict[str, str]]
    """

    try:
        sliceProfile=sliceProfileHelper.get_resource(slice_profile_id)
    except ValueError:
        response=ErrorResponse(ErrorResponseError('NOT_FOUND: Cannot find resource.'))
        return make_response(jsonify(response),404)

    return make_response(sliceProfile.data,200)
