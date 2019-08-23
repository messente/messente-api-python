# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber, WhatsApp and Telegram messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from messente_api.api_client import ApiClient
from messente_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class OmnimessageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_scheduled_message(self, omnimessage_id, **kwargs):  # noqa: E501
        """Cancels a scheduled Omnimessage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_scheduled_message(omnimessage_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str omnimessage_id: UUID of the scheduled omnimessage to be cancelled (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_scheduled_message_with_http_info(omnimessage_id, **kwargs)  # noqa: E501

    def cancel_scheduled_message_with_http_info(self, omnimessage_id, **kwargs):  # noqa: E501
        """Cancels a scheduled Omnimessage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_scheduled_message_with_http_info(omnimessage_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str omnimessage_id: UUID of the scheduled omnimessage to be cancelled (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['omnimessage_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_scheduled_message" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'omnimessage_id' is set
        if ('omnimessage_id' not in local_var_params or
                local_var_params['omnimessage_id'] is None):
            raise ApiValueError("Missing the required parameter `omnimessage_id` when calling `cancel_scheduled_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'omnimessage_id' in local_var_params:
            path_params['omnimessageId'] = local_var_params['omnimessage_id']  # noqa: E501

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

        return self.api_client.call_api(
            '/omnimessage/{omnimessageId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_omnimessage(self, omnimessage, **kwargs):  # noqa: E501
        """Sends an Omnimessage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_omnimessage(omnimessage, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Omnimessage omnimessage: Omnimessage to be sent (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: OmniMessageCreateSuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.send_omnimessage_with_http_info(omnimessage, **kwargs)  # noqa: E501

    def send_omnimessage_with_http_info(self, omnimessage, **kwargs):  # noqa: E501
        """Sends an Omnimessage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_omnimessage_with_http_info(omnimessage, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Omnimessage omnimessage: Omnimessage to be sent (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(OmniMessageCreateSuccessResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['omnimessage']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_omnimessage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'omnimessage' is set
        if ('omnimessage' not in local_var_params or
                local_var_params['omnimessage'] is None):
            raise ApiValueError("Missing the required parameter `omnimessage` when calling `send_omnimessage`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'omnimessage' in local_var_params:
            body_params = local_var_params['omnimessage']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/omnimessage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OmniMessageCreateSuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
