"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.  * Send and receive SMS, Viber, WhatsApp and Telegram messages. * Manage contacts and groups. * Fetch detailed info about phone numbers. * Blacklist phone numbers to make sure you're not sending any unwanted messages.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from messente_api.api_client import ApiClient, Endpoint
from messente_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from messente_api.model.contact_envelope import ContactEnvelope
from messente_api.model.contact_fields import ContactFields
from messente_api.model.contact_list_envelope import ContactListEnvelope
from messente_api.model.contact_update_fields import ContactUpdateFields
from messente_api.model.error_phonebook import ErrorPhonebook
from messente_api.model.group_list_envelope import GroupListEnvelope


class ContactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_contact_to_group(
            self,
            group_id,
            phone,
            **kwargs
        ):
            """Adds a contact to a group  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_contact_to_group(group_id, phone, async_req=True)
            >>> result = thread.get()

            Args:
                group_id (str): String in UUID format
                phone (str): A phone number

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['group_id'] = \
                group_id
            kwargs['phone'] = \
                phone
            return self.call_with_http_info(**kwargs)

        self.add_contact_to_group = Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/groups/{groupId}/contacts/{phone}',
                'operation_id': 'add_contact_to_group',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                    'phone',
                ],
                'required': [
                    'group_id',
                    'phone',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (str,),
                    'phone':
                        (str,),
                },
                'attribute_map': {
                    'group_id': 'groupId',
                    'phone': 'phone',
                },
                'location_map': {
                    'group_id': 'path',
                    'phone': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__add_contact_to_group
        )

        def __create_contact(
            self,
            contact_fields,
            **kwargs
        ):
            """Creates a new contact  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_contact(contact_fields, async_req=True)
            >>> result = thread.get()

            Args:
                contact_fields (ContactFields):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ContactEnvelope
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['contact_fields'] = \
                contact_fields
            return self.call_with_http_info(**kwargs)

        self.create_contact = Endpoint(
            settings={
                'response_type': (ContactEnvelope,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/contacts',
                'operation_id': 'create_contact',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'contact_fields',
                ],
                'required': [
                    'contact_fields',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'contact_fields':
                        (ContactFields,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'contact_fields': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_contact
        )

        def __delete_contact(
            self,
            phone,
            **kwargs
        ):
            """Deletes a contact  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_contact(phone, async_req=True)
            >>> result = thread.get()

            Args:
                phone (str): A phone number

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['phone'] = \
                phone
            return self.call_with_http_info(**kwargs)

        self.delete_contact = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/contacts/{phone}',
                'operation_id': 'delete_contact',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'phone',
                ],
                'required': [
                    'phone',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'phone':
                        (str,),
                },
                'attribute_map': {
                    'phone': 'phone',
                },
                'location_map': {
                    'phone': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_contact
        )

        def __fetch_contact(
            self,
            phone,
            **kwargs
        ):
            """Lists a contact  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetch_contact(phone, async_req=True)
            >>> result = thread.get()

            Args:
                phone (str): A phone number

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ContactEnvelope
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['phone'] = \
                phone
            return self.call_with_http_info(**kwargs)

        self.fetch_contact = Endpoint(
            settings={
                'response_type': (ContactEnvelope,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/contacts/{phone}',
                'operation_id': 'fetch_contact',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'phone',
                ],
                'required': [
                    'phone',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'phone':
                        (str,),
                },
                'attribute_map': {
                    'phone': 'phone',
                },
                'location_map': {
                    'phone': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetch_contact
        )

        def __fetch_contact_groups(
            self,
            phone,
            **kwargs
        ):
            """Lists groups of a contact  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetch_contact_groups(phone, async_req=True)
            >>> result = thread.get()

            Args:
                phone (str): A phone number

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                GroupListEnvelope
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['phone'] = \
                phone
            return self.call_with_http_info(**kwargs)

        self.fetch_contact_groups = Endpoint(
            settings={
                'response_type': (GroupListEnvelope,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/contacts/{phone}/groups',
                'operation_id': 'fetch_contact_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'phone',
                ],
                'required': [
                    'phone',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'phone':
                        (str,),
                },
                'attribute_map': {
                    'phone': 'phone',
                },
                'location_map': {
                    'phone': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetch_contact_groups
        )

        def __fetch_contacts(
            self,
            **kwargs
        ):
            """Returns all contacts  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetch_contacts(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                group_ids ([str]): Optional one or many group id strings in UUID format. For example: \"/contacts?groupIds=group_id_one&groupIds=group_id_two\" . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ContactListEnvelope
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.fetch_contacts = Endpoint(
            settings={
                'response_type': (ContactListEnvelope,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/contacts',
                'operation_id': 'fetch_contacts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_ids',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_ids':
                        ([str],),
                },
                'attribute_map': {
                    'group_ids': 'groupIds',
                },
                'location_map': {
                    'group_ids': 'query',
                },
                'collection_format_map': {
                    'group_ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetch_contacts
        )

        def __remove_contact_from_group(
            self,
            group_id,
            phone,
            **kwargs
        ):
            """Removes a contact from a group  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.remove_contact_from_group(group_id, phone, async_req=True)
            >>> result = thread.get()

            Args:
                group_id (str): String in UUID format
                phone (str): A phone number

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['group_id'] = \
                group_id
            kwargs['phone'] = \
                phone
            return self.call_with_http_info(**kwargs)

        self.remove_contact_from_group = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/groups/{groupId}/contacts/{phone}',
                'operation_id': 'remove_contact_from_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                    'phone',
                ],
                'required': [
                    'group_id',
                    'phone',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (str,),
                    'phone':
                        (str,),
                },
                'attribute_map': {
                    'group_id': 'groupId',
                    'phone': 'phone',
                },
                'location_map': {
                    'group_id': 'path',
                    'phone': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__remove_contact_from_group
        )

        def __update_contact(
            self,
            phone,
            contact_update_fields,
            **kwargs
        ):
            """Updates a contact  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_contact(phone, contact_update_fields, async_req=True)
            >>> result = thread.get()

            Args:
                phone (str): A phone number
                contact_update_fields (ContactUpdateFields):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ContactEnvelope
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['phone'] = \
                phone
            kwargs['contact_update_fields'] = \
                contact_update_fields
            return self.call_with_http_info(**kwargs)

        self.update_contact = Endpoint(
            settings={
                'response_type': (ContactEnvelope,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/phonebook/contacts/{phone}',
                'operation_id': 'update_contact',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'phone',
                    'contact_update_fields',
                ],
                'required': [
                    'phone',
                    'contact_update_fields',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'phone':
                        (str,),
                    'contact_update_fields':
                        (ContactUpdateFields,),
                },
                'attribute_map': {
                    'phone': 'phone',
                },
                'location_map': {
                    'phone': 'path',
                    'contact_update_fields': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_contact
        )
