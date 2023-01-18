# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.
    * Send and receive SMS, Viber, WhatsApp and Telegram messages.
    * Manage contacts and groups.
    * Fetch detailed info about phone numbers.
    * Blacklist phone numbers to make sure you're not sending any unwanted messages.
    Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# python 2 and python 3 compatibility library
import six

from messente_api.api_client import ApiClient
from messente_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_group(self, group_name, **kwargs):  # noqa: E501
        """Creates a new group with the provided name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_group(group_name, async_req=True)
        >>> result = thread.get()

        :param group_name: (required)
        :type group_name: GroupName
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupEnvelope
        """
        kwargs['_return_http_data_only'] = True
        return self.create_group_with_http_info(group_name, **kwargs)  # noqa: E501

    def create_group_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Creates a new group with the provided name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_group_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param group_name: (required)
        :type group_name: GroupName
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupEnvelope, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_name` when calling `create_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_name' in local_var_params:
            body_params = local_var_params['group_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            201: "GroupEnvelope",
            400: "ErrorPhonebook",
            401: "ErrorPhonebook",
        }

        return self.api_client.call_api(
            '/phonebook/groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_group(self, group_id, **kwargs):  # noqa: E501
        """Deletes a group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: String in UUID format (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_group_with_http_info(group_id, **kwargs)  # noqa: E501

    def delete_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Deletes a group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: String in UUID format (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `delete_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/phonebook/groups/{groupId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def fetch_group(self, group_id, **kwargs):  # noqa: E501
        """Lists a group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_group(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: String in UUID format (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupEnvelope
        """
        kwargs['_return_http_data_only'] = True
        return self.fetch_group_with_http_info(group_id, **kwargs)  # noqa: E501

    def fetch_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Lists a group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: String in UUID format (required)
        :type group_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupEnvelope, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `fetch_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "GroupEnvelope",
            401: "ErrorPhonebook",
            404: "ErrorPhonebook",
        }

        return self.api_client.call_api(
            '/phonebook/groups/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def fetch_groups(self, **kwargs):  # noqa: E501
        """Returns all groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_groups(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupListEnvelope
        """
        kwargs['_return_http_data_only'] = True
        return self.fetch_groups_with_http_info(**kwargs)  # noqa: E501

    def fetch_groups_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupListEnvelope, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_groups" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "GroupListEnvelope",
            401: "ErrorPhonebook",
        }

        return self.api_client.call_api(
            '/phonebook/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_group(self, group_id, group_name, **kwargs):  # noqa: E501
        """Updates a group with the provided name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group(group_id, group_name, async_req=True)
        >>> result = thread.get()

        :param group_id: String in UUID format (required)
        :type group_id: str
        :param group_name: (required)
        :type group_name: GroupName
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GroupEnvelope
        """
        kwargs['_return_http_data_only'] = True
        return self.update_group_with_http_info(group_id, group_name, **kwargs)  # noqa: E501

    def update_group_with_http_info(self, group_id, group_name, **kwargs):  # noqa: E501
        """Updates a group with the provided name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group_with_http_info(group_id, group_name, async_req=True)
        >>> result = thread.get()

        :param group_id: String in UUID format (required)
        :type group_id: str
        :param group_name: (required)
        :type group_name: GroupName
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GroupEnvelope, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_id',
            'group_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_id' is set
        if self.api_client.client_side_validation and ('group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_id` when calling `update_group`")  # noqa: E501
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['group_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_name` when calling `update_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['groupId'] = local_var_params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_name' in local_var_params:
            body_params = local_var_params['group_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "GroupEnvelope",
            400: "ErrorPhonebook",
            401: "ErrorPhonebook",
            404: "ErrorPhonebook",
        }

        return self.api_client.call_api(
            '/phonebook/groups/{groupId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
