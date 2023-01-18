# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.
    * Send and receive SMS, Viber, WhatsApp and Telegram messages
    * Manage contacts and groups. * Fetch detailed info about phone numbers
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


class BlacklistApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_to_blacklist(self, number_to_blacklist, **kwargs):  # noqa: E501
        """Adds a phone number to the blacklist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_to_blacklist(number_to_blacklist, async_req=True)
        >>> result = thread.get()

        :param number_to_blacklist: Phone number to be blacklisted (required)
        :type number_to_blacklist: NumberToBlacklist
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
        return self.add_to_blacklist_with_http_info(number_to_blacklist, **kwargs)  # noqa: E501

    def add_to_blacklist_with_http_info(self, number_to_blacklist, **kwargs):  # noqa: E501
        """Adds a phone number to the blacklist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_to_blacklist_with_http_info(number_to_blacklist, async_req=True)
        >>> result = thread.get()

        :param number_to_blacklist: Phone number to be blacklisted (required)
        :type number_to_blacklist: NumberToBlacklist
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
            'number_to_blacklist'
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
                    f"Got an unexpected keyword argument {key} to method add_to_blacklist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'number_to_blacklist' is set
        if self.api_client.client_side_validation and ('number_to_blacklist' not in local_var_params or  # noqa: E501
                                                        local_var_params['number_to_blacklist'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `number_to_blacklist` when calling `add_to_blacklist`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'number_to_blacklist' in local_var_params:
            body_params = local_var_params['number_to_blacklist']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            '/phonebook/blacklist', 'POST',
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

    def delete_from_blacklist(self, phone, **kwargs):  # noqa: E501
        """Deletes a phone number from the blacklist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_from_blacklist(phone, async_req=True)
        >>> result = thread.get()

        :param phone: A phone number (required)
        :type phone: str
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
        return self.delete_from_blacklist_with_http_info(phone, **kwargs)  # noqa: E501

    def delete_from_blacklist_with_http_info(self, phone, **kwargs):  # noqa: E501
        """Deletes a phone number from the blacklist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_from_blacklist_with_http_info(phone, async_req=True)
        >>> result = thread.get()

        :param phone: A phone number (required)
        :type phone: str
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
            'phone'
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
                    f"Got an unexpected keyword argument {key} to method delete_from_blacklist"
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if self.api_client.client_side_validation and ('phone' not in local_var_params or  # noqa: E501
                                                        local_var_params['phone'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `phone` when calling `delete_from_blacklist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

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
            '/phonebook/blacklist/{phone}', 'DELETE',
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

    def fetch_blacklist(self, **kwargs):  # noqa: E501
        """Returns all blacklisted phone numbers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_blacklist(async_req=True)
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
        :rtype: FetchBlacklistSuccess
        """
        kwargs['_return_http_data_only'] = True
        return self.fetch_blacklist_with_http_info(**kwargs)  # noqa: E501

    def fetch_blacklist_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all blacklisted phone numbers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_blacklist_with_http_info(async_req=True)
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
        :rtype: tuple(FetchBlacklistSuccess, status_code(int), headers(HTTPHeaderDict))
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
                    f"Got an unexpected keyword argument {key} to method fetch_blacklist"
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
            200: "FetchBlacklistSuccess",
            401: "ErrorPhonebook",
        }

        return self.api_client.call_api(
            '/phonebook/blacklist', 'GET',
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

    def is_blacklisted(self, phone, **kwargs):  # noqa: E501
        """Checks if a phone number is blacklisted  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.is_blacklisted(phone, async_req=True)
        >>> result = thread.get()

        :param phone: A phone number (required)
        :type phone: str
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
        return self.is_blacklisted_with_http_info(phone, **kwargs)  # noqa: E501

    def is_blacklisted_with_http_info(self, phone, **kwargs):  # noqa: E501
        """Checks if a phone number is blacklisted  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.is_blacklisted_with_http_info(phone, async_req=True)
        >>> result = thread.get()

        :param phone: A phone number (required)
        :type phone: str
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
            'phone'
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
                    f"Got an unexpected keyword argument {key} to method is_blacklisted"
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone' is set
        if self.api_client.client_side_validation and ('phone' not in local_var_params or  # noqa: E501
                                                        local_var_params['phone'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `phone` when calling `is_blacklisted`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone' in local_var_params:
            path_params['phone'] = local_var_params['phone']  # noqa: E501

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
            '/phonebook/blacklist/{phone}', 'GET',
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
