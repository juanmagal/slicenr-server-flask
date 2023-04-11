import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.patch_item import PatchItem  # noqa: E501
from openapi_server.models.resource import Resource  # noqa: E501
from openapi_server.models.scope import Scope  # noqa: E501
from openapi_server import util


def class_nameid_delete(class_name, id):  # noqa: E501
    """Deletes one resource

    With HTTP DELETE one resource is deleted. The resources to be deleted is identified with the target URI. # noqa: E501

    :param class_name: 
    :type class_name: str
    :param id: 
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def class_nameid_get(class_name, id, attributes, scope=None, filter=None, fields=None):  # noqa: E501
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
    return 'do some magic!'


def class_nameid_patch(class_name, id, resource):  # noqa: E501
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
    return 'do some magic!'


def class_nameid_put(class_name, id, resource):  # noqa: E501
    """Replaces a complete single resource or creates it if it does not exist

    With HTTP PUT a complete resource is replaced or created if it does not exist. The target resource is identified by the target URI. # noqa: E501

    :param class_name: 
    :type class_name: str
    :param id: 
    :type id: str
    :param resource: 
    :type resource: dict | bytes

    :rtype: Union[Resource, Tuple[Resource, int], Tuple[Resource, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        resource = Resource.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
